import requests
from email_data import mock_email
from product_lists import product_list
from status_list import status
from formatting import single_json_structure, multiple_json_structure

def add_format (email):
    for i, current_email in enumerate(email):
        print(f"processing mock email {i+1}")
        added_format = requests.post("http://localhost:11434/api/generate", json={
            "model": "phi3.5",
            "prompt": f"""
    you are an automated engine for handling orders through email. your sole task is to collect items found in the order email order.

    critical no-hallucination requirement: you are strictly forbidden from inventing, hallucinating, or pulling product data from outside the provided reference blocks. do not generate fake or placeholder data under any circumstances.

    ### Input Data
    
    [product list]
    {product_list}

    [order email]
    {current_email}

    [status list]
    {status}

    [output requirement]
    return a single json object result with the designed [json structure] for the email order. 
    do not include any other text or markdown block formatting.

    [json structure]
    If there is only one order item: {single_json_structure}
    If there are multiple order items: {multiple_json_structure}
    """,
            "stream": False,
            "format": "json",
            "options": {
                "temperature": 0.0
            }
        })

        print(added_format.json()["response"])
        print("==================================")

add_format(mock_email)

