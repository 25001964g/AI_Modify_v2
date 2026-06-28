import requests
from email_data import mock_email, demo_email

#Harness: Identify missing/ambiguous parameters before extraction
def check_status(email):
    #This acts as an initial control step to steer the extraction
    name_detect_prompt = f"""
You are an administrative office assistant. Your sole job is to review a customer email and extract the lowercase customer brand name.

[REGULATORY EXAMPLES FOR REFERENCE]
- Sender: "From: admin@apple.com" -> Customer_Name: apple
- Sender: "From: support@TESLA.co.uk" -> Customer_Name: TESLA
- Sender: "From: orders@cloThcompany.com" -> Customer_Name: cloThcompany

[ORDER EMAIL]
{email}

[CRITICAL INSTRUCTIONS - EXECUTE IN ORDER]
1. Scan the [ORDER EMAIL] to locate the line starting with "From:".
2. Isolate the email address on that line.
3. Mimic the [REGULATORY EXAMPLES] exactly: extract only the core company or brand text between the "@" symbol and the extensions. 
4. Do not include any periods, extensions like ".com", or backticks (```). Output ONLY the template layout below.

[OUTPUT LAYOUT]
### EXTRACTED LINE ITEMS
* Customer_Name: [Name of Customer]
            """
    
    name_detect = requests.post("http://localhost:11434/api/generate", json={
        #"model": "llama3.2",
        "model" : "phi3.5",
        "prompt": name_detect_prompt,
        "stream": False
    })

    # code for testing purpose    
    customer_name = name_detect.json()["response"]
    #return customer_name
    print(customer_name)

check_status(mock_email[0])