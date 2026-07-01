"""
Test Case Type:
Single order item
1. Product Name: In list; Quantity: Provided
2. Product Name: In list; Quantity: Not Clear (a few, some e.t.c) /Not Provided
4. Product Name: Not Provided; Quantity: Provided
5. Product Name: Not in List; Quantity: Provided
6. Product Name: Not Provided; Quantity: Not Clear (a few, some e.t.c) /Not Provided
7. Product Name: Not in List; Quantity: Not Clear (a few, some e.t.c) /Not Provided

Multiple order item
1. Product Name: In list; Quantity: Provided
2. Product Name: In list; Quantity: Not Clear (a few, some e.t.c) /Not Provided
4. Product Name: Not Provided; Quantity: Provided
5. Product Name: Not in List; Quantity: Provided
6. Product Name: Not Provided; Quantity: Not Clear (a few, some e.t.c) /Not Provided
7. Product Name: Not in List; Quantity: Not Clear (a few, some e.t.c) /Not Provided

"""

mock_email = [
    #1
    """
    From: procurement@ABCcompany.com
    To: sales@XYZCompany.com
    Hi Sales Team,
    Please process an order. 
    We would like to order 90 jeans. 
    
    Thanks,
    Procurement Dept.
    """,
    #2
    """
    From: Alex@CloThcompany.com
    To: sales@XYZCompany.com
    Hi Sales Team,
    Could we order 100 T-shirt? Many thanks.
    
    Thanks,
    Alex
    """,
    #3
    """
    From: procurement@MENClothing.com
    To: sales@XYZCompany.com
    Hi Sales Team,
    We want to order 100 SKU1190. Many thanks.
    
    Thanks,
    Procurement Dept.
    """,
    #4
    """
    From: procurement@IdealClothing.com
    To: sales@XYZCompany.com
    Hi Sales Team,
    We want to order a few jeans. Many thanks.
    
    Thanks,
    Procurement Dept.
    """,
    #5
    """
    From: procurement@FGHcompany.com
    To: sales@XYZCompany.com
    Hi Sales Team,
    Please process an order. 
    We would like to order 50 shoes. 
    
    Thanks,
    Procurement Dept.
    """,
    #6
    """
    From: patrick.chan@REWLimited.com
    To: sales@XYZCompany.com
    Hi Sales Team,
    Please process an order. 
    We would like to order 120 Socks. 
    
    Thanks,
    Patrick
    """,
    #7
    """
    From: amychan@REWLimited.com
    To: sales@XYZCompany.com
    Hi Sales Team,
    Please process an order. 
    We would like to order 120 SKU1190 and 50 Jeans. 
    
    Thanks,
    Amy
    """
    ]
