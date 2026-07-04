"""
Test Case Type:
Single order item:
1. Product Name: In list; Quantity: Provided
2. Product Name: In list; Quantity: Not Clear (a few, some e.t.c) /Not Provided
4. Product Name: Not Provided; Quantity: Provided
5. Product Name: Not in List; Quantity: Provided
6. Product Name: Not Provided; Quantity: Not Clear (a few, some e.t.c) /Not Provided
7. Product Name: Not in List; Quantity: Not Clear (a few, some e.t.c) /Not Provided
8. Product Name: In list by SKU; Quantity: Provided
9. Product Name: In list by SKU; Quantity: Not Clear (a few, some e.t.c) /Not Provided
10. Product Name: In list; Quantity: Over stock (more than 100)
11. Product Name: In list; Quantity: Equal to stock boundary (100)
12. Product Name: Partial In list; Quantity: Provided (e.g., "Polo Shirt" without color)
13. Product Name: Partial In list; Quantity: Not Clear (a few, some e.t.c) /Not Provided
14. Product Name: In list; Quantity: Provided; SKU: Conflicting with product name
15. Product Name: In list duplicate name in DB; Quantity: Provided; SKU: Not Provided
16. Product Name: In list duplicate name in DB; Quantity: Provided; SKU: Provided
17. Product Name: In list; Quantity: Invalid value (0 / negative / decimal)
18. Product Name: Not in List; Quantity: Over stock style number (still unlisted)
19. Product Name: In list; Quantity: Provided; Request double quantity if stock is available (e.g., "Please provide 50 if stock is available") 
20. Product Name: In list; Quantity: Provided; Request double quantity if stock is available (over stock in total) (e.g., "Please provide 60 if stock is available") 

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
9. Product Name: In list by SKU; Quantity: Provided (All items)
10. Product Name: In list; Quantity: Over stock (All items)

 Category B: Mixed item statuses (The "Partial/Mixed" Scenarios)
1. Product Name: Partial In list; Quantity: Partial Provided *(e.g., Item 1 is in list + qty provided; Item 2 is partial match + qty missing)*
2. Product Name: In list & Partial In list; Quantity: Provided
3. Product Name: In list & Not in List; Quantity: Provided
4. Product Name: In list & Not Provided; Quantity: Provided
5. Product Name: In list & Partial In list; Quantity: Not Clear (a few, some e.t.c) /Not Provided
6. Product Name: In list & Not in List; Quantity: Not Clear (a few, some e.t.c) /Not Provided
7. Product Name: In list & Not Provided; Quantity: Not Clear (a few, some e.t.c) /Not Provided
8. Product Name: Partial In list & Not in List; Quantity: Provided
9. Product Name: Partial In list & Not Provided; Quantity: Provided
10. Product Name: Partial In list & Not in List; Quantity: Not Clear (a few, some e.t.c) /Not Provided
11. Product Name: Partial In list & Not Provided; Quantity: Not Clear (a few, some e.t.c) /Not Provided
12. Product Name: Not in List & Not Provided; Quantity: Provided
13. Product Name: Not in List & Not Provided; Quantity: Not Clear (a few, some e.t.c) /Not Provided
14. Product Name: In list & In list by SKU; Quantity: Provided
15. Product Name: In list & In list by SKU; Quantity: Not Clear (a few, some e.t.c) /Not Provided
16. Product Name: In list & Over stock item; Quantity: Provided
17. Product Name: In list by SKU & Not in List; Quantity: Provided
18. Product Name: In list by SKU & Not Provided; Quantity: Provided
19. Product Name: In list + conflicting SKU items; Quantity: Provided

 Additional validation focused combinations:
1. Client Name Extraction: Same company with different sender local parts (e.g., procurement@ABCcompany.com, amy@ABCcompany.com)
2. Client Name Extraction: Mixed case domain name (e.g., Alex@CloThcompany.com)
3. Client Name Extraction: Subdomain address (e.g., buyer@apac.ABCcompany.com)
4. Client Name Extraction: using "DomainName company" as the signature name while sender email is procurement@ABCcompany.com
5. Price/Subtotal Check: Item with decimal price in product list
6. Total Check: Multi-item order with integer + decimal unit price
7. Translation: Email content in Japanese
8. Translation: Email content in Chinese 
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
    """,
    #８
    """
    From: yamamoto@ABCcompany.jp
    To: sales@XYZCompany.com
    営業部の皆様、

    いつもお世話になっております。
    商品の注文をお願いいたします。

    カップヌードル（エビ味）を3ケース注文させていただけますでしょうか。

    お手数をおかけしますが、ご対応のほどよろしくお願いいたします。

    以上、よろしくお願いいたします。
    山本
    
    """
    ]


