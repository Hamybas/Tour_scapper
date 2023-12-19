import time
import sqlite3
import funcs

URL = "https://programmer100.pythonanywhere.com/tours/"

while True:
    scrapped = funcs.scrape(URL)
    extracted = funcs.extract(scrapped)
    print(extracted)
    if extracted != "No upcoming tours":
        row = funcs.read(extracted)
        if not row:
            funcs.store(extracted)
            funcs.send_email(message="Subject: New event" + '\n' + extracted)
            print("email was sent")
    time.sleep(2)
