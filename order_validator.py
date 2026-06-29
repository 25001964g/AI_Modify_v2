import pandas as pd
import numpy as np
import json
from order_extractor import item_extract

def order_validation (email, product_list):
    #Get the structured JSON string from your Ollama request response
    # (Simulated raw response string from your prompt above)
    order_list = item_extract(email)

    #Load json formatted data to pandas dataframe
    extracted_data = json.loads(order_list)
    df = pd.DataFrame(extracted_data['items'])

    # Data Cleaning for matching
    df['match_key'] = df['product_name'].str.lower().str.strip()

    product_list['match_name'] = product_list['product_name'].str.lower().str.strip()
    product_list['match_sku'] = product_list['sku'].str.lower().str.strip()

    all_items = []

    for row in df.iterrows():
        item_row = pd.DataFrame([row])

        #If customer provide product name:
        is_sku = row['match_key'].startswith('sku')

        if is_sku == False:
            # Match using product name
            single_item = pd.merge(item_row, product_list, left_on='match_key', right_on='match_name', how='left')
        else:
            # Match using sku code
            single_item = pd.merge(item_row, product_list, left_on='match_key', right_on='match_sku', how='left')
            # If using sku matched an inventory item, product_name will become product_name_x and product_name_y
            if 'product_name_y' in single_item.columns:
                single_item['product_name'] = single_item['product_name_y'].fillna(product_list['product_name'])
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
    # Condition 3: Order Quantity exceed current stock
    conditions = [
        (all_items_list['sku'].isna()),       
        (all_items_list['quantity'].isna()),
        (all_items_list['quantity']>all_items_list['stock'])   
    ]
    status = ['unlisted', 'ambiguous', 'not enough stock']
    remarks = ['Please double check and follow up the order item.', 'Please double check and follow up the actual quantity', 'Please follow up immediately for mitigation plan.']

    #If status is not unlisted and ambiguous, set the status as VALID, and remarks as None
    all_items_list['status'] = np.select(conditions,status, default='VALID')
    all_items_list['remarks'] = np.select(conditions, remarks, default = None)

    #Fill in NA data to 0
    all_items_list['unit_price'] = all_items_list['unit_price'].fillna(0.00)
    all_items_list['quantity_input'] = all_items_list['quantity'].fillna(0)

    #Calculate the subtotal for each order item
    all_items_list['subtotal'] = all_items_list['quantity_input'] * all_items_list['unit_price']

    #Cleaning up the dataframe
    all_items_list = all_items_list.drop(columns=['match_key', 'match_name', 'match_sku'], errors='ignore')

    validated_order_list = all_items_list[['product_name', 'quantity', 'sku', 'unit_price', 'subtotal', 'status']]
    return order_list, validated_order_list