import requests
from bs4 import BeautifulSoup

def scan_vinted():

    items = []

    url = "https://www.vinted.pl/catalog?order=newest_first"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    try:

        r = requests.get(url, headers=headers, timeout=10)
        print("Vinted HTML status:", r.status_code)

        soup = BeautifulSoup(r.text, "html.parser")

      offers = soup.select("a[href^='/items/']")

print("Znaleziono ofert:", len(offers))

    for offer in offers[:30]:

        link = "https://www.vinted.pl" + offer["href"]

        print("OFERTA:", link)

        items.append({
            "title": "",
            "price": 0,
            "link": link
        })
    except Exception as e:
        print("Vinted error:", e)

    return items
