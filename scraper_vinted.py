import requests

def scan_vinted():

    items = []

    url = "https://www.vinted.pl/api/v2/catalog/items?order=newest_first&page=1&per_page=50"

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json"
    }

    try:

        r = requests.get(url, headers=headers, timeout=10)

        if r.status_code != 200:
            print("Vinted status:", r.status_code)
            return []

        data = r.json()

    except Exception as e:

        print("Błąd pobierania Vinted:", e)
        return []

    for item in data.get("items", []):

        try:

            title = item["title"].lower()
            price = float(item["price"]["amount"])
            link = "https://www.vinted.pl/items/" + str(item["id"])

            items.append({
                "title": title,
                "price": price,
                "link": link
            })

        except:
            pass

    return items
