import requests
from bs4 import BeautifulSoup

def scan_vinted():

    items = []

    url = "https://www.vinted.pl/catalog?order=newest_first"

    headers = {"User-Agent":"Mozilla/5.0"}

    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.text,"html.parser")

    links = soup.find_all("a", href=True)

    for link in links:

        href = link["href"]

        if "/items/" not in href:
            continue

        title = link.get_text().lower()

        price = None

        for w in title.split():

            if "zł" in w:

                try:
                    price = float(w.replace("zł","").replace(",","."))
                except:
                    pass

        if price:

            items.append({
                "title": title,
                "price": price,
                "link": "https://www.vinted.pl"+href
            })

    return items