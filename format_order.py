import requests
from product_lists import product_list
from status_list import status
from formatting import single_json_structure, multiple_json_structure


def add_format (email):
        added_format = requests.post("http://localhost:11434/api/generate", json={
            "model": "phi3.5",
            "prompt": f"""
    You are an automated engine for handling orders through email.  Your sole task is to collect items found in the order email order.

    critical no-hallucination requirement: You are strictly forbidden from inventing, hallucinating, or pulling product data from outside the provided reference blocks. If a product (such as "T-Shirt") does not explicitly appear in the [Validation Matrix Reference] below, it does not exist for this run. Do not generate fake or placeholder data under any circumstances.

    [product list]
    {product_list}

    [order email]
    {email}

    [status list]
    {status}

    [output requirement]
    Return a single JSON object result with the designed [JSON structure] for the email order. 
    Do not include any other text or markdown block formatting.

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

        format_result = added_format.json()["response"]
        return format_result