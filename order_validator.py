import pandas as pd
import numpy as np
import json
import requests
from order_extractor import item_extract
from email_data import mock_email, demo_email
from product_lists import product_list


#Get the structured JSON string from your Ollama request response
# (Simulated raw response string from your prompt above)
order_list = item_extract(mock_email[0], product_list)

#Load json formatted data to pandas dataframe
extracted_data = json.loads(order_list)
df = pd.DataFrame(extracted_data['items'])

# Data Cleaning for matching
df['product_name'] = df['product_name'].str.lower().str.strip()
product_list['product_name'] = product_list['product_name'].str.lower().str.strip()

#Gnerated dataframe Left join product list
merged_df = pd.merge(df, product_list, on='product_name', how='left')

# Conditions for invalid input
# Condition 1: Item Name cannot match with product list
# Condition 2: Quantity was missing or ambiguous ("some", "few")
conditions = [
    (merged_df['SKU'].isna()),       
    (merged_df['quantity'].isna())   
]
choices = ['UNLISTED', 'AMBIGUOUS']

#If status is not UNLISTED and AMBIGUOUS, set the status as VALID
merged_df['status'] = np.select(conditions, choices, default='VALID')

#Fill in NA data to 0
merged_df['unit_price'] = merged_df['unit_price'].fillna(0.00)
merged_df['quantity_input'] = merged_df['quantity'].fillna(0)

#Calculate the subtotal for each order item
merged_df['subtotal'] = merged_df['quantity_input'] * merged_df['unit_price']

print(merged_df[['product_name', 'quantity', 'SKU', 'unit_price', 'subtotal', 'status']])