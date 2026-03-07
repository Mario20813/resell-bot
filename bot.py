import time
from scraper_vinted import scan_vinted

print("BOT START")

while True:

    print("Skanuję Vinted...")

    items = scan_vinted()

    print("Znaleziono:", len(items))

    time.sleep(300)
