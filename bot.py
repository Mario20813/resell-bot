import time
from scraper_olx import scan_olx
from scraper_vinted import scan_vinted
from price_checker import get_average_price
from discord_alert import send_alert

seen = set()

DISCOUNT_LIMIT = 0.3

while True:

    print("Skanuję oferty...")

    items = scan_vinted() + scan_olx()

    for item in items:

        link = item["link"]

        if link in seen:
            continue

        avg = get_average_price(item["title"])

        if not avg:
            continue
        print("ilość ofert:", len(items))
        price = item["price"]

        discount = 1 - price/avg

        if discount > DISCOUNT_LIMIT:

            send_alert(item["title"], price, avg, link)

        seen.add(link)

    time.sleep(30)
