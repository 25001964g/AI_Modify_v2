test_email_4 = [
    # 1. All in list; quantity provided (Chinese)
    """
    发件人: supply@northgatecommerce.com
    收件人: sales@XYZCompany.com
    主题: 多品项补货订单

    亲爱的销售团队，

    请处理以下确认订单，安排下周交付：14箱经典鸡肉杯面，12箱海鲜什锦杯面，10箱蔬菜园杯面。所有数量已批准，并符合三家试点门店的货架规划。

    请将商品分开装箱并贴标签，在装箱单中包含SKU以便收货。请今天确认库存和发货日期，以便物流伙伴锁定卡车时段。

    此致，
    张伟
    中央采购
    """,
    # 2. All in list; quantity unclear (Chinese)
    """
    发件人: ops@sunplazaretail.com
    收件人: sales@XYZCompany.com
    主题: 暂定多品项请求

    销售团队您好，

    我们需要补货经典鸡肉杯面、咖喱风味杯面和泡菜辣味杯面。目前分店数量仍在汇总，暂时没有最终数字。请为这三种商品预留库存，等待内部计划完成。

    请分享当前库存情况和本周发货的截止时间。我们将在财务批准后尽快回复最终数量。

    谨上，
    王芳
    采购运营
    """,
    # 3. All partial in list; quantity provided (Chinese)
    """
    发件人: desk@harvestretailers.com
    收件人: sales@XYZCompany.com
    主题: 部分名称多品项订单

    亲爱的销售团队，

    请安排以下确认订单：15箱鸡肉杯面，11箱海鲜杯面，9箱泡菜杯面。数量已固定并批准，但我们的内部文件使用了缩写名称。

    请在发货前将每一行映射到您目录中的准确产品，并在确认单上显示最终名称。交货时间为周五上午至主配送中心。

    谢谢，
    刘强
    采购协调员
    """,
    # 4. All partial in list; quantity unclear (Chinese)
    """
    发件人: team@cityretailhub.com
    收件人: sales@XYZCompany.com
    主题: 初步补货请求

    销售团队您好，

    我们计划为区域促销补充鸡肉杯面、虾仁杯面和猪肉杯面。请求中的名称是缩写，最终数量仍在等待区域经理确认。请为这些商品预留库存，等待分配完成。

    请回复每个商品的可用选项和交货时间，以便我们今天锁定正式订单。

    此致，
    李杰
    战略采购
    """,
    # 5. All not in list; quantity provided (Chinese)
    """
    发件人: category@nextwavefoods.com
    收件人: sales@XYZCompany.com
    主题: 新口味采购询问

    亲爱的团队，

    我们希望试购三种新口味：10箱松露奶油杯面，8箱玉米黄油杯面，12箱胡椒蟹杯面。数量已确认，用于高端门店的限量测试。

    请确认这些商品是否在您目录中。如不可供货，请建议最接近的替代品及价格和交期，以便我们快速调整计划。

    谨上，
    陈丽
    品类采购
    """,
    # 6. All not in list; quantity unclear (Chinese)
    """
    发件人: planning@retailfrontier.com
    收件人: sales@XYZCompany.com
    主题: 新口味可用性检查

    销售团队您好，

    我们的商品部门对松露奶油杯面、味噌玉米杯面和龙虾浓汤杯面感兴趣。目前尚未确认数量，因为门店参与仍在进行，但我们需要尽早了解可用性。

    请告知这些产品是否在您产品线中，如果没有，请推荐可快速供应的类似产品用于试点上市。

    此致，
    赵强
    需求计划
    """,
    # 7. All product not provided; quantity provided (Chinese)
    """
    发件人: support@harborlinegroup.com
    收件人: sales@XYZCompany.com
    主题: 仅数量补货请求

    亲爱的销售团队，

    请准备三条补货线，数量已确认：第一条20箱，第二条14箱，第三条9箱。内部表格遗漏了产品名称，但数量已批准，应立即预留。

    请告知所需的最小产品信息，并在我们修正字段前暂时保留这些数量。

    谢谢，
    孙敏
    采购支持
    """,
    # 8. All product not provided; quantity unclear (Japanese)
    """
    差出人: coordination@greenlanehk.com
    宛先: sales@XYZCompany.com
    件名: 補充の未確定情報

    営業チーム各位

    カップヌードルカテゴリーの補充ラインを作成する必要がありますが、商品名と数量はまだ支店から提出されていません。最終的な詳細が確認されるまで、適度な在庫容量を確保してください。

    割当方針と最新の注文締切時間を共有いただけますか。内部統合が完了次第、商品名と数量を送付します。

    敬具
    田中美咲
    需要調整
    """,
    # 9. All in list by SKU; quantity provided (Japanese)
    """
    差出人: purchase@riverstonefoods.com
    宛先: sales@XYZCompany.com
    件名: SKUベースの複数商品注文

    営業チーム各位

    次の確認済み注文をSKUで処理してください: SKU1001を18ユニット（クラシックチキンカップヌードル）、SKU1005を16ユニット（豚骨カップヌードル）、SKU1008を12ユニット（キムチスパイシーカップヌードル）。数量は補充委員会に承認され、金曜日にRS-02倉庫へ納品されるべきです。

    請求書と梱包リストにSKUと商品説明を含めてください。在庫状況と出荷予定を確認いただき、内部予約を完了させてください。

    敬具
    松本健
    調達マネージャー
    """,
    # 10. All in list; over stock (Japanese)
    """
    差出人: ops@megastorechain.com
    宛先: sales@XYZCompany.com
    件名: 大規模キャンペーン注文

    営業チーム各位

    大規模プロモーションを準備しており、次の数量を依頼します: クラシックチキンカップヌードル120個、スパイシービーフカップヌードル140個、シュリンプフレーバーカップヌードル110個。これらの数値は印刷済みのキャンペーン資料に基づいているため、緊急の在庫確認が必要です。

    即時供給可能な数量と、不足分に対する分割出荷の可否をお知らせください。店舗活性化計画を調整するため、迅速な回答をお願いします。

    敬具
    伊藤真由
    オペレーション購買
    """,
    # 11. In list and not in list; quantity provided (Japanese)
    """
    差出人: procurement@sunlighthub.com
    宛先: sales@XYZCompany.com
    件名: 混在カタログ注文

    営業チーム各位

    ベジタブルガーデンカップヌードルを19ユニット、トリュフマッシュルームカップヌードルを11ユニット発注します。数量は確定済みです。最初の商品は標準カタログに含まれていますが、2つ目は試験的に依頼しており、現在のリストにない可能性があります。

    出荷可能な商品を確認し、利用できない場合は代替品を提案してください。

    敬具
    山口翔
    カテゴリー調達
    """
     # 12. In list and not provided; quantity provided (Japanese)
    """
    差出人: demand@retailsphere.com
    宛先: sales@XYZCompany.com
    件名: 商品フィールド欠落

    営業チーム各位

    まずキムチスパイシーカップヌードルを15ユニット手配してください。さらに数量9のラインが必要ですが、商品名がデータエクスポートの不具合で欠落しました。両方の数量は承認済みで、今週の出荷に含めるべきです。

    欠落した商品フィールドをどのように補完すべきかご指示ください。その間、在庫を確保していただければ幸いです。

    敬具
    木村真紀
    需要購買
    """,
    # 13. In list and not in list; quantity unclear (Japanese)
    """
    差出人: buyers@highstreetgroup.com
    宛先: sales@XYZCompany.com
    件名: 在庫予約依頼

    営業チーム各位

    スパイシービーフカップヌードルの補充を計画しており、さらに新しいライン「ブラックガーリックカップヌードル」を検討しています。数量はまだ確定していません。キャンペーン範囲が承認待ちだからです。

    記載された商品の在庫を予約し、新しいラインが御社の品揃えに存在するかどうか確認してください。もし利用できない場合は、推奨される代替品を教えてください。

    敬具
    長谷川優子
    購買部
    """,
    # 14. In list and not provided; quantity unclear (Japanese)
    """
    差出人: replenish@freshcityretail.com
    宛先: sales@XYZCompany.com
    件名: 情報不足の補充依頼

    営業チーム各位

    シーフードメドレーカップヌードルともう一つのヌードルラインを購入予定です。2つ目の商品名は計画表に記録されておらず、両方の数量もまだ統合中です。

    シーフードメドレーの現在の在庫を共有し、注文締切時間を教えてください。支店データが揃い次第、欠落した商品名と確定数量をお送りします。

    敬具
    小林健
    補充チーム
    """
]