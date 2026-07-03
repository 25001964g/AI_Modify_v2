import pandas as pd
import numpy as np
import json
from order_extractor import item_extract

def order_validation (email, product_list):
    #Get the structured JSON string from your Ollama request response
    order_list = item_extract(email)
    try:
        #Load json formatted data to pandas dataframe
        extracted_data = json.loads(order_list)
        df = pd.DataFrame(extracted_data['items'])
    except (json.JSONDecodeError, KeyError, TypeError) as e:
        print(f"Error parsing JSON from email: {e}")
        # Return an empty DataFrame matching your schema if input fails
        return pd.DataFrame(columns=['product_name', 'quantity', 'sku', 'price', 'subtotal', 'status'])

    # Data Cleaning for matching
    df['match_key'] = df['product_name'].fillna('').astype(str).str.lower().str.strip()

    #Create matching table for product list by adding the matching key from product list
    product_lookup = product_list.copy()
    product_lookup['match_name'] = product_lookup['product_name'].astype(str).str.lower().str.strip()
    product_lookup['match_sku'] = product_lookup['sku'].astype(str).str.lower().str.strip()


    is_sku_mask = df['match_key'].str.startswith('sku', na=False)
    df_sku = df[is_sku_mask].copy()
    df_name = df[~is_sku_mask].copy()

    # Match names
    matched_name = pd.merge(df_name, product_lookup, left_on='match_key', right_on = 'match_name', how='left', suffixes=('', '_nameDummy'))
    
    # Match SKUs
    matched_sku = pd.merge(df_sku, product_lookup, left_on='match_key', right_on = 'match_sku', how='left', suffixes=('_skuDummy', ''))

    # Combine both match tracks back together safely
    all_items_list = pd.concat([matched_name, matched_sku], ignore_index=True)

    # Handle na for numeric data
    all_items_list['price'] = all_items_list['price'].fillna(0.00)
    all_items_list['quantity'] = all_items_list['quantity'].fillna(0)

    # Conditions for invalid input
    # Condition 1: Item Name cannot match with product list
    # Condition 2: Quantity was missing or ambiguous ("some", "few")
    # Condition 3: Order Quantity exceed current stock
    conditions = [
        (all_items_list['sku'].isna()),       
        (all_items_list['quantity'].isna()),
        (all_items_list['quantity']>all_items_list['stock'])   
    ]
    status = ['unlisted', 'ambiguous', 'not enough stock']

    #If status is not unlisted and ambiguous, set the status as VALID, and remarks as None
    all_items_list['item_status'] = np.select(conditions,status, default='VALID')

    #Calculation
    all_items_list['subtotal'] = all_items_list['quantity'] * all_items_list['price']

    # Safely select final columns even if columns were slightly named differently
    validated_order_list = all_items_list[['product_name', 'quantity', 'sku', 'price', 'subtotal', 'status']]


    return validated_order_list