import requests
from email_data import mock_email, demo_email
from product_lists import product_list
from status_list import status
from name_detect import name_detection

for i, current_email in enumerate(mock_email):
    print(f"Processing mock email {i+1}")
    name_detected = name_detection(current_email)
    resp = requests.post("http://localhost:11434/api/generate", json={
        "model": "phi3.5",
        "prompt": f"""
You are an automated engine for handling orders through email.  Your sole task is to collect items found in the order email order.

[product list]
{product_list}

[order email]
{current_email}

[customer name]
{name_detected}

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
            "num_predict": 150 
        }
    })
    print(resp.json()["response"])
    print("==================================")