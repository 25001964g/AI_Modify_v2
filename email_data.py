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
test_email_1_1 = [
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
    """
]

# Single order item test cases split 1 (10)
test_email_1_2 = [
    # 10. In list; quantity equals boundary (100)
    """
    From: purchasing@valuechoiceglobal.com
    To: sales@XYZCompany.com
    Subject: Exact Campaign Allocation

    Hello Sales Team,

    Please process an order for 100 Tonkotsu Pork Cup Noodle for our annual customer reward campaign. The figure is exactly aligned to the planned giveaway packs and has been approved by both sales and finance. We need this quantity delivered to our main DC under normal terms.

    Kindly acknowledge receipt of this request and provide your estimated dispatch schedule. If any lead-time issue appears, please inform us today so we can update our campaign communication.

    Best regards,
    Mandy Fok
    Procurement Manager
    """,
    # 11. Partial in list; quantity provided
    """
    From: replenishment@primebuyhk.com
    To: sales@XYZCompany.com
    Subject: Flavor Confirmation Needed

    Dear Team,

    We would like to order 22 Shrimp Cup Noodle for our neighborhood store program. Quantity is fixed and already approved, but our team shortened the item description in the internal form. Please confirm the exact matching product name in your catalog before dispatch to avoid receiving mismatch.

    Once you confirm the closest valid item, we will issue the final PO number in the same thread and keep the requested quantity unchanged.

    Thanks in advance,
    Rachel Tam
    Purchasing Coordinator
    """,
    # 12. Partial in list; quantity unclear or not provided
    """
    From: demand@freshlinegroup.com
    To: sales@XYZCompany.com
    Subject: Preliminary Refill for Kimchi Line

    Hi Sales Team,

    Our stores are asking for more Kimchi Cup Noodle soon, but we have not finalized the shipment quantity. Please reserve some stock temporarily while our branch count is being consolidated. The item name in our request is shortened from your catalog wording, so we may need your confirmation on the exact matching product.

    Kindly reply with available quantity and lead time. We will send final numbers after internal sign-off later today.

    Regards,
    Louis Cheng
    Demand Planner
    """,
    # 13. In list; quantity provided; conflicting SKU
    """
    From: purchasing@orbittrading.hk
    To: sales@XYZCompany.com
    Subject: PO with Item/SKU Check

    Dear Sales Team,

    Please arrange 16 Curry Flavor Cup Noodle for our central warehouse. In our ERP line, the SKU appears as SKU1002 due to a template copy from a previous order. Kindly follow the product name requested in this email and flag any mismatch according to your standard validation process.

    We need confirmation today because transport booking closes at 4 PM. Please reply with the accepted item code and expected delivery date.

    Best,
    Hannah Chiu
    Procurement Executive
    """,
    # 14. In list duplicate name in DB; quantity provided; SKU not provided
    """
    From: buyer@westshoremarkets.com
    To: sales@XYZCompany.com
    Subject: Catalog Name Clarification

    Hello Team,

    We need 28 Classic Chicken Cup Noodle for next week's floor-stack display. Our master data team mentioned there may be two internal records carrying a similar Classic Chicken naming convention, but we are not submitting SKU in this request. Please process with your standard item-matching rules and confirm which exact record you will ship.

    Quantity is final and delivery should follow normal route to our Yuen Long warehouse. Please send confirmation by end of day.

    Regards,
    Derek Lui
    Category Procurement
    """,
    # 15. In list duplicate name in DB; quantity provided; SKU provided
    """
    From: sourcing@finedealretail.com
    To: sales@XYZCompany.com
    Subject: Name Duplication Control

    Dear Sales Colleagues,

    Please process 26 Classic Chicken Cup Noodle with SKU1001 for our monthly replenishment. We understand the product name can appear in more than one internal naming variant, so we are including SKU here to lock the intended item. Quantity and shipping address are both confirmed.

    Kindly acknowledge that SKU1001 will be used as the primary reference on packing documents and invoice lines. We appreciate your quick confirmation to proceed.

    Best regards,
    Joanne Kwok
    Senior Buyer
    """,
    # 16. In list; invalid quantity (0 / negative / decimal)
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
    """,
    # 17. Not in list; over-stock style number
    """
    From: category.team@marketpulsehk.com
    To: sales@XYZCompany.com
    Subject: High Volume New Item Inquiry

    Dear Team,

    For a summer roadshow, we would like to buy 180 Truffle Mushroom Cup Noodle units if your production supports this quantity. The volume is tied to event commitments already shared with partners, so we need an early feasibility response.

    Please confirm whether this item is in your current catalog and whether the requested amount is realistic for one shipment. If not available, propose a close substitute and possible maximum quantity.

    Regards,
    Brian Yu
    Event Procurement
    """,
    # 18. In list; quantity provided; request double if stock available
    """
    From: purchasing@metrohubstores.com
    To: sales@XYZCompany.com
    Subject: Flexible Quantity Request

    Dear Sales Team,

    Please schedule 20 Kimchi Spicy Cup Noodle for our baseline replenishment this week. If your stock position allows, we would like to double the quantity to 40 in the same shipment to support an unplanned weekend display. If doubling is not possible, please at least secure the original 20 units.

    Kindly confirm what quantity can be committed today and share your earliest dispatch timing so we can finalize store communication.

    Best,
    Stanley Fung
    Procurement Supervisor
    """,
    # 19. In list; quantity provided; request double causes over stock
    """
    From: replenishment@urbanselectgroup.com
    To: sales@XYZCompany.com
    Subject: Conditional Expansion Order

    Hello Sales Team,

    We are placing an initial order for 60 Curry Flavor Cup Noodle for our city outlets. If inventory is strong, please increase this order to double quantity, meaning 120 units total. This additional amount would support a short-term promotion requested by store operations.

    Please confirm feasible quantity based on available stock and advise whether split delivery is required. We need your response by noon to finalize route planning.

    Regards,
    Felicia Mak
    Demand Replenishment
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
    """
]


