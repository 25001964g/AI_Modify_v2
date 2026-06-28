import requests
from email_data import mock_email, demo_email
from product_lists import product_list
from status_list import status
from formatting import json_structure

for i, current_email in enumerate(mock_email):
    print(f"Processing mock email {i+1}")
    resp = requests.post("http://localhost:11434/api/generate", json={
        "model": "phi3.5",
        "prompt": f"""
Do not provide any programming function code and script.
You are an automated engine for handling orders through email.  Your sole task is to collect items found in the order email order.

[product list]
{product_list}

[order email]
{current_email}

[status list]
{status}

[output requirement]
Return a single JSON object result with the designed [JSON structure] for the email order. 
Do not include any other text or markdown block formatting.

[JSON structure]
{json_structure}
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