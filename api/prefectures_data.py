import requests
from bs4 import BeautifulSoup

hokkaido_page = requests.get('https://en.wikipedia.org/wiki/Hokkaido')
hokkaido_soup = BeautifulSoup(hokkaido_page.text, 'html.parser')
raw_hok_pop = hokkaido_soup.find_all('td')[14].find_all(text=True, recursive=True)
raw_hok_den = hokkaido_soup.find_all('td')[16].find_all(text=True, recursive=True)
hokkaido_population = f"{raw_hok_pop[0]}"
hokkaido_density = f"{raw_hok_den[0].replace('/', ' ')}{raw_hok_den[1]}{raw_hok_den[2].replace('/', ' ')}"

aomori_page = requests.get('https://en.wikipedia.org/wiki/Aomori_prefecture')
aomori_soup = BeautifulSoup(aomori_page.text, 'html.parser')
raw_ao_pop = aomori_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_ao_den = aomori_soup.find_all('td')[15].find_all(text=True, recursive=True)
aomori_population = f"{raw_ao_pop[0]}"
aomori_density = f"{raw_ao_den[0].replace('/', ' ')}{raw_ao_den[1]}{raw_ao_den[2].replace('/', ' ')}"

iwate_page = requests.get('https://en.wikipedia.org/wiki/Iwate_prefecture')
iwate_soup = BeautifulSoup(iwate_page.text, 'html.parser')
raw_iw_pop = iwate_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_iw_den = iwate_soup.find_all('td')[15].find_all(text=True, recursive=True)
iwate_population = f"{raw_iw_pop[0]}"
iwate_density = f"{raw_iw_den[0].replace('/', ' ')}{raw_iw_den[1]}{raw_iw_den[2].replace('/', ' ')}"

miyagi_page = requests.get('https://en.wikipedia.org/wiki/Miyagi_prefecture')
miyagi_soup = BeautifulSoup(miyagi_page.text, 'html.parser')
raw_mi_pop = miyagi_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_mi_den = miyagi_soup.find_all('td')[15].find_all(text=True, recursive=True)
miyagi_population = f"{raw_mi_pop[0]}"
miyagi_density = f"{raw_mi_den[0].replace('/', ' ')}{raw_mi_den[1]}{raw_mi_den[2].replace('/', ' ')}"

akita_page = requests.get('https://en.wikipedia.org/wiki/Akita_prefecture')
akita_soup = BeautifulSoup(akita_page.text, 'html.parser')
raw_ak_pop = akita_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_ak_den = akita_soup.find_all('td')[15].find_all(text=True, recursive=True)
akita_population = f"{raw_ak_pop[0]}"
akita_density = f"{raw_ak_den[0].replace('/', ' ')}{raw_ak_den[1]}{raw_ak_den[2].replace('/', ' ')}"

yamagata_page = requests.get('https://en.wikipedia.org/wiki/Yamagata_prefecture')
yamagata_soup = BeautifulSoup(yamagata_page.text, 'html.parser')
raw_ya_pop = yamagata_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_ya_den = yamagata_soup.find_all('td')[15].find_all(text=True, recursive=True)
yamagata_population = f"{raw_ya_pop[0]}"
yamagata_density = f"{raw_ya_den[0].replace('/', ' ')}{raw_ya_den[1]}{raw_ya_den[2].replace('/', ' ')}"

fukushima_page = requests.get('https://en.wikipedia.org/wiki/Fukushima_prefecture')
fukushima_soup = BeautifulSoup(fukushima_page.text, 'html.parser')
raw_fu_pop = fukushima_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_fu_den = fukushima_soup.find_all('td')[15].find_all(text=True, recursive=True)
fukushima_population = f"{raw_fu_pop[0]}"
fukushima_density = f"{raw_fu_den[0].replace('/', ' ')}{raw_fu_den[1]}{raw_fu_den[2].replace('/', ' ')}"
