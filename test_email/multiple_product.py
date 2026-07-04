# Multiple order item test cases
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