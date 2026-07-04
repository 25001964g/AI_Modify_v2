# Single order item test cases
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