import requests
from order_validator import order_validation
from email_data import mock_email
from product_lists import product_list
from format_order import add_format
from name_detect import name_detection

def modifier(email):
    for i, current_email in enumerate(email):
        print(f"Processing mock email {i+1}")
        # Detect suitable customer name
        customer_name = name_detection(current_email)
        # Order check process
        format_result = add_format(current_email)
        #Harness: add on status check       
        validated_order = order_validation(current_email, product_list)
        resp = requests.post("http://localhost:11434/api/generate", json={
            #"model": "llama3.2",
            "model" : "phi3.5",
            "prompt": f"""
    You are a precise backend data-transformation engine. Your sole task is to validate, modify, and format a raw JSON structure based on provided reference data.

    critical no-hallucination requirement: You are strictly forbidden from inventing, hallucinating, or pulling product data from outside the provided reference blocks. If a product (such as "T-Shirt") does not explicitly appear in the [Validation Matrix Reference] below, it does not exist for this run. Do not generate fake or placeholder data under any circumstances.

    ### Input Data

    [Generated Result To Be Modified]
    {format_result}

    [Customer Name Reference]
    {customer_name}

    [Validation Result Reference]
    {validated_order}

    [Strict Transformation Rules]
    1. Map Customer Identity: Map the top-level "customer" string field by copying the exact string found within [Customer Name Reference].
    2. Synchronize Item Structure (1:1 standard): Read the structured matrix/table provided in [Validation Result Reference]. For every single distinct row object present in that reference, create exactly one item object inside the final output "items" array. Do not drop, skip, combine, or invent records.
    3. Enforce Database Standard Fields: For each item mapping, inject and format the following explicit keys pulled from your validated data:
        * "product_name": Copy the official product description exactly as written in [Validation Result Reference].
        * "quantity": Map the exact numeric quantity input.
        * "sku": Map the assigned internal SKU value.
        * "price": Map the designated per-item catalog pricing decimal value.
        * "subtotal": Map the calculated item row total value.
        * "status": Map the evaluated operational flag (e.g., "VALID", "unlisted", "not enough stock").
    4. Aggregate Mathematical Total: Calculate the final top-level "total" field. This must equal the strict mathematical sum of all individual item "subtotal" values in the array. Do not infer or hardcode a static figure.

    [Output Requirement]
    Return ONLY the final, modified JSON object matching this exact architectural structure. Do not include conversational text, markdown wrapping prose, or explanations. The output must be valid, parseable JSON.
    """,
            "stream": False,
            "format": "json",
            "options": {
                "temperature": 0.0
            }
        })
        
        print(resp.json()["response"])
        print("==================================")
        
modifier(mock_email)