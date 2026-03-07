import requests

def scan_vinted():

    items = []

    url = "https://www.vinted.pl/api/v2/catalog/items?order=newest_first&page=1&per_page=50"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    r = requests.get(url, headers=headers)

    data = r.json()

    for item in data["items"]:

        title = item["title"].lower()
        price = float(item["price"]["amount"])
        link = "https://www.vinted.pl/items/" + str(item["id"])

        items.append({
            "title": title,
            "price": price,
            "link": link
        })

    return items
