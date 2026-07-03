"""
Test Case Type:
Single order item:
1. Product Name: In list; Quantity: Provided
2. Product Name: In list; Quantity: Not Clear (a few, some e.t.c) /Not Provided
4. Product Name: Not Provided; Quantity: Provided
5. Product Name: Not in List; Quantity: Provided
6. Product Name: Not Provided; Quantity: Not Clear (a few, some e.t.c) /Not Provided
7. Product Name: Not in List; Quantity: Not Clear (a few, some e.t.c) /Not Provided

 Multiple order item:
*(Note: To thoroughly test multiple items, the system must face scenarios where all items match, some items match, or nothing matches.)*

 Category A: All items share the same status
1. Product Name: In list; Quantity: Provided (All items)
2. Product Name: In list; Quantity: Not Clear (a few, some e.t.c) /Not Provided (All items)
3. Product Name: Partial In list; Quantity: Provided (All items)
4. Product Name: Partial In list; Quantity: Not Clear (a few, some e.t.c) /Not Provided (All items)
5. Product Name: Not in List; Quantity: Provided (All items)
6. Product Name: Not in List; Quantity: Not Clear (a few, some e.t.c) /Not Provided (All items)
7. Product Name: Not Provided; Quantity: Provided (All items)
8. Product Name: Not Provided; Quantity: Not Clear (a few, some e.t.c) /Not Provided (All items)

 Category B: Mixed item statuses (The "Partial/Mixed" Scenarios)
9. Product Name: Partial In list; Quantity: Partial Provided *(e.g., Item 1 is in list + qty provided; Item 2 is partial match + qty missing)*
10. Product Name: In list & Partial In list; Quantity: Provided
11. Product Name: In list & Not in List; Quantity: Provided
12. Product Name: In list & Not Provided; Quantity: Provided
13. Product Name: In list & Partial In list; Quantity: Not Clear (a few, some e.t.c) /Not Provided
14. Product Name: In list & Not in List; Quantity: Not Clear (a few, some e.t.c) /Not Provided
15. Product Name: In list & Not Provided; Quantity: Not Clear (a few, some e.t.c) /Not Provided
16. Product Name: Partial In list & Not in List; Quantity: Provided
17. Product Name: Partial In list & Not Provided; Quantity: Provided
18. Product Name: Partial In list & Not in List; Quantity: Not Clear (a few, some e.t.c) /Not Provided
19. Product Name: Partial In list & Not Provided; Quantity: Not Clear (a few, some e.t.c) /Not Provided
20. Product Name: Not in List & Not Provided; Quantity: Provided
21. Product Name: Not in List & Not Provided; Quantity: Not Clear (a few, some e.t.c) /Not Provided

"""

mock_email = [
    #1
    """
    From: procurement@ABCcompany.com
    To: sales@XYZCompany.com
    Hi Sales Team,
    Please process an order. 
    We would like to order 5 Classic Chicken Cup Noodle. 
    
    Thanks,
    Procurement Dept.
    """,
    #2
    """
    From: Alex@Retailcompany.com
    To: sales@XYZCompany.com
    Hi Sales Team,
    Could we order 100 Cup noodle? Many thanks.
    
    Thanks,
    Alex
    """,
    #3
    """
    From: procurement@MENRetailing.com
    To: sales@XYZCompany.com
    Hi Sales Team,
    We want to order 10 SKU1002. Many thanks.
    
    Thanks,
    Procurement Dept.
    """,
    #4
    """
    From: procurement@Idealshop.com
    To: sales@XYZCompany.com
    Hi Sales Team,
    We want to order a few Curry Flavor Cup Noodle. Many thanks.
    
    Thanks,
    Procurement Dept.
    """,
    #5
    """
    From: procurement@FGHcompany.com
    To: sales@XYZCompany.com
    Hi Sales Team,
    Please process an order. 
    We would like to order 5 box of Tomato Cup noodle. 
    
    Thanks,
    Procurement Dept.
    """,
    #6
    """
    From: patrick.chan@REWLimited.com
    To: sales@XYZCompany.com
    Hi Sales Team,
    Please process an order. 
    We would like to order 20 Curry Flavor Cup Noodle. 
    
    Thanks,
    Patrick
    """,
    #7
    """
    From: amychan@WelcomeRetail.com
    To: sales@XYZCompany.com
    Hi Sales Team,
    Please process an order. 
    We would like to order 12 SKU1001 and 5 Shrimp Flavor Cup Noodle. 
    
    Thanks,
    Amy
    """
    ]
