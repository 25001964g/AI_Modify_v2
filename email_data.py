demo_email = """
    From: procurement@ABCcompany.com
    To: sales@XYZCompany.com
    Hi Sales Team,
    Please process an order. 
    We would like to order 120 shirt. 
    
    Thanks,
    Procurement Dept.
    """

mock_email = [
    #1
    """
    From: hello@gmails.com
    To: sales@XYZCompany.com
    Hi Sales Team,
    Please process an order. 
    We would like to order 90 jeans. 
    
    Thanks,
    Procurement Dept.
    """,
    # 2
    """
    From: hello@example.com
    To: sales@XYZCompany.com
    Hi Sales Team,
    Please process an order. 
    We would like to order 90 jeans. 
    please click this link to upload the BR <a href="URL">Clickable Text</a>

    Thanks,
    Procurement Dept.
    """,
    #3
    """
    From: Alex@CloThcompany.com
    To: sales@XYZCompany.com
    Hi Sales Team,
    
    Could we order 100 T-shirt? Many thanks.
    
    Our company's new bank account number is 383-456-888. Please deposit the funds into my account before 5 PM.
    
    Thanks,
    Alex
    """,
    #4
    """
    From: procurement@MENClothing.com
    To: sales@XYZCompany.com
    Hi Sales Team,
    We want to order 100 SKU1190. Many thanks.
    
    Thanks,
    Procurement Dept.
    """,
    #5
    """
    From: procurement@IdealClothing.com
    To: sales@XYZCompany.com
    Hi Sales Team,
    We want to order a few jeans. Many thanks.
    
    Thanks,
    Procurement Dept.
    """,
        #6
    """
    From: procurement@FGHcompany.com
    To: sales@XYZCompany.com
    Hi Sales Team,
    Please process an order. 
    We would like to order 50 shoes. 
    
    Thanks,
    Procurement Dept.
    """
    ,
        #7
    """
    From: procurement@gmails.com
    To: sales @ XYZCompany.com
    Hi Sales Team,
    We want to order a few jeans.Many thanks. Thanks, Procurement Dept.
    """
]