# Single order item test cases split 1 (11)
test_email_1 = [
    # 1. In list; quantity provided
    """
    From: purchasing@northvaleretail.com
    To: sales@XYZCompany.com
    Subject: Weekly Restock Request

    Dear Sales Team,

    We are preparing next week's convenience-store promotion and need a confirmed replenishment. Please arrange 24 Classic Chicken Cup Noodle for our Kowloon warehouse. This quantity was approved by our category manager and matches the shelf reset plan. Kindly keep your standard export carton packing and include the item code in the commercial invoice for easier receiving.

    If stock is available, we would appreciate dispatch by Thursday afternoon. Please confirm availability, expected ship date, and final amount.

    Best regards,
    Martin Lee
    Procurement Officer
    """,
    # 2. In list; quantity unclear or not provided
    """
    From: buyer.team@harborchain.com
    To: sales@XYZCompany.com
    Subject: Urgent Cup Noodle Refill

    Hello Sales Team,

    Our branch supervisors reported fast movement on Spicy Beef Cup Noodle this week. Please send us some additional stock for immediate replenishment. We do not have a final carton count yet because two stores are still submitting their consumption numbers, but we need the shipment to leave as soon as practical.

    Please reserve inventory now and share your earliest delivery slot. Once the final internal count is approved, we will reply with a confirmed quantity in the same thread.

    Sincerely,
    Chloe Wong
    Purchasing Department
    """,
    # 3. Product not provided; quantity provided
    """
    From: ordering@sunrisefoodsupply.com
    To: sales@XYZCompany.com
    Subject: Standard Reorder Quantity

    Dear Team,

    Please process a reorder for 18 cases from your cup noodle range for our urban outlets. The quantity is confirmed and should be shipped under our regular account terms. Our merchandising team forgot to note the exact flavor in this request, but the quantity is fixed and approved by finance for this cycle.

    Kindly acknowledge this message and advise what product details you still require so we can complete the item confirmation quickly and avoid any shipping delay.

    Regards,
    Andrew Ho
    Supply Planning
    """,
    # 4. Not in list; quantity provided
    """
    From: procurement@greenbasketmart.com
    To: sales@XYZCompany.com
    Subject: New Flavor Trial Purchase

    Hi Sales Team,

    We would like to place a test order for 12 Tomato Basil Cup Noodle for selected premium stores. The quantity is small because this is a market trial tied to customer feedback cards. If this item is available, please quote lead time and confirm whether mixed-flavor pallets are allowed on your side.

    If the product is not part of your current catalog, kindly let us know the closest available alternative so our team can revise the launch memo today.

    Thank you,
    Irene Cheung
    Category Buyer
    """,
    # 5. Product not provided; quantity unclear or not provided
    """
    From: sourcing@metrochoicegroup.com
    To: sales@XYZCompany.com
    Subject: Follow-up Restock Request

    Dear Sales Colleagues,

    We need to replenish cup noodles for our weekend campaign and would like to place an order soon. At this stage, our team only knows we require a few extra cartons, but product details and exact quantity are still pending from regional managers. Please help us hold a small allocation so we can lock the order once internal approval is completed.

    Kindly reply with your current stock situation and cut-off time for next-day dispatch, so we can finalize the purchase request without missing the campaign window.

    Best,
    Peter Ng
    Purchasing Team
    """,
    # 6. Not in list; quantity unclear or not provided
    """
    From: demand.planning@dailycart.hk
    To: sales@XYZCompany.com
    Subject: Inquiry on Seasonal Noodle Variant

    Hello,

    Our product team is searching for Miso Corn Cup Noodle for a themed promotion and wants to buy some units if supply is possible. We do not have a confirmed quantity yet because store enrollment is still open, but we need an initial response for planning by tomorrow morning.

    Please advise whether this SKU exists in your assortment and, if unavailable, which similar item can be offered with comparable flavor profile and lead time.

    Regards,
    Vivian Lau
    Procurement Analyst
    """,
    # 7. In list by SKU; quantity provided
    """
    From: purchasing.ops@eastbridgefoods.com
    To: sales@XYZCompany.com
    Subject: PO Request by SKU

    Dear Sales Team,

    Please arrange 30 units of SKU1004 for our monthly replenishment cycle. The quantity and destination warehouse are confirmed, and this should be billed under contract EB-24-Q3 as usual. Our receiving team prefers carton labels with both SKU and English item name to reduce check-in time.

    Kindly send order confirmation with committed shipment date, plus any notice if your available stock differs from the requested amount.

    Thank you for your support.

    Best regards,
    Kelvin Chan
    Procurement Lead
    """,
    # 8. In list by SKU; quantity unclear or not provided
    """
    From: buyer@harvestnetwork.com
    To: sales@XYZCompany.com
    Subject: Tentative SKU Reservation

    Hi Team,

    We may need additional stock of SKU1006 for the coming holiday rush. The final number is still under review, but please reserve some quantity for us if possible so we do not run out at the end of the month. Branch managers are submitting revised forecasts tonight.

    Could you share current availability and your recommended allocation window? We will revert with an exact purchase quantity once internal checks are complete.

    Regards,
    Susan Yip
    Central Purchasing
    """,
    # 9. In list; over stock (>100)
    """
    From: procurement@citymaxretail.com
    To: sales@XYZCompany.com
    Subject: Large Volume Request

    Dear Sales Team,

    We are launching a chain-wide discount event and want to place an order for 130 Seafood Medley Cup Noodle for immediate delivery. This volume is tied to promotion mechanics already printed in our leaflet, so we hope to secure stock quickly.

    Please confirm whether full quantity can be shipped in one batch. If partial fulfillment is necessary, share the maximum available amount and the soonest date for the balance so our operations team can adjust shelf plans.

    Sincerely,
    Gary Poon
    Buyer, Dry Grocery
    """,
    # 10. In list; invalid quantity (0 / negative / decimal)
    """
    From: planning@dailyharvestgroup.com
    To: sales@XYZCompany.com
    Subject: Adjustment Request

    Hi Sales Team,

    We are updating a prior request and currently have 0 Vegetable Garden Cup Noodle listed in our draft line for this cycle. Please check whether this can remain in the order worksheet or should be removed before final confirmation. The quantity came from an automatic calculation after returns reconciliation.

    Please advise your required format for valid quantities so our team can correct and reissue the purchase request immediately.

    Thank you,
    Anita Lam
    Inventory Planning
    """
]

