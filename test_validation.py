import requests
from order_validator import order_validation
from order_extractor import item_extract
from email_data import mock_email, demo_email
from product_lists import product_list
from status_list import status

for i, current_email in enumerate(mock_email):
    print(f"Processing mock email {i+1}")
    #Harness: add on status check
    order_list, validated_order = order_validation(current_email, product_list)
    resp = requests.post("http://localhost:11434/api/generate", json={
        "model": "llama3.2",
        #"model" : "phi3.5",
        "prompt": f"""
Do not provide any programming function code and script.
You are an automated backend engine for parsing validated order details into raw JSON. Your sole task is to transform provided text data into a structured JSON object.

[extracted result]
{order_list}

[validation result]
{validated_order}

[CRITICAL INSTRUCTIONS - EXECUTE IN ORDER]
1. EXTRACT Client Name: Read the [extracted result] and identify the customer's name only. Set this as the "customer".
2. For the items ordered, Read the [validation result]
    - MAP 1:1 FROM BULLET POINTS: For every single distinct bullet point listing a product, create exactly one item object in the "items" array. Do not merge, split, omit, or invent products.
    - For the "product_name" field inside the items array, you MUST copy the official product name exactly as written in the [validation result]. Do not use the raw names from the [extracted result].
    - CALCULATE TOTAL: The "total" field must be the mathematical sum of all item "subtotal" values.

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