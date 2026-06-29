# email_security.py
import json
import re
import requests
import dns.resolver


def extract_sender_domain(email_content):
    """
    Parses the email text to find the sender's email address domain.
    Looks for typical patterns like "From: Name <sender@domain.com>" or "from: sender@domain.com"
    """
    from_match = re.search(r'(?:From|from):\s*(?:.*<)?([\w\.-]+@[\w\.-]+\.\w+)>?', email_content)
    if from_match:
        email_address = from_match.group(1).lower()
        domain = email_address.split('@')[-1]
        return domain
    return None


def is_domain_globally_blacklisted(domain):
    """
    Performs a real-time DNS lookup against Spamhaus Domain Block List (DBL).
    Returns True if the domain is flagged globally as malicious.
    """
    if not domain:
        return False

    # Spamhaus DBL requires appending their query endpoint to your domain target
    query_target = f"{domain}.dbl.spamhaus.org"
    try:
        # If the domain is blacklisted, it returns an IP address record (like 127.0.1.2)
        dns.resolver.resolve(query_target, 'A')
        return True
    except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer):
        return False  # Domain is clean / not found in blocklist
    except Exception:
        return False  # Fallback if DNS timeout happens


def check_spam_or_phishing(email_content, model_name="phi3.5", debug=False):
    """
    Evaluates whether an email is spam or phishing.
    First checks the global DNS blocklist. If caught, skips the LLM to save system power.
    Otherwise, runs the advanced LLM evaluation on the content body.
    """
    # Step 1: Extract domain and run the Global Blocklist query
    sender_domain = extract_sender_domain(email_content)

    if sender_domain and is_domain_globally_blacklisted(sender_domain):
        # Match found! Return a mock high-risk JSON payload to stop processing immediately
        return {
            "evaluation": "Phishing",
            "sender_spam_percentage": 100,
            "sender_phishing_percentage": 100,
            "body_spam_percentage": 0,
            "body_phishing_percentage": 0,
            "risk_flags": ["Global Blocklist Match", "High Risk Domain"],
            "brief_reason": f"CRITICAL: The sender domain ({sender_domain}) is listed on global Spamhaus threat intelligence feeds.",
            "brief_reason2": "Blacklisted domain detected on global security feeds."  # 7 words
        }

    # Step 2: Fallback to LLM assessment if the domain isn't explicitly blacklisted
    try:
        resp = requests.post("http://localhost:11434/api/generate", json={
            "model": model_name,
            "prompt": f"""
You are an advanced email security firewall. Your task is to analyze the email below and calculate separate mathematical probabilities (0-100%) for the SENDER identity and the EMAIL BODY text.

[Scoring Rubric Guidance]
- High Risk (70-100%): Suspicious/spoofed domains, urgent threats, hidden tracking links, requests for credentials or financial actions.
- Medium Risk (30-60%): Bulk marketing aliases, unsolicited newsletters, commercial promotions with aggressive sales language.
- Low Risk (0-25%): Verifiable business domains, expected transactional receipts, personal communications.

[Email to Analyze]
{email_content}

[Output Requirement]
Return a single JSON object. Do not include any markdown wrap or extra text.
Required keys:
- evaluation: "Safe", "Marketing", "Spam", or "Phishing"
- sender_spam_percentage: (Integer 0-100)
- sender_phishing_percentage: (Integer 0-100)
- body_spam_percentage: (Integer 0-100)
- body_phishing_percentage: (Integer 0-100)
- risk_flags: (List of specific triggers found, e.g., ["Mismatched Domain", "Urgent Language"])
- brief_reason: (A 1-sentence summary of why it received these scores)
""",
            "stream": False,
            "format": "json",
            "options": {
                "temperature": 0.0,
                "num_predict": 400
            }
        })

        if resp.status_code == 200:
            ollama_data = resp.json()
            if "response" in ollama_data:
                return json.loads(ollama_data["response"])

        if debug:
            print(f"⚠️ Security API error {resp.status_code}: {resp.text}")
    except Exception as e:
        if debug:
            print(f"⚠️ Security module connection failure: {e}")

    return None