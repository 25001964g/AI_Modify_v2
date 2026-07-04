test_email_4 = [
    # 1. All in list; quantity provided (Spanish)
    """
    De: centralbuy@northgatecommerce.com
    Para: sales@XYZCompany.com
    Asunto: Pedido de reposición multiartículo

    Estimado equipo de ventas,

    Por favor procesen el siguiente pedido confirmado para entrega la próxima semana: 14 Classic Chicken Cup Noodle, 12 Seafood Medley Cup Noodle y 10 Vegetable Garden Cup Noodle. Todas las cantidades están aprobadas y alineadas con la planificación de espacio en estanterías en tres tiendas piloto.

    Mantengan los artículos en cajas separadas con etiquetas y incluyan las referencias de SKU en la lista de empaque para mayor precisión. Confirmen stock y fecha de despacho hoy para que nuestro socio logístico pueda reservar un camión.

    Atentamente,
    Carol Sin
    Compras Centrales
    """,
    # 2. All in list; quantity unclear (French)
    """
    De: buyer.ops@sunplazaretail.com
    À: sales@XYZCompany.com
    Objet: Demande multi‑articles provisoire

    Bonjour équipe,

    Nous avons besoin d’un réapprovisionnement pour Classic Chicken Cup Noodle, Curry Flavor Cup Noodle et Kimchi Spicy Cup Noodle. À ce stade, les quantités exactes ne sont pas prêtes car elles sont encore consolidées au niveau des succursales. Veuillez réserver du stock pour ces trois articles pendant que nous finalisons la planification interne.

    Pourriez‑vous partager la disponibilité actuelle et votre dernière heure limite pour l’expédition de cette semaine ? Nous reviendrons avec les quantités finales après l’approbation financière.

    Cordialement,
    Oscar Cheng
    Opérations d’achat
    """,
    # 3. All partial in list; quantity provided (German)
    """
    Von: orderdesk@harvestretailers.com
    An: sales@XYZCompany.com
    Betreff: Teilweise Namensbestellung mehrerer Artikel

    Sehr geehrtes Verkaufsteam,

    Bitte arrangieren Sie diese bestätigte Bestellung für unser Convenience‑Netzwerk: 15 Chicken Cup Noodle, 11 Seafood Cup Noodle und 9 Kimchi Cup Noodle. Die Mengen sind festgelegt und genehmigt, aber unser internes Dokument verwendet verkürzte Produktnamen.

    Bitte ordnen Sie jede Zeile Ihrem genauen Katalogprodukt zu und zeigen Sie die endgültigen Artikelnamen auf der Bestätigung. Lieferung wird für Freitagmorgen an unser Hauptlager angefordert.

    Vielen Dank,
    Emily Kwan
    Einkaufskoordinatorin
    """,
    # 4. All partial in list; quantity unclear (Italian)
    """
    Da: sourcing.team@cityretailhub.com
    A: sales@XYZCompany.com
    Oggetto: Rifornimento preliminare assortimento

    Ciao team vendite,

    Stiamo pianificando di rifornire Chicken Cup Noodle, Shrimp Cup Noodle e Pork Cup Noodle per una promozione regionale. I nomi nella nostra richiesta sono abbreviati e le quantità finali sono ancora in attesa dai responsabili di area. Vi chiediamo di riservare un po’ di stock sotto questi gruppi di articoli mentre completiamo l’allocazione.

    Rispondete con le opzioni disponibili e i tempi di consegna per articolo così possiamo chiudere l’ordine ufficiale oggi.

    Cordiali saluti,
    Jason Hui
    Sourcing Strategico
    """,
    # 5. All not in list; quantity provided (Russian)
    """
    От: procurement@nextwavefoods.com
    Кому: sales@XYZCompany.com
    Тема: Запрос на покупку новой линейки

    Уважаемая команда,

    Мы хотели бы разместить подтвержденный пробный заказ на три новых вкуса: 10 Truffle Cream Cup Noodle, 8 Corn Butter Cup Noodle и 12 Pepper Crab Cup Noodle. Количества утверждены для ограниченного теста в премиальных магазинах.

    Подтвердите, доступны ли эти товары в вашем активном каталоге. Если нет, пожалуйста, предложите ближайшие альтернативы с аналогичной ценовой категорией и ожидаемым сроком поставки, чтобы мы могли быстро скорректировать план.

    С уважением,
    Monica Yuen
    Категорийные закупки
    """,
    # 6. All not in list; quantity unclear (Chinese Simplified)
    """
    发件人: planning@retailfrontier.com
    收件人: sales@XYZCompany.com
    主题: 新口味的可用性检查

    销售团队您好，

    我们的商品部门对 Truffle Cream Cup Noodle、Miso Corn Cup Noodle 和 Lobster Bisque Cup Noodle 感兴趣。目前尚未确认数量，因为门店参与仍在进行，但我们需要尽早了解可用性。

    请告知这些产品是否在您产品线中，如果没有，请推荐可快速供应的类似产品用于试点上市。

    此致，
    Raymond Ip
    需求规划
    """,
    # 7. All product not provided; quantity provided (Japanese)
    """
    差出人: buyersupport@harborlinegroup.com
    宛先: sales@XYZCompany.com
    件名: 数量のみの補充ライン

    営業チーム各位

    今回のサイクルで次の数量を確認済みです: ライン1に20ケース、ライン2に14ケース、ライン3に9ケース。内部スプレッドシートで商品名が欠落しましたが、数量は承認済みで直ちに確保すべきです。

    必要な最小限の商品情報を教えていただき、商品フィールドを修正するまでこれらの数量枠を一時的に保持してください。

    よろしくお願いします。
    Tiffany Leung
    購買サポート
    """,
    # 8. All product not provided; quantity unclear (Portuguese)
    """
    De: demand.coordination@greenlanehk.com
    Para: sales@XYZCompany.com
    Assunto: Detalhes pendentes para reposição

    Olá equipe,

    Precisamos criar várias linhas de reposição para nossa categoria de cup noodles, mas tanto os nomes dos produtos quanto as quantidades exatas ainda estão pendentes das filiais. Por favor, reservem uma capacidade modesta de estoque para nós até que os detalhes finais sejam confirmados.

    Poderiam compartilhar sua política de alocação e o último prazo de pedido? Assim que a consolidação interna estiver concluída, enviaremos imediatamente os nomes e quantidades completos.

    Atenciosamente,
    Gloria Pui
    Coordenação de Demanda
    """,
    # 9. All in list by SKU; quantity provided (Arabic)
    """
    من: purchasing@riverstonefoods.com
    إلى: sales@XYZCompany.com
    الموضوع: أمر شراء متعدد العناصر حسب SKU

    فريق المبيعات المحترم،

    يرجى معالجة الطلب المؤكد التالي حسب SKU: 18 وحدة من SKU1001، و16 وحدة من SKU1005، و12 وحدة من SKU1008. تمت الموافقة على جميع الكميات من قبل لجنة التوريد ويجب تسليمها إلى المستودع RS-02 يوم الجمعة.

    يرجى تضمين SKU ووصف المنتج في الفاتورة وقائمة التعبئة. نرجو تأكيد توفر المخزون وتوقيت الشحن المخطط لإكمال الحجز الداخلي.

    مع خالص التحية،
    Howard Tsang
    مدير المشتريات
    """,
    # 10. All in list; over stock (Korean)
    """
    발신: operations.buying@megastorechain.com
    수신: sales@XYZCompany.com
    제목: 대규모 프로모션 주문

    영업팀 여러분,

    대규모 프로모션을 준비 중이며 다음 수량을 요청합니다: Classic Chicken Cup Noodle 120개, Spicy Beef Cup Noodle 140개, Shrimp Flavor Cup Noodle 110개. 이 수치는 이미 인쇄된 캠페인 자료와 연결되어 있으므로 긴급한 재고 확인이 필요합니다.

    즉시 공급 가능한 수량과 부족분에 대한 분할 배송 가능 여부를 알려주시기 바랍니다. 매장 활성화 계획을 맞추기 위해 빠른 회신을 부탁드립니다.

    감사합니다,
    Winnie Ko
    운영 구매팀
    """
]