# Multiple order item test cases - Category A (10)
test_email_2 = [
    # 1. All in list; quantity provided
    """
    From: centralbuy@northgatecommerce.com
    To: sales@XYZCompany.com
    Subject: Multi-Item Replenishment Order

    Dear Sales Team,

    Please process the following confirmed order for next-week delivery: 14 Classic Chicken Cup Noodle, 12 Seafood Medley Cup Noodle, and 10 Vegetable Garden Cup Noodle. All quantities are approved and aligned with shelf-space planning at three pilot outlets.

    Kindly keep items in separate labeled cartons and include SKU references in the packing list for receiving accuracy. Please confirm stock and dispatch date today so our logistics partner can lock a truck slot.

    Best regards,
    Carol Sin
    Central Procurement
    """,
    # 2. All in list; quantity unclear or not provided
    """
    From: buyer.ops@sunplazaretail.com
    To: sales@XYZCompany.com
    Subject: Tentative Multi-Item Request

    Hello Team,

    We need restock support for Classic Chicken Cup Noodle, Curry Flavor Cup Noodle, and Kimchi Spicy Cup Noodle. At this stage, branch-level quantities are still being consolidated, so exact numbers are not ready. Please reserve some stock for all three items while we complete internal planning.

    Could you share current availability and your latest cut-off time for this week's shipment? We will revert with finalized quantities shortly after finance approval.

    Sincerely,
    Oscar Cheng
    Purchasing Operations
    """,
    # 3. All partial in list; quantity provided
    """
    From: orderdesk@harvestretailers.com
    To: sales@XYZCompany.com
    Subject: Partial Name Multi-Item Order

    Dear Sales Team,

    Please arrange this confirmed order for our convenience network: 15 Chicken Cup Noodle, 11 Seafood Cup Noodle, and 9 Kimchi Cup Noodle. Quantities are fixed and approved, but our internal document uses shortened item names.

    Kindly map each line to your exact catalog product before dispatch and show the final item names on the confirmation. Delivery is requested for Friday morning to our main distribution center.

    Thank you,
    Emily Kwan
    Procurement Coordinator
    """,
    # 4. All partial in list; quantity unclear or not provided
    """
    From: sourcing.team@cityretailhub.com
    To: sales@XYZCompany.com
    Subject: Preliminary Assortment Refill

    Hi Sales Team,

    We are planning to replenish Chicken Cup Noodle, Shrimp Cup Noodle, and Pork Cup Noodle for a regional promotion. The names in our request are abbreviated, and final quantities are still pending from area managers. Please reserve some stock under these item groups while we complete allocation.

    Please reply with available options and lead time by item so we can lock the official PO later today.

    Regards,
    Jason Hui
    Strategic Sourcing
    """,
    # 5. All not in list; quantity provided
    """
    From: procurement@nextwavefoods.com
    To: sales@XYZCompany.com
    Subject: New Range Purchase Inquiry

    Dear Team,

    We would like to place a confirmed trial order for three new flavors: 10 Truffle Cream Cup Noodle, 8 Corn Butter Cup Noodle, and 12 Pepper Crab Cup Noodle. Quantities are finalized for a limited in-store test in premium branches.

    Please confirm whether these items are available in your active catalog. If not, kindly suggest closest alternatives with equivalent pricing tier and expected lead time, so we can revise the plan quickly.

    Best,
    Monica Yuen
    Category Procurement
    """,
    # 6. All not in list; quantity unclear or not provided
    """
    From: planning@retailfrontier.com
    To: sales@XYZCompany.com
    Subject: Availability Check for New Flavors

    Hello Sales Team,

    Our merchandising unit is interested in Truffle Cream Cup Noodle, Miso Corn Cup Noodle, and Lobster Bisque Cup Noodle. We do not have confirmed quantities yet because store participation is still open, but we need an early indication of availability.

    Please let us know whether these products exist in your lineup, and if not, which comparable items can be supplied quickly for a pilot launch.

    Regards,
    Raymond Ip
    Demand Planning
    """,
    # 7. All product not provided; quantity provided
    """
    From: buyersupport@harborlinegroup.com
    To: sales@XYZCompany.com
    Subject: Quantity-Only Replenishment Lines

    Dear Sales Team,

    Please prepare three replenishment lines with confirmed quantities for this cycle: 20 cases for line one, 14 cases for line two, and 9 cases for line three. Our internal spreadsheet omitted product names during export, but the quantities are approved and should be reserved immediately.

    Kindly advise what minimum item details are needed to proceed and hold these quantity slots temporarily while we correct the product fields.

    Thank you,
    Tiffany Leung
    Purchasing Support
    """,
    # 8. All product not provided; quantity unclear or not provided
    """
    From: demand.coordination@greenlanehk.com
    To: sales@XYZCompany.com
    Subject: Pending Item Details for Restock

    Hi Team,

    We need to create several replenishment lines for our cup noodle category, but both product names and exact quantities are still pending from branch submissions. Please reserve a modest amount of stock capacity for us until final details are confirmed.

    Could you share your allocation policy and latest order cut-off time? Once internal consolidation is complete, we will send full item names and quantities immediately.

    Best regards,
    Gloria Pui
    Demand Coordination
    """,
    # 9. All in list by SKU; quantity provided
    """
    From: purchasing@riverstonefoods.com
    To: sales@XYZCompany.com
    Subject: SKU-Based Multi-Item PO

    Dear Sales Team,

    Please process the following confirmed order by SKU: 18 units of SKU1001, 16 units of SKU1005, and 12 units of SKU1008. All quantities have been approved by our replenishment committee and should be delivered to warehouse RS-02 this Friday.

    Kindly include SKU and product description on both invoice and packing list. Please confirm stock availability and planned dispatch timing to complete our internal booking.

    Sincerely,
    Howard Tsang
    Procurement Manager
    """,
    # 10. All in list; over stock
    """
    From: operations.buying@megastorechain.com
    To: sales@XYZCompany.com
    Subject: Large Multi-Item Campaign Order

    Dear Team,

    We are preparing a major promotion and request the following quantities: 120 Classic Chicken Cup Noodle, 140 Spicy Beef Cup Noodle, and 110 Shrimp Flavor Cup Noodle. These figures are tied to printed campaign materials and need urgent stock confirmation.

    Please advise how much can be supplied immediately, and whether split shipments are possible for any shortfall. We need your earliest response to align store activation plans.

    Regards,
    Winnie Ko
    Operations Buying
    """,
    # 11. In list and not in list; quantity provided
    """
    From: procurement@sunlighthub.com
    To: sales@XYZCompany.com
    Subject: Mixed Catalog Status Order

    Dear Sales Team,

    Please process 19 Vegetable Garden Cup Noodle and 11 Truffle Mushroom Cup Noodle for our upcoming shelf reset. Quantities for both lines are finalized. The first item should match your standard catalog, while the second is requested for a trial and may not be in your current list.

    Kindly confirm what can be shipped and suggest an alternative for any unavailable line so we can close the PO today.

    Sincerely,
    Patrick Man
    Category Procurement
    """,
    # 12. In list and not provided; quantity provided
    """
    From: demand.buying@retailsphere.com
    To: sales@XYZCompany.com
    Subject: One Missing Product Field

    Hi Sales Team,

    Please arrange 15 Kimchi Spicy Cup Noodle as the first confirmed line. We also require a second line with quantity 9, but the product name was left blank in our uploaded form due to a data-export issue. Both quantities are approved and should be considered for this week's shipment.

    Please advise how we should complete the missing product field and keep stock reserved meanwhile.

    Thanks,
    Cheryl Law
    Demand Buying
    """,
    # 13. In list and not in list; quantity unclear or not provided
    """
    From: buyers@highstreetgroup.com
    To: sales@XYZCompany.com
    Subject: Stock Reservation Request

    Hello Sales Team,

    We are planning to restock Spicy Beef Cup Noodle and also consider a new line, Black Garlic Cup Noodle, for premium stores. Exact quantities are not ready yet because our campaign scope is still under approval.

    Could you reserve some stock for the listed item and advise whether the new line exists in your assortment? Please also provide your recommended alternatives if the second product is unavailable.

    Regards,
    Nora Fung
    Buying Department
    """,
    # 14. In list and not provided; quantity unclear or not provided
    """
    From: replenishment@freshcityretail.com
    To: sales@XYZCompany.com
    Subject: Mixed Information Refill

    Dear Sales Colleagues,

    We intend to purchase Seafood Medley Cup Noodle plus one additional noodle line for weekend promotion. Product name for the second line was not captured in our planning sheet, and final quantities for both lines are still being consolidated.

    Please share current stock for Seafood Medley and advise your order cut-off timeline. We will provide the missing item and confirmed quantities once branch data is complete.

    Thank you,
    Keith Wong
    Replenishment Team
    """
]


