import requests

def scan_vinted():

    items = []

    url = "https://www.vinted.pl/api/v2/catalog/items?order=newest_first&page=1&per_page=50"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept": "application/json",
        "Accept-Language": "pl-PL,pl;q=0.9",
        "Referer": "https://www.vinted.pl/",
        "Origin": "https://www.vinted.pl"
    }

    try:

        r = requests.get(url, headers=headers, timeout=10)

        print("Vinted status:", r.status_code)

        if r.status_code != 200:
            return []

        data = r.json()

    except Exception as e:

        print("Vinted error:", e)
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
