import requests
from bs4 import BeautifulSoup

def get_average_price(product):

    prices = []

    url = f"https://allegro.pl/listing?string={product}"

    headers = {"User-Agent":"Mozilla/5.0"}

    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.text,"html.parser")

    spans = soup.find_all("span")

    for s in spans:

        text = s.get_text().lower()

        if "zł" in text:

            try:

                p = float(text.replace("zł","").replace(",",".").strip())

                if p < 20000:
                    prices.append(p)

            except:
                pass

    if len(prices) == 0:
        return None

    return sum(prices) / len(prices)