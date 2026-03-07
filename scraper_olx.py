import requests
from bs4 import BeautifulSoup

def scan_olx():

    items = []

    url = "https://www.olx.pl/elektronika/?search%5Border%5D=created_at:desc"

    headers = {"User-Agent": "Mozilla/5.0"}

    try:

        r = requests.get(url, headers=headers)

        soup = BeautifulSoup(r.text, "html.parser")

        offers = soup.find_all("a", href=True)

        for offer in offers:

            href = offer["href"]

            if "/d/oferta/" not in href:
                continue

            text = offer.get_text().lower()

            price = None

            for w in text.split():

                if "zł" in w:

                    try:
                        price = float(w.replace("zł","").replace(",","."))
                    except:
                        pass

            if price:

                items.append({
                    "title": text,
                    "price": price,
                    "link": href
                })

    except Exception as e:

        print("OLX error:", e)

    return items
