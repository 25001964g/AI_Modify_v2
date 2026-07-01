#Harness: Format the output in a specific JSON format
single_json_structure = {
    "customer": "string",
    "items": [
        {
        "product_name": "string",
        "sku": "string or null",
        "quantity": 0.0,
        "unit_price": 0.0,
        "subtotal": 0.0,
        "status": "string"
        }
    ],
    "total": 0.0
}

multiple_json_structure = {
    "customer": "string",
    "items": [
        {
        "product_name": "item1",
        "sku": "string or null",
        "quantity": 0.0,
        "unit_price": 0.0,
        "subtotal": 0.0,
        "status": "string"
        },
        {
        "product_name": "item2",
        "sku": "string or null",
        "quantity": 0.0,
        "unit_price": 0.0,
        "subtotal": 0.0,
        "status": "string"
        }
    ],
    "total": 0.0
}