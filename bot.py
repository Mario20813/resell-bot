import time
from scraper_vinted import scan_vinted
from scraper_olx import scan_olx
from scraper_allegro import scan_allegro
from scraper_promotions import scan_promotions
from price_checker import get_average_price
from discord_alert import send_alert

seen = set()

DISCOUNT_LIMIT = 0.25

while True:

    print("Skanuję oferty...")

    items = (
        scan_vinted()
        + scan_olx()
        + scan_allegro()
        + scan_promotions()
    )

    print("znaleziono ofert:", len(items))
    for item in items:

        link = item["link"]

        if link in seen:
            continue

        avg = get_average_price(item["title"])

        if not avg:
            continue
       
        price = item["price"]

        discount = 1 - price/avg

        if discount > DISCOUNT_LIMIT:

            send_alert(item["title"], price, avg, link)

        seen.add(link)

    time.sleep(30)
