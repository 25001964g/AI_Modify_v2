import pandas as pd

product_list = pd.DataFrame({
    'product_name': [
        'Classic Chicken Cup Noodle', 
        'Spicy Beef Cup Noodle', 
        'Seafood Medley Cup Noodle', 
        'Shrimp Flavor Cup Noodle',
        'Tonkotsu Pork Cup Noodle', 
        'Vegetable Garden Cup Noodle', 
        'Curry Flavor Cup Noodle', 
        'Kimchi Spicy Cup Noodle'
    ],
    'sku': [
        'SKU1001', 'SKU1002', 'SKU1003', 'SKU1004',
        'SKU1005', 'SKU1006', 'SKU1007', 'SKU1008'
    ],
    'price': [
        150, 150, 175, 175,
        160, 145, 180, 165
    ],
    'stock': [
        50, 45, 30, 35,
        20, 25, 15, 40
    ]
})
