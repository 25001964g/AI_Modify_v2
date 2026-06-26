import requests
from order_validator import check_status
from email_data import mock_email, demo_email
from product_lists import product_list

for i, current_email in enumerate(mock_email):
    print(f"Processing mock email {i+1}")
    #Harness: add on status check
    order_status = check_status(current_email, product_list)
    resp = requests.post("http://localhost:11434/api/generate", json={
        #"model": "llama3.2",
        "model" : "phi3.5",
        "prompt": f"""
Do not provide any programming function code and script.
You are an automated engine for handling orders through email. Your sole task is to collect items found in the order email and map their validation statuses.

[product list]
{product_list}

[order email]
{current_email}

[validation result]
{order_status}

[CRITICAL INSTRUCTIONS - EXECUTE IN ORDER]
1. Read the [order email] to extract the client name.
2. Read the [validation result] text line by line to find the extracted product names, quantities. 
3. Count the exact number of bullet points in the [validation result]. Your output array MUST contain exactly that many items. Do not invent products or split items.
4. For each item, look up its matching details in the [product list] to find its exact SKU and unit_price. 
5. Compute the math textually: subtotal is (quantity * unit_price). Total is the sum of all subtotals.
6. Get the status stated in [validation result], and fill in the status for the output. 
7. Write a helpful "remark" sentence if an item's status is AMBIGUOUS or UNLISTED in [validation result]. Otherwise, use null.

[output requirement]
Return a single JSON object result for the [order email] and generated [validation result] including: client_name, product_name, SKU, quantity, unit_price, subtotal, total, status, remark. 
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