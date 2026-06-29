# test_customer_name.py
import json
import requests
from email_data import mock_email, demo_email
from product_lists import product_list
from status_list import status

# Import the screening module from your separate file
from email_security import check_spam_or_phishing

for i, current_email in enumerate(mock_email):
    print(f"\n==================================================")
    print(f"PROCESSING MOCK EMAIL {i + 1}")
    print(f"==================================================")

    # STEP 1: Run the screening step (debug is False by default, keeping it hidden)
    security_report = check_spam_or_phishing(current_email, model_name="phi3.5", debug=False)

    if security_report:
        verdict = security_report.get("evaluation", "Safe")

        # Explicitly print the clear, polished final report
        print(f"\n🛡️  [FINAL REPORT] Security Screening Result:")
        print(f"   ├─ Verdict:              {verdict}")
        #print(f"   ├─ Sender email:     {current_email}")
        print(f"   ├─ Sender Spam Risk:     {security_report.get('sender_spam_percentage')}%")
        print(f"   ├─ Sender Phishing Risk: {security_report.get('sender_phishing_percentage')}%")
        print(f"   ├─ Body Spam Risk:       {security_report.get('body_spam_percentage')}%")
        print(f"   ├─ Body Phishing Risk:   {security_report.get('body_phishing_percentage')}%")
        print(f"   └─ Reason:               {security_report.get('brief_reason')}\n")
        print(f"   └─ Reason2:               {security_report.get('brief_reason2')}\n")

        # Intercept and block unsafe vectors
        if verdict in ["Spam", "Phishing"]:
            print(f"🚨 ORDER BLOCKED: Dropping unsafe malicious email pipeline.")
            print("==================================================")
            continue
    else:
        print("\n❌ CRITICAL: Security report generation failed completely.\n")

    print("🔓 Email cleared. Moving to Step 2 (Order parsing)...")

    # STEP 2: Proceed with processing if the email is clean
    resp = requests.post("http://localhost:11434/api/generate", json={
        "model": "phi3.5",
        "prompt": f"""
Do not provide any programming function code and script.
You are an automated engine for handling orders through email. Your sole task is to collect items found in the order email order.

[product list]
{product_list}

[order email]
{current_email}

[status list]
{status}

[output requirement]
Return a single JSON object result for the email order including: client_name, product_name, SKU, quantity, unit_price, subtotal, total, status, remark. 
Do not include any other text or markdown block formatting.
""",
        "stream": False,
        "format": "json",
        "options": {
            "temperature": 0.0,
            "num_predict": 400
        }
    })

    if resp.status_code == 200:
        try:
            ollama_response = resp.json().get("response", "{}")
            order_data = json.loads(ollama_response)
            print("\n📦 Extracted Order JSON:")
            print(json.dumps(order_data, indent=2))
        except json.JSONDecodeError:
            print("\n❌ Failed to parse valid Order JSON from LLM output.")
    else:
        print(f"\n❌ Server error during extraction endpoint call: {resp.status_code}")

    print("==================================================")