# Multiple order item test cases - Category B - split 1 (9)
test_email_3_1 = [
    # 1. Partial in list; partial quantity provided
    """
    From: buyteam@sunmarkethk.com
    To: sales@XYZCompany.com
    Subject: Mixed Completeness Order

    Dear Sales Team,

    Please process 20 Classic Chicken Cup Noodle as a confirmed line for our next shipment. We also need Shrimp Cup Noodle, but quantity for that second line is still pending because two stores have not submitted final demand. The second item name is abbreviated in our form and may require your catalog mapping.

    Kindly confirm available stock for both lines and hold inventory where possible. We will send the missing quantity shortly.

    Best regards,
    Adam Lo
    Purchasing Team
    """,
    # 2. In list and partial in list; quantity provided
    """
    From: sourcing@brightlanegroup.com
    To: sales@XYZCompany.com
    Subject: Confirmed Mixed Name Order

    Hello Team,

    Please arrange 17 Seafood Medley Cup Noodle and 13 Curry Cup Noodle for our central warehouse. Both quantities are confirmed, while the second item uses a shortened name from our internal system. Please map it to your exact catalog record before shipping.

    We would appreciate confirmation with final item names and expected dispatch date today, as transport booking closes this afternoon.

    Regards,
    Bonnie Ho
    Strategic Sourcing
    """,
    # 3. In list and not in list; quantity provided
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
    # 4. In list and not provided; quantity provided
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
    # 5. In list and partial in list; quantity unclear or not provided
    """
    From: procurement.ops@citylinefoods.com
    To: sales@XYZCompany.com
    Subject: Pending Quantity Confirmation

    Dear Team,

    We need additional Tonkotsu Pork Cup Noodle and Shrimp Cup Noodle for the next replenishment run. At this moment, final quantities are still being reviewed by branch managers, and the second item name is abbreviated in our request.

    Please reserve some stock for both lines and confirm your current availability. Once we receive the final store numbers, we will return with exact quantities and PO reference.

    Best regards,
    Edwin Chu
    Procurement Operations
    """,
    # 6. In list and not in list; quantity unclear or not provided
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
    # 7. In list and not provided; quantity unclear or not provided
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
    """,
    # 8. Partial in list and not in list; quantity provided
    """
    From: sourcing@marketgateasia.com
    To: sales@XYZCompany.com
    Subject: Confirmed Mixed Validation Lines

    Hi Team,

    Please process 14 Chicken Cup Noodle and 10 Truffle Cream Cup Noodle for our test launch. Quantities are final. The first line uses a shortened product name that should map to your existing catalog, while the second line may be outside your standard assortment.

    Kindly confirm accepted items and advise any substitutions needed so we can issue the final PO number this afternoon.

    Best,
    Ivy Chee
    Strategic Buyer
    """,
    # 9. Partial in list and not provided; quantity provided
    """
    From: purchasing@starretailnetwork.com
    To: sales@XYZCompany.com
    Subject: Two-Line Order with Missing Item

    Dear Sales Team,

    Please arrange 12 Kimchi Cup Noodle for line one. For line two, quantity 8 is confirmed but product name is currently blank due to a template issue from our ERP export. Both quantities are approved and intended for the same delivery route.

    Please confirm the first mapped item and advise what data is required to complete line two so we can finalize documentation quickly.

    Regards,
    Leo Chan
    Purchasing Executive
    """
]


# Multiple order item test cases - Category B - split 2 (10)
test_email_3_2 = [
    # 10. Partial in list and not in list; quantity unclear or not provided
    """
    From: demand@coremartgroup.com
    To: sales@XYZCompany.com
    Subject: Preliminary Mixed Product Inquiry

    Hello,

    We are considering Pork Cup Noodle and Lobster Bisque Cup Noodle for a short-term campaign. Final quantities are not confirmed yet, and the first item name in our note is abbreviated from your official catalog. Please help us check availability and hold stock where possible.

    If the second product is not listed, kindly propose a close substitute that can ship this week. We will confirm exact quantities after internal approval.

    Sincerely,
    Pauline Tse
    Demand Planning
    """,
    # 11. Partial in list and not provided; quantity unclear or not provided
    """
    From: ordercontrol@harborpointretail.com
    To: sales@XYZCompany.com
    Subject: Incomplete Item and Quantity Details

    Dear Team,

    We may need additional Shrimp Cup Noodle and one more noodle line for our branch refill plan. At present, the second product name is missing from our document, and both line quantities are still pending manager confirmation.

    Please send your current stock view for the identifiable item and indicate the latest timing for quantity confirmation. We will complete missing fields as soon as the regional reports arrive.

    Best regards,
    Cindy Poon
    Order Control
    """,
    # 12. Not in list and not provided; quantity provided
    """
    From: categorybuy@novaretail.hk
    To: sales@XYZCompany.com
    Subject: Trial Line Plus Missing Product

    Dear Sales Team,

    Please arrange two lines for a trial shipment: 9 Black Garlic Cup Noodle and a second line with quantity 7 where product name is currently unavailable in our request form. Quantities are fixed and approved by our pilot-store team.

    Kindly confirm whether the named product is part of your assortment and advise how we should complete the missing line to proceed. We prefer dispatch within this week if possible.

    Regards,
    Samuel Hui
    Category Buyer
    """,
    # 13. Not in list and not provided; quantity unclear or not provided
    """
    From: planning@easthavenstores.com
    To: sales@XYZCompany.com
    Subject: Early Stage Product Inquiry

    Hi Sales Team,

    Our team is exploring a new noodle line, Truffle Corn Cup Noodle, and another yet-to-be-specified item for a potential promotion. We do not have final quantities for either line at this moment because store enrollment is still open.

    Please advise if the named item is available and what comparable products you can suggest. We will return with complete item details and quantities after internal review.

    Thank you,
    Maggie Lai
    Planning Department
    """,
    # 14. In list and in list by SKU; quantity provided
    """
    From: buyerdesk@freshworldgroup.com
    To: sales@XYZCompany.com
    Subject: Name and SKU Combined Order

    Dear Team,

    Please process 18 Curry Flavor Cup Noodle and 14 units of SKU1003 for this week's replenishment. Both quantities are confirmed and should ship together to our Tsing Yi facility. We intentionally used product name on one line and SKU on the other to match our internal workflow.

    Kindly confirm stock availability for both references and share expected dispatch date so we can lock transport allocation.

    Best,
    Derek Yau
    Buyer Desk
    """,
    # 15. In list and in list by SKU; quantity unclear or not provided
    """
    From: procurement@marketbridgehk.com
    To: sales@XYZCompany.com
    Subject: Flexible Two-Line Reservation

    Hello Sales Team,

    We are preparing a replenishment for Shrimp Flavor Cup Noodle and SKU1008. Final quantities are still being confirmed by operations, so please reserve some stock for both lines while we complete demand validation.

    Please share your current available quantities and cut-off time for this dispatch cycle. We will provide exact numbers as soon as branch approvals are completed.

    For internal tracking, please also indicate whether partial shipment by line is allowed under your current logistics policy.

    Regards,
    Fiona Yik
    Procurement Specialist
    """,
    # 16. In list and over stock item; quantity provided
    """
    From: promo.buying@maxwayretail.com
    To: sales@XYZCompany.com
    Subject: Standard Plus High-Volume Mix

    Dear Sales Team,

    Please arrange 20 Vegetable Garden Cup Noodle and 125 Classic Chicken Cup Noodle for our upcoming promotional cycle. Both quantities are confirmed in our campaign brief. The first line is routine replenishment, while the second reflects a high-volume event requirement.

    Kindly confirm what can be fulfilled immediately and whether split shipment is possible for any shortfall. We need your reply today to finalize in-store communication.

    Sincerely,
    Veronica Ma
    Promo Buying
    """,
    # 17. In list by SKU and not in list; quantity provided
    """
    From: purchasing@urbanbasketchain.com
    To: sales@XYZCompany.com
    Subject: SKU Plus Trial Flavor Order

    Dear Team,

    Please process 21 units of SKU1002 and 10 Truffle Mushroom Cup Noodle for our mixed replenishment and trial program. Quantities are finalized and approved. The SKU line should map directly to your listed product, while the second line may require availability confirmation.

    Please advise if the trial flavor can be supplied and suggest a substitute if not. We would like shipment to depart by Friday.

    Best regards,
    Connie Law
    Purchasing Department
    """,
    # 18. In list by SKU and not provided; quantity provided
    """
    From: central.order@lakeviewretail.com
    To: sales@XYZCompany.com
    Subject: One SKU Line and One Missing Product

    Hi Sales Team,

    Please arrange 24 units of SKU1007. Also, range 6 units for the product purchased last time. Both lines belong to the same replenishment batch and should be shipped together if possible.

    Kindly confirm the SKU line and advise what additional information is needed for the unnamed line so we can submit a corrected PO immediately.

    Regards,
    Tammy Koo
    Central Order Team
    """,
    # 19. In list plus conflicting SKU items; quantity provided
    """
    From: sourcing@primecirclefoods.com
    To: sales@XYZCompany.com
    Subject: Conflict Check for Two Lines

    Dear Sales Team,

    Please process these confirmed lines: 13 Seafood Medley Cup Noodle labeled with SKU1001, and 11 Classic Chicken Cup Noodle labeled with SKU1003. Quantities are approved, but our template appears to contain cross-assigned SKU codes from a prior sheet.

    Kindly validate each line using your standard controls and confirm which item-SKU pair will be accepted for fulfillment. We need corrected confirmation for finance posting today.

    Thank you,
    Marco Leung
    Sourcing Manager
    """
]

# Additional validation focused combinations (8)
test_email_4 = [
    # 1. Same company with different sender local parts
    """
    From: amy@ABCcompany.com
    To: sales@XYZCompany.com
    Subject: Monthly Replenishment from ABCcompany

    Dear Sales Team,

    This is Amy from ABCcompany central procurement. Please arrange 18 Shrimp Flavor Cup Noodle for our monthly restock to warehouse A. Our colleague from procurement@ABCcompany.com usually handles this account, but I am covering this cycle while she is on leave.

    Please keep the same billing profile and delivery address used in our previous confirmed orders. Kindly reply with stock confirmation and expected shipment date.

    Best regards,
    Amy Chow
    ABCcompany Procurement
    """,
    # 2. Mixed case domain name
    """
    From: Alex@CloThcompany.com
    To: sales@XYZCompany.com
    Subject: Restock Request for Retail Floor Reset

    Hello Sales Team,

    We are preparing a floor reset this weekend and need 20 Tonkotsu Pork Cup Noodle for our flagship store. Quantity is confirmed by operations and should be delivered under our regular credit terms. Please include SKU and item name on the packing list for receiving speed.

    Kindly confirm availability and earliest dispatch time. If there is any shortage, please share the maximum shippable quantity so we can adjust display plans.

    Regards,
    Alex Wong
    Clothcompany Buying Office
    """,
    # 3. Subdomain address
    """
    From: buyer@apac.ABCcompany.com
    To: sales@XYZCompany.com
    Subject: APAC Warehouse Replenishment

    Dear Sales Colleagues,

    Please process a confirmed order for 22 Classic Chicken Cup Noodle and 14 units of SKU1008 for our APAC distribution center. Both quantities are approved and should be dispatched together this week. We are using our regional subdomain mailbox for this transaction due to routing updates.

    Kindly provide stock confirmation, ship date, and total amount so our finance team can pre-approve payment release.

    Best regards,
    Jason P.
    APAC Procurement
    """,
    # 4. Signature name uses domain name company while sender is procurement@ABCcompany.com
    """
    From: procurement@ABCcompany.com
    To: sales@XYZCompany.com
    Subject: Standard Restock Request

    Dear Sales Team,

    Please arrange 16 Seafood Medley Cup Noodle for our routine replenishment this week. Quantity and destination are confirmed according to our standing plan. We would appreciate dispatch by Thursday so store backrooms can receive before weekend traffic.

    Kindly send your order confirmation with invoice estimate and lead time. If any adjustment is needed, please call our office before noon.

    This message should be treated as an official request from our company mailbox and matched to our standard customer profile.

    Thank you,
    Domain Name Procurement
    """,
    # 5. Price/subtotal check with decimal price
    """
    From: purchasing@retailpilot.com
    To: sales@XYZCompany.com
    Subject: Decimal Price Validation Order

    Dear Team,

    Please process 10 Seafood Medley Cup Noodle for our test order. In our draft PO, unit price is entered as 175.50 for internal validation of decimal handling, and expected subtotal is listed as 1755.00 before tax. Quantity is confirmed and shipment can follow standard terms.

    Kindly confirm your accepted unit price and line subtotal format in the confirmation document, as our finance team is testing decimal parsing in the new intake workflow.

    Regards,
    Felix Kan
    Procurement Systems User
    """,
    # 6. Total check: integer + decimal unit price in multi-item order
    """
    From: ops.buying@quantummart.com
    To: sales@XYZCompany.com
    Subject: Multi-Line Total Verification

    Dear Sales Team,

    Please arrange 8 Classic Chicken Cup Noodle at 150 each and 6 Shrimp Flavor Cup Noodle at 175.25 each for our system validation purchase. Our expected pre-tax total is 1951.50, and quantities are fully approved. This order is intended to verify total calculations across integer and decimal unit prices.

    Please confirm line subtotals and grand total in your reply, together with shipment date and invoice reference format.

    Best,
    Natalie Fung
    Operations Buying
    """
]

test_email_pending = [    
    # 7. Translation scenario
    """
    From: takahashi@globalretail.jp
    To: sales@XYZCompany.com
    Subject: 日本語での発注依頼

    XYZCompany 営業ご担当者様

    いつもお世話になっております。Global Retail Procurement の高橋です。
    東京エリアの小売向け在庫補充として、カレーフレーバーのカップヌードルを12個発注いたします。
    在庫に問題がなければ、来週水曜日までに弊社保税倉庫へ納品いただけますでしょうか。

    今回は日本側販促日程に合わせた手配のため、納期確約を優先して確認したく存じます。
    数量は12で確定しており、変更予定はありません。
    可能であれば、出荷予定日、請求書番号の記載形式、ならびに確定金額をご返信ください。

    社内経理処理の都合上、返信時には数量・納品予定日・明細金額を明記いただけると助かります。
    何卒よろしくお願いいたします。

    敬具
    高橋 由紀
    Global Retail Procurement
    """
    ,
    # 8. Translation scenario
    """
    From: chen.lihua@easternretail.cn
    To: sales@XYZCompany.com
    Subject: 中文订单请求

    XYZCompany 销售团队您好：

    我是 Eastern Retail 采购部的陈丽华。为了下周门店补货，请为我们安排采购 15 箱海鲜风味杯面。
    该数量已经由营运团队确认，如库存充足，请于下周二前送达我司深圳仓库。

    另外，请在回复中确认预计出货日期、单价、订单小计以及含税总金额，方便我们完成内部审批。
    如果当前库存不足，也请告知可供应数量以及最早补货时间。

    感谢配合，期待您的确认回复。

    此致
    敬礼
    陈丽华
    Eastern Retail 采购部
    """]
