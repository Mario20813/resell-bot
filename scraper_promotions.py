import requests
from bs4 import BeautifulSoup

def scan_promotions():

    deals = []

    url = "https://www.pepper.pl/gorace"

    headers = {"User-Agent": "Mozilla/5.0"}

    try:

        r = requests.get(url, headers=headers)

        soup = BeautifulSoup(r.text, "html.parser")

        titles = soup.find_all("a")

        for t in titles:

            text = t.get_text().lower()

            if "%" in text:

                deals.append({
                    "title": text,
                    "price": 0,
                    "link": "https://www.pepper.pl"
                })

    except Exception as e:

        print("Pepper error:", e)

    return deals
