import requests
from bs4 import BeautifulSoup

def scan_allegro():

    items = []

    url = "https://allegro.pl/kategoria/elektronika"

    headers = {"User-Agent": "Mozilla/5.0"}

    try:

        r = requests.get(url, headers=headers)

        soup = BeautifulSoup(r.text, "html.parser")

        titles = soup.find_all("h2")

        for t in titles:

            text = t.get_text().lower()

            items.append({
                "title": text,
                "price": 0,
                "link": "https://allegro.pl"
            })

    except Exception as e:

        print("Allegro error:", e)

    return items
