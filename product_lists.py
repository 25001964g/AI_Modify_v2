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
        1250, 1250, 1500, 1500,
        1250, 1250, 1800, 1800,
        2999, 2999, 3250, 3250,
        2500, 2500, 4500, 48.00,
        3500, 3500, 3800, 3800,
        2200, 2200, 1850, 1850,
        310, 310, 350, 350
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