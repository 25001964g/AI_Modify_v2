import requests
from email_data import mock_email, demo_email
from product_lists import product_list

#Harness: Identify missing/ambiguous parameters before extraction
def item_extract(email, product_list):
    #This acts as an initial control step to steer the extraction
    extract_prompt = f"""
You are an administrative data extraction engine. Your sole job is to read an order email and extract the requested items into raw JSON.

[ORDER EMAIL]
{email}

[CRITICAL INSTRUCTIONS]
1. Read the email and identify the a list of requested products and their quantities.
2. Quantity must be float type. If a quantity is missing or generic (e.g., "some", "a few"), set the quantity value to null.
3. Output ONLY a valid JSON object matching the template layout below. Do not use markdown backticks (```). Do not include chat preamble or notes.

[OUTPUT LAYOUT]
{{
  "items": [
    {{"product_name": "Item 1", "quantity": Number or null}}
  ]
}}
"""

    order_extracted = requests.post("http://localhost:11434/api/generate", json={
        "model": "llama3.2",
        #"model" : "phi3.5",  
        "prompt": extract_prompt,
        "stream": False,
        "format": "json",
        "options": {
            "temperature": 0.0,  
            "num_predict": 150 
        }
    })

    # code for testing purpose    
    order_list = order_extracted.json()["response"]
    return order_list
    #print(order_list)

#item_extract(mock_email[1], product_list)