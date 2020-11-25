import csv
from prefectures import *

with open('../data/japan.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=japan.keys())
    writer.writeheader()
    writer.writerow(japan)

# with open('../data/okinawa.csv', 'w', newline='', encoding="utf-8") as file:
#     writer = csv.DictWriter(file, fieldnames=okinawa.keys())
#     writer.writeheader()
#     writer.writerow(okinawa)