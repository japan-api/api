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
