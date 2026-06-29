import pandas as pd
import numpy as np
import json
import requests
from order_extractor import item_extract
from email_data import mock_email, demo_email
from product_lists import product_list

product_list = pd.DataFrame({
    'SKU': ['SKU8821', 'SKU4402'],
    'product_name': ['T-shirt-Black', 'Jeans'],
    'unit_price': [12.50, 3.10]
})

# 2. Raw data extracted from AI (Messy/mixed capitalization)
df = pd.DataFrame([
    {"product_name": "jeans", "quantity": 2.0},
    {"product_name": "jeans", "quantity": None},
    {"product_name": "SKU8821", "quantity": 5.0},
    {"product_name": "SKU8820", "quantity": 5.0},
    {"product_name": "Invalid_ITEM", "quantity": 1.0}
])

# Data Cleaning for matching
df['match_key'] = df['product_name'].str.lower().str.strip()

product_list['match_name'] = product_list['product_name'].str.lower().str.strip()
product_list['match_sku'] = product_list['SKU'].str.lower().str.strip()

all_items = []

for index, row in df.iterrows():
    item_row = pd.DataFrame([row])

    #If customer provide product name:
    is_sku = row['match_key'].startswith('sku')

    if is_sku == False:
        # Match using product name
        single_item = pd.merge(item_row, product_list, left_on='match_key', right_on='match_name', how='left')
    else:
        # Match using SKU code
        single_item = pd.merge(item_row, product_list, left_on='match_key', right_on='match_sku', how='left')
        # If using SKU matched an inventory item, product_name will become product_name_x and product_name_y
        if 'product_name_y' in single_item.columns:
            single_item['product_name'] = single_item['product_name_y'].fillna(single_item['product_name_x'])
            # Drop the temporary x and y columns so they don't mess up future steps
            single_item = single_item.drop(columns=['product_name_x', 'product_name_y'])
        else:
            single_item['product_name_x'] = single_item['product_name_y']

    # Rename back product_name for appending into list
    single_item = single_item.rename(columns={'product_name_x': 'product_name'})
    all_items.append(single_item)
    
all_items_list = pd.concat(all_items, ignore_index=True)

# Conditions for invalid input
# Condition 1: Item Name cannot match with product list
# Condition 2: Quantity was missing or ambiguous ("some", "few")
conditions = [
    (all_items_list['SKU'].isna()),       
    (all_items_list['quantity'].isna())   
]
choices = ['UNLISTED', 'AMBIGUOUS']

#If status is not UNLISTED and AMBIGUOUS, set the status as VALID
all_items_list['status'] = np.select(conditions, choices, default='VALID')

#Fill in NA data to 0
all_items_list['unit_price'] = all_items_list['unit_price'].fillna(0.00)
all_items_list['quantity_input'] = all_items_list['quantity'].fillna(0)

#Calculate the subtotal for each order item
all_items_list['subtotal'] = all_items_list['quantity_input'] * all_items_list['unit_price']

all_items_list = all_items_list.drop(columns=['match_key', 'match_name', 'match_sku'], errors='ignore')

print(all_items_list[['product_name', 'quantity', 'SKU', 'unit_price', 'subtotal', 'status']])