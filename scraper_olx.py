import requests
from bs4 import BeautifulSoup

def scan_olx():

    items = []

    url = "https://www.olx.pl/elektronika/?search%5Border%5D=created_at:desc"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.text, "html.parser")

    offers = soup.find_all("a", href=True)

    for offer in offers:

        href = offer["href"]

        if "/d/oferta/" not in href:
            continue

        title = offer.get_text().lower()

        price = None

        for word in title.split():

            if "zł" in word:

                try:
                    price = float(word.replace("zł","").replace(",","."))
                except:
                    pass

        if price:

            items.append({
                "title": title,
                "price": price,
                "link": href
            })

    return items