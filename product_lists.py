import pandas as pd

product_list = pd.DataFrame({
    'product_name': [
        'T-Shirt Black', 'T-Shirt Blue', 'Graphic T-Shirt White', 'Graphic T-Shirt Black',
        'VNeck Shirt White', 'VNeck Shirt Grey', 'Polo Shirt White', 'Polo Shirt Green',
        'Oversized Hoodie Black', 'Oversized Hoodie Grey', 'ZipUp Hoodie', 'ZipUp Hoodie Black',
        'Sweater Beige', 'Sweater Burgundy', 'Denim Jacket Blue', 'Bomber Jacket Black Orange',
        'SlimFit Jeans Blue', 'SlimFit Jeans Black', 'Cargo Pants', 'Cargo Pants',
        'Chino Shorts', 'Chino Shorts Tan', 'Athletic Shorts Black', 'Athletic Shorts Grey',
        'Crew Socks White', 'Crew Socks Black', 'Ankle Socks Blue', 'Ankle Socks White'
    ],
    'sku': [
        'SKU8821', 'SKU8822', 'SKU8823', 'SKU8824',
        'SKU8825', 'SKU8826', 'SKU8827', 'SKU8828',
        'SKU5510', 'SKU5511', 'SKU5512', 'SKU5513',
        'SKU5514', 'SKU5515', 'SKU2260', 'SKU2261',
        'SKU4402', 'SKU4403', 'SKU4404', 'SKU4405',
        'SKU3312', 'SKU3313', 'SKU3314', 'SKU3315',
        'SKU1190', 'SKU1191', 'SKU1192', 'SKU1193'
    ],
    'price': [
        12.50, 12.50, 15.00, 15.00,
        12.50, 12.50, 18.00, 18.00,
        29.99, 29.99, 32.50, 32.50,
        25.00, 25.00, 45.00, 48.00,
        35.00, 35.00, 38.00, 38.00,
        22.00, 22.00, 18.50, 18.50,
        3.10, 3.10, 3.50, 3.50
    ],
    'stock': [
        100, 100, 100, 100,
        100, 100, 100, 100,
        100, 100, 100, 100,
        100, 100, 100, 100,
        100, 100, 100, 100,
        100, 100, 100, 100,
        100, 100, 100, 100
    ]
})