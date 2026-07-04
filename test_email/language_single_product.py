test_email_3 = [
    # 1. En lista; cantidad proporcionada (Spanish)
    """
    De: purchasing@northvaleretail.com
    Para: sales@XYZCompany.com
    Asunto: Solicitud de reposición semanal

    Estimado equipo de ventas,

    Estamos preparando la promoción de la próxima semana en la tienda de conveniencia y necesitamos una reposición confirmada. Por favor, organicen 24 Classic Chicken Cup Noodle para nuestro almacén de Kowloon. Esta cantidad fue aprobada por nuestro gerente de categoría y coincide con el plan de reorganización de estanterías. Les rogamos mantener su embalaje estándar de cartón de exportación e incluir el código del artículo en la factura comercial para facilitar la recepción.

    Si hay stock disponible, agradeceríamos el despacho para el jueves por la tarde. Por favor, confirmen disponibilidad, fecha de envío prevista y monto final.

    Atentamente,
    Martin Lee
    Oficial de Compras
    """,
    # 2. En liste; quantité non claire ou non fournie (French)
    """
    De: buyer.team@harborchain.com
    À: sales@XYZCompany.com
    Objet: Réapprovisionnement urgent de Cup Noodle

    Bonjour équipe des ventes,

    Nos superviseurs de succursale ont signalé une forte demande pour le Spicy Beef Cup Noodle cette semaine. Veuillez nous envoyer du stock supplémentaire pour un réapprovisionnement immédiat. Nous n’avons pas encore le nombre final de cartons car deux magasins doivent encore soumettre leurs chiffres de consommation, mais nous avons besoin que l’expédition parte dès que possible.

    Merci de réserver l’inventaire maintenant et de partager votre premier créneau de livraison. Une fois le décompte interne approuvé, nous répondrons avec la quantité confirmée dans le même fil.

    Cordialement,
    Chloe Wong
    Département des achats
    """,
    # 3. Produkt nicht angegeben; Menge angegeben (German)
    """
    Von: ordering@sunrisefoodsupply.com
    An: sales@XYZCompany.com
    Betreff: Standard-Nachbestellmenge

    Sehr geehrtes Team,

    Bitte bearbeiten Sie eine Nachbestellung von 18 Kartons aus Ihrem Cup-Noodle-Sortiment für unsere städtischen Filialen. Die Menge ist bestätigt und sollte gemäß unseren regulären Kontobedingungen versendet werden. Unser Merchandising-Team hat vergessen, den genauen Geschmack in dieser Anfrage zu notieren, aber die Menge ist festgelegt und von der Finanzabteilung für diesen Zyklus genehmigt.

    Bitte bestätigen Sie den Erhalt dieser Nachricht und teilen Sie uns mit, welche Produktdetails Sie noch benötigen, damit wir die Artikelbestätigung schnell abschließen und Versandverzögerungen vermeiden können.

    Mit freundlichen Grüßen,
    Andrew Ho
    Supply Planning
    """,
    # 4. Non in elenco; quantità fornita (Italian)
    """
    Da: procurement@greenbasketmart.com
    A: sales@XYZCompany.com
    Oggetto: Acquisto di prova nuovo gusto

    Ciao team vendite,

    Vorremmo effettuare un ordine di prova di 12 Tomato Basil Cup Noodle per alcuni negozi premium selezionati. La quantità è ridotta perché si tratta di un test di mercato legato a schede di feedback dei clienti. Se l’articolo è disponibile, vi preghiamo di indicare i tempi di consegna e confermare se consentite pallet con gusti misti.

    Se il prodotto non fa parte del vostro catalogo attuale, fateci sapere l’alternativa più vicina disponibile così il nostro team potrà rivedere la nota di lancio oggi stesso.

    Grazie,
    Irene Cheung
    Buyer di categoria
    """,
    # 5. Продукт не указан; количество неясно или не предоставлено (Russian)
    """
    От: sourcing@metrochoicegroup.com
    Кому: sales@XYZCompany.com
    Тема: Запрос на пополнение запасов

    Уважаемые коллеги по продажам,

    Нам необходимо пополнить запасы Cup Noodle для нашей кампании выходного дня и мы хотели бы разместить заказ в ближайшее время. На данный момент наша команда знает только то, что требуется несколько дополнительных коробок, но детали продукта и точное количество еще ожидаются от региональных менеджеров. Пожалуйста, помогите нам зарезервировать небольшую партию, чтобы мы могли оформить заказ после завершения внутреннего утверждения.

    Просим ответить о текущей ситуации со складом и крайним сроком для отправки на следующий день, чтобы мы могли завершить заявку на покупку без потери времени кампании.

    С уважением,
    Peter Ng
    Команда закупок
    """,
    # 6. 未在清单中；数量不明确或未提供 (Chinese - Simplified)
    """
    发件人: demand.planning@dailycart.hk
    收件人: sales@XYZCompany.com
    主题: 季节性口味方便面询问

    您好，

    我们的产品团队正在寻找味噌玉米杯面，用于主题促销，如果有供应希望能购买一些。由于门店报名仍在进行，我们尚未确认数量，但需要在明天上午前得到初步回复以便规划。

    请告知该SKU是否在您产品系列中，如不可供货，请推荐口味相近且交期相似的替代品。

    此致，
    Vivian Lau
    采购分析师
    """,
    # 7. 在列表中按SKU；数量已提供 (Japanese)
    """
    差出人: purchasing.ops@eastbridgefoods.com
    宛先: sales@XYZCompany.com
    件名: SKUによる発注依頼

    営業チーム各位

    月次補充サイクルのため、SKU1004を30ユニット手配してください。数量と配送先倉庫は確認済みで、通常通り契約 EB-24-Q3 に基づいて請求されるべきです。受け取りチームは、チェックイン時間を短縮するため、SKUと英語の商品名を記載したカートンラベルを希望しています。

    ご注文確認と出荷予定日をご送付ください。もし在庫が希望数量と異なる場合は、その旨もお知らせください。

    ご協力ありがとうございます。

    敬具
    Kelvin Chan
    調達リード
    """,
    # 8. En lista por SKU; cantidad no clara o no proporcionada (Portuguese)
    """
    De: buyer@harvestnetwork.com
    Para: sales@XYZCompany.com
    Assunto: Reserva provisória de SKU

    Olá equipe,

    Podemos precisar de estoque adicional do SKU1006 para a próxima temporada de festas. O número final ainda está em revisão, mas por favor reservem alguma quantidade para nós, se possível, para não ficarmos sem estoque no fim do mês. Os gerentes das filiais estão enviando previsões revisadas esta noite.

    Poderiam compartilhar a disponibilidade atual e a janela de alocação recomendada? Voltaremos com a quantidade exata de compra assim que as verificações internas forem concluídas.

    Atenciosamente,
    Susan Yip
    Compras Centrais
    """,
    # 9. En lista; sobre stock (>100) (Arabic)
    """
    من: procurement@citymaxretail.com
    إلى: sales@XYZCompany.com
    الموضوع: طلب كمية كبيرة

    فريق المبيعات المحترم،

    نحن نطلق حملة خصومات على مستوى السلسلة ونرغب في تقديم طلب لـ 130 عبوة من Seafood Medley Cup Noodle للتسليم الفوري. هذه الكمية مرتبطة بآليات الترويج المطبوعة بالفعل في منشورنا، لذلك نأمل في تأمين المخزون بسرعة.

    يرجى تأكيد ما إذا كان يمكن شحن الكمية الكاملة دفعة واحدة. إذا كان لابد من تنفيذ جزئي، شاركوا أقصى كمية متاحة وأقرب تاريخ للباقي حتى يتمكن فريق العمليات لدينا من تعديل خطط الرفوف.

    مع خالص التحية،
    Gary Poon
    مشتري، البقالة الجافة
    """,
    # 10. En lista; cantidad inválida (0 / negativa / decimal) (Korean)
    """
    발신: planning@dailyharvestgroup.com
    수신: sales@XYZCompany.com
    제목: 조정 요청

    영업팀 여러분께,

    이전 요청을 업데이트하고 있으며 현재 이번 사이클의 초안 라인에 0 Vegetable Garden Cup Noodle이 기재되어 있습니다. 이 수량이 주문 워크시트에 남아 있어야 하는지, 아니면 최종 확인 전에 제거해야 하는지 확인 부탁드립니다. 해당 수량은 반품 조정 후 자동 계산에서 나온 것입니다.

    유효한 수량에 대한 귀사의 요구 형식을 알려주시면 저희 팀이 즉시 수정하여 구매 요청을 다시 발행할 수 있습니다.

    감사합니다,
    Anita Lam
    재고 계획
    """
]
