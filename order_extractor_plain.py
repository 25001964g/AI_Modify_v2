import requests
from email_data import mock_email

#Harness: Identify missing/ambiguous parameters before extraction
def item_extract_plain(email):
    #This acts as an initial control step to steer the extraction
    extract_prompt = f"""
You are an administrative data extraction engine. Your sole job is to read an order email and extract the requested items.

[ORDER EMAIL]
{email}

[CRITICAL INSTRUCTIONS]
1. Read the email and identify the a list of requested products and their quantities.
2. Quantity must be float type. If a quantity is missing or generic (e.g., "some", "a few"), set the quantity value to null.
3. Output ONLY a valid JSON object matching the template layout below. Do not use markdown backticks (```). Do not include chat preamble or notes.
4. Detect the language of the email above.
5. If the email is NOT in English, translate the full email to English.
6. If the email IS already in English.

[OUTPUT LAYOUT]
### extracted line items
*Product Name: [Name of product] | Quantity: [Number requested]
"""

    order_extracted = requests.post("http://localhost:11434/api/generate", json={
        #"model": "llama3.2",
        "model" : "phi3.5",  
        "prompt": extract_prompt,
        "stream": False,
        "format": "json",
        "options": {
            "temperature": 0.0,  
            "num_predict": 150 
        }
    })

    order_list = order_extracted.json()["response"]
    return order_list

print(item_extract_plain(mock_email[7]))