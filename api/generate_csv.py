import csv
from prefectures import *

with open('../data/japan.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=japan.keys())
    writer.writeheader()
    writer.writerow(japan)

with open('../data/prefectures/hokkaido.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=hokkaido.keys())
    writer.writeheader()
    writer.writerow(hokkaido)

with open('../data/prefectures/aomori.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=aomori.keys())
    writer.writeheader()
    writer.writerow(aomori)

with open('../data/prefectures/iwate.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=iwate.keys())
    writer.writeheader()
    writer.writerow(iwate)

with open('../data/prefectures/miyagi.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=miyagi.keys())
    writer.writeheader()
    writer.writerow(miyagi)

with open('../data/prefectures/akita.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=akita.keys())
    writer.writeheader()
    writer.writerow(akita)

with open('../data/prefectures/yamagata.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=yamagata.keys())
    writer.writeheader()
    writer.writerow(yamagata)

with open('../data/prefectures/fukushima.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fukushima.keys())
    writer.writeheader()
    writer.writerow(fukushima)

with open('../data/prefectures/ibaraki.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=ibaraki.keys())
    writer.writeheader()
    writer.writerow(ibaraki)

with open('../data/prefectures/tochigi.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=tochigi.keys())
    writer.writeheader()
    writer.writerow(tochigi)

with open('../data/prefectures/gunma.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=gunma.keys())
    writer.writeheader()
    writer.writerow(gunma)

with open('../data/prefectures/saitama.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=saitama.keys())
    writer.writeheader()
    writer.writerow(saitama)

with open('../data/prefectures/chiba.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=chiba.keys())
    writer.writeheader()
    writer.writerow(chiba)

with open('../data/prefectures/tokyo.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=tokyo.keys())
    writer.writeheader()
    writer.writerow(tokyo)

with open('../data/prefectures/kanagawa.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=kanagawa.keys())
    writer.writeheader()
    writer.writerow(kanagawa)

with open('../data/prefectures/niigata.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=niigata.keys())
    writer.writeheader()
    writer.writerow(niigata)

with open('../data/prefectures/toyama.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=toyama.keys())
    writer.writeheader()
    writer.writerow(toyama)

with open('../data/prefectures/ishikawa.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=ishikawa.keys())
    writer.writeheader()
    writer.writerow(ishikawa)

with open('../data/prefectures/fukui.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fukui.keys())
    writer.writeheader()
    writer.writerow(fukui)

with open('../data/prefectures/yamanashi.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=yamanashi.keys())
    writer.writeheader()
    writer.writerow(yamanashi)

with open('../data/prefectures/nagano.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=nagano.keys())
    writer.writeheader()
    writer.writerow(nagano)

with open('../data/prefectures/gifu.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=gifu.keys())
    writer.writeheader()
    writer.writerow(gifu)

with open('../data/prefectures/shizuoka.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=shizuoka.keys())
    writer.writeheader()
    writer.writerow(shizuoka)

with open('../data/prefectures/aichi.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=aichi.keys())
    writer.writeheader()
    writer.writerow(aichi)

with open('../data/prefectures/mie.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=mie.keys())
    writer.writeheader()
    writer.writerow(mie)

with open('../data/prefectures/shiga.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=shiga.keys())
    writer.writeheader()
    writer.writerow(shiga)

with open('../data/prefectures/kyoto.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=kyoto.keys())
    writer.writeheader()
    writer.writerow(kyoto)

with open('../data/prefectures/osaka.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=osaka.keys())
    writer.writeheader()
    writer.writerow(osaka)

with open('../data/prefectures/hyogo.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=hyogo.keys())
    writer.writeheader()
    writer.writerow(hyogo)

with open('../data/prefectures/nara.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=nara.keys())
    writer.writeheader()
    writer.writerow(nara)

with open('../data/prefectures/wakayama.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=wakayama.keys())
    writer.writeheader()
    writer.writerow(wakayama)

with open('../data/prefectures/tottori.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=tottori.keys())
    writer.writeheader()
    writer.writerow(tottori)

with open('../data/prefectures/shimane.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=shimane.keys())
    writer.writeheader()
    writer.writerow(shimane)

with open('../data/prefectures/okayama.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=okayama.keys())
    writer.writeheader()
    writer.writerow(okayama)

with open('../data/prefectures/hiroshima.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=hiroshima.keys())
    writer.writeheader()
    writer.writerow(hiroshima)

with open('../data/prefectures/yamaguchi.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=yamaguchi.keys())
    writer.writeheader()
    writer.writerow(yamaguchi)

with open('../data/prefectures/tokushima.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=tokushima.keys())
    writer.writeheader()
    writer.writerow(tokushima)

with open('../data/prefectures/kagawa.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=kagawa.keys())
    writer.writeheader()
    writer.writerow(kagawa)

with open('../data/prefectures/ehime.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=ehime.keys())
    writer.writeheader()
    writer.writerow(ehime)

with open('../data/prefectures/kochi.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=kochi.keys())
    writer.writeheader()
    writer.writerow(kochi)

with open('../data/prefectures/fukuoka.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fukuoka.keys())
    writer.writeheader()
    writer.writerow(fukuoka)

with open('../data/prefectures/saga.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=saga.keys())
    writer.writeheader()
    writer.writerow(saga)

with open('../data/prefectures/nagasaki.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=nagasaki.keys())
    writer.writeheader()
    writer.writerow(nagasaki)

with open('../data/prefectures/kumamoto.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=kumamoto.keys())
    writer.writeheader()
    writer.writerow(kumamoto)

with open('../data/prefectures/oita.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=oita.keys())
    writer.writeheader()
    writer.writerow(oita)                        

with open('../data/prefectures/miyazaki.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=miyazaki.keys())
    writer.writeheader()
    writer.writerow(miyazaki)

with open('../data/prefectures/kagoshima.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=kagoshima.keys())
    writer.writeheader()
    writer.writerow(kagoshima)                        

with open('../data/prefectures/okinawa.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=okinawa.keys())
    writer.writeheader()
    writer.writerow(okinawa)