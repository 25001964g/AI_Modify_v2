import requests
from email_data import mock_email, demo_email
from product_lists import product_list

#Harness: Identify missing/ambiguous parameters before extraction
def check_status(email, product_list):
    #This acts as an initial control step to steer the extraction
    invalid_check_prompt = f"""
You are an administrative office assistant. Your sole job is to review a customer email, cross-reference it with our official inventory, and write a structured, plain-text analysis log.

[OFFICIAL PRODUCT LIST]
{product_list}

[ORDER EMAIL]
{email}

[CRITICAL INSTRUCTIONS - EXECUTE IN ORDER]
STEP 1 (EXTRACT ONLY): Read the [ORDER EMAIL] and identify the exact items requested. 
    - Read the [ORDER EMAIL] line by line. Identify the items explicitly written by the customer.
    - Do not create items that are not in the email.

STEP 2 (CROSS-REFERENCE): Look up the extracted items in the [OFFICIAL PRODUCT LIST].
    - If the item name perfectly matches an inventory item (e.g., "jeans" matches "jeans"), mark it as VALID.
    - If the item name is generic (e.g. T-shirt)and matches multiple options ("T-shirt-black" or "T-shirt-Yellow"), mark the product name null and mark the status as AMBIGUOUS.
    - If the quantity is not specify (e.g. some, few, a lot of), mark the quantity as null and mark the status as AMBIGUOUS.
    - If the item name is the SKU, directly match the inventory item (e.g. "SKU0001" matches "Apple"), mark it as VALID.
    - If the item is completely absent, mark it as UNLISTED.

STEP 3 (WRITE REPORT): 
    - Fill out the exact layout template below based on Step 1 and Step 2. Do not include markdown code block backticks.
    - Do not include any greeting preamble, concluding remarks, notes or markdown code blocks (backticks).

[OUTPUT LAYOUT]
### ANALYSIS SUMMARY
[Write your 1-sentence analysis summary note here]

### EXTRACTED LINE ITEMS
* Product Name: [Name of product] | Quantity: [Number requested] | Status: [VALID / UNLISTED / AMBIGUOUS]
            """
    
    checking_valid = requests.post("http://localhost:11434/api/generate", json={
        "model": "llama3.2",
        #"model" : "phi3.5",
        "prompt": invalid_check_prompt,
        "stream": False
    })

    # code for testing purpose    
    order_status = checking_valid.json()["response"]
    print(order_status)

check_status(mock_email[1], product_list)