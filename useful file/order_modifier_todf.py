import json
import pandas as pd
import requests
from email_data import mock_email
from format_order import add_format
from name_detect import name_detection
from order_validator import order_validation
from product_lists import product_list


def find_nested_key(data, target_keys):
    """Helper to find a key in a dictionary regardless of casing or nesting."""
    if not isinstance(data, dict):
        return None
    # Check current level keys flexibly
    for a, b in data.items():
        if a.lower().strip() in [tk.lower() for tk in target_keys]:
            return b
    # Look one level deeper if the LLM nested the response under a root key (e.g., {"order": {...}})
    for a, b in data.items():
        if isinstance(v, dict):
            res = find_nested_key(b, target_keys)
            if res is not None:
                return res
    return None


def modifier(email_list):
    """Processes a list of emails through name detection, formatting,

    validation, and LLM structured synthesis. Returns a flat list of items
    ready for a Pandas DataFrame.
    """
    all_flat_items = []

    for i, current_email in enumerate(email_list):
        print(f"--- Processing mock email {i+1} ---")

        # 1. Pipeline Extractions
        customer_name = name_detection(current_email)
        format_result = add_format(current_email)
        validated_order = order_validation(current_email, product_list)

        # 2. Query Ollama / Phi3.5
        resp = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "phi3.5",
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

    ### Strict Transformation Rules
    You must execute these steps in order:

    1. **Map Customer Identity:** Map the top-level "customer" string field by copying the exact string found within [Customer Name Reference].
    2. **Synchronize Item Structure (1:1 standard):** Read the structured matrix/table provided in [Validation Result Reference]. For every single distinct row object present in that reference, create exactly one item object inside the final output "items" array. Do not drop, skip, combine, or invent records.
    3. **Enforce Database Standard Fields:** For each item mapping, inject and format the following explicit keys pulled from your validated data:
        * "product_name": Copy the official product description exactly as written in [Validation Result Reference].
        * "quantity": Map the exact numeric quantity input.
        * "sku": Map the assigned internal SKU value.
        * "unit_price": Map the designated per-item catalog pricing decimal value.
        * "subtotal": Map the calculated item row total value.
        * "status": Map the evaluated operational flag (e.g., "VALID", "unlisted", "not enough stock").
    4. **Aggregate Mathematical Total:** Calculate the final top-level "total" field. This must equal the strict mathematical sum of all individual item "subtotal" values in the array. Do not infer or hardcode a static figure.

    ### Output Requirement
    Return ONLY a single valid JSON object block matching this exact architectural structure. Do not include conversational text, markdown wrapping prose, or explanations.
    """,
                "stream": False,
                "format": "json",
                "options": {"temperature": 0.0},
            },
        )

        try:
            raw_response_str = resp.json().get("response", "")

            if not raw_response_str.strip():
                print(f"Warning: Model returned an empty response string for email {i+1}")
                continue

            # load json
            email_data = json.loads(raw_response_str)
            
            # --- DEBUG BLOCK ---
            # If things fail, this helps you inspect the raw layout immediately
            print(f"DEBUG - LLM JSON Payload Keys: {list(email_data.keys())}")

            # Flexible Key Matching to prevent empty results from stylistic casing
            customer = find_nested_key(email_data, ["customer", "customer_name", "name"]) or "UNKNOWN"
            order_total = find_nested_key(email_data, ["total", "order_total", "grand_total"]) or 0.0
            
            # Fallback to find the items list wherever the LLM left it
            items_list = find_nested_key(email_data, ["items", "item_list", "products", "orders"])

            # Flatten nested JSON hierarchy into separate tabular rows
            for item in items_list:
                if isinstance(item, dict):
                    # Extract keys flexibly to account for camelCase variations
                    p_name = find_nested_key(item, ["product_name", "productname", "product"])
                    qty = find_nested_key(item, ["quantity", "qty"])
                    sku = find_nested_key(item, ["sku"])
                    u_price = find_nested_key(item, ["unit_price", "unitprice", "price"])
                    subt = find_nested_key(item, ["subtotal", "sub_total"])
                    stat = find_nested_key(item, ["status", "flag"])

                    flat_row = {
                        "customer": customer,
                        "order_total": order_total,
                        "product_name": p_name,
                        "quantity": qty,
                        "sku": sku,
                        "unit_price": u_price,
                        "subtotal": subt,
                        "status": stat,
                    }
                    all_flat_items.append(flat_row)

        except Exception as e:
            print(f"Unexpected processing error on email {i+1}: {e}")

        print(f"Successfully processed email {i+1}\n")

    return all_flat_items




processed_records = modifier(mock_email)

if processed_records:
    df = pd.DataFrame(processed_records)
    print(df.to_string(index=False))
else:
    print("\nNo item records were parsed. DataFrame is empty.")