import requests

WEBHOOK = "https://discord.com/api/webhooks/1479566825514598410/rIFQxLmpobEi9Bmt3Fz7KbeS_7X2pc_sRt51meeYfuy_tWxAdOmDHgsOcURpTsRG2r9M"

def send_alert(product, price, avg_price, link):

    discount = round((1 - price/avg_price) * 100)

    data = {
        "content": f"""
🔥 OKAZJA

produkt: {product}

cena oferty: {price} zł
średnia cena: {avg_price} zł

zniżka: -{discount}%

{link}
"""
    }

    requests.post(WEBHOOK, json=data)