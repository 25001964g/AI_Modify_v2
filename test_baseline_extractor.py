import requests
from email_data import mock_email
from product_lists import product_list
from status_list import status
from order_extractor_plain import item_extract_plain

for i, current_email in enumerate(mock_email):
    print(f"Processing mock email {i+1}")
    item_extracted = item_extract_plain(current_email)
    resp = requests.post("http://localhost:11434/api/generate", json={
        "model": "phi3.5",
        "prompt": f"""
    you are an automated engine for handling orders through email. your sole task is to collect items found in the order email order.

    critical no-hallucination requirement: you are strictly forbidden from inventing, hallucinating, or pulling product data from outside the provided reference blocks. do not generate fake or placeholder data under any circumstances.

    [product list]
    {product_list}

    [order email]
    {current_email}

    [status list]
    {status}

    [output requirement]
    Refer to {item_extracted},
    Return a single JSON object result for the email order including: client_name, product_name, SKU, quantity, unit_price, subtotal, total, each order item's status. 
    Do not include any other text or markdown block formatting.
    """,
        "stream": False,
        "format": "json",
        "options": {
            "temperature": 0.0
        }
    })
    print(resp.json()["response"])
    print("==================================")