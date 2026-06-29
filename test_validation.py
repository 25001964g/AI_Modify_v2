import requests
from order_validator import order_validation
from email_data import mock_email, demo_email
from product_lists import product_list
from status_list import status

for i, current_email in enumerate(mock_email):
    print(f"Processing mock email {i+1}")
    #Harness: add on status check
    order_status = order_validation(current_email, product_list)
    resp = requests.post("http://localhost:11434/api/generate", json={
        "model": "llama3.2",
        #"model" : "phi3.5",
        "prompt": f"""
Do not provide any programming function code and script.
You are an automated engine for handling orders through email. Your sole task is to collect items found in the order email and map their validation statuses.

[ORDER EMAIL]
{current_email}

[validation result]
{order_validation}

[CRITICAL INSTRUCTIONS - EXECUTE IN ORDER]
1. Read the [ORDER EMAIL] to extract the customer name only.
2. Read the [validation result] to extract the items.
3. Count the exact number of bullet points in the [validation result]. Your output array MUST contain exactly that many items. Do not invent products or split items.

[output requirement]
Return a single JSON object result for the generated [validation result] including: client_name, product_name, SKU, quantity, unit_price, subtotal, total, status, remark. 
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