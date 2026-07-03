import requests
from email_data import mock_email
from general_information.product_lists import product_list
from general_information.status_list import status
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

    [Strict Transformation Rules]
    1. Map Customer Identity: Map the top-level "customer" string field by copying the exact string found within [order email].
    2. Synchronize Item Structure (1:1 standard): Read the [order_email] provided. For every single distinct row object present in that reference, create exactly one item object inside the final output "items" array. Do not drop, skip, combine, or invent records.
    3. Enforce Database Standard Fields: For each item mapping, inject and format the following explicit keys pulled from your validated data:
        * "product_name": Copy the official product description exactly as written in [order email].
        * "quantity": Map the exact numeric quantity input.
        * "sku": Map the assigned internal SKU value.
        * "price": Map the designated per-item catalog pricing decimal value.
        * "subtotal": Map the calculated item row total value.
        * "status": Map the evaluated operational flag (e.g., "valid", "unlisted", "ambiguous", "not enough stock").
    4. Aggregate Mathematical Total: Calculate the final top-level "total" field. This must equal the strict mathematical sum of all individual item "subtotal" values in the array. Do not infer or hardcode a static figure.
    5. Language Requirement: All information for the order should be in English.

    [Output Requirement]
    Follow the [Strict Transformation Rules] and Return a single JSON object result for the email order including: customer_name, product_name, SKU, quantity, price, subtotal, total, status. 
    """,
        "stream": False,
        "format": "json",
        "options": {
            "temperature": 0.0
        }
    })
    print(resp.json()["response"])
    print("==================================")