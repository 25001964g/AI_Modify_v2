import requests
from test_email.mock_emails import mock_email
from test_email.single_product import test_email_1
from test_email.multiple_product import test_email_2
from test_email.language_single_product import test_email_3
from test_email.language_multiple_product import test_email_4
from general_information.product_lists import product_list
from general_information.status_list import status
from general_information.formatting import json_structure

def baseline_format (email, product_list, status):
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

    [Ouput Structure]
    {json_structure}

    [Strict Transformation Rules]
        1. Map Customer Identity: Map the top-level "customer" string field by copying the exact string found within [order email].
        2. Synchronize Item Structure (1:1 standard): Read the [order_email] provided. For every single distinct row object present in that reference, create exactly one item object inside the final output "items" array. Do not drop, skip, combine, or invent records.
        3. Enforce Database Standard Fields: For each item mapping, inject and format the following explicit keys pulled from your validated data:
            * "product_name": Copy the official product description exactly as written in [order email].
            * "quantity": Map the exact numeric quantity input.
            * "sku": Map the assigned internal SKU value.
            * "price": Map the designated per-item catalog pricing decimal value.
            * "subtotal": Map the calculated item row total value.
            * "status": Map the evaluated operational flag (e.g., "valid", "unlisted", "ambiguous","not enough stock").
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

        print(added_format.json()["response"])
        print("==================================")

#baseline_format(mock_email, product_list, status)
baseline_format(test_email_1, product_list, status)
#baseline_format(test_email_2, product_list, status)
#baseline_format(test_email_3, product_list, status)
#baseline_format(test_email_4, product_list, status)
