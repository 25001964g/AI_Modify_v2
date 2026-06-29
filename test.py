import pandas as pd
import numpy as np
import json
import requests
from order_extractor import item_extract
from email_data import mock_email, demo_email
from product_lists import product_list


# 2. Get the structured JSON string from your Ollama request response
# (Simulated raw response string from your prompt above)
ai_response_string = item_extract(mock_email[3], product_list)

# 3. Convert the AI's "items" array straight into a Pandas DataFrame
extracted_data = json.loads(ai_response_string)
df = pd.DataFrame(extracted_data['items'])
print(df)