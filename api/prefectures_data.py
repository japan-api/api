import requests
from bs4 import BeautifulSoup

hokkaido_page = requests.get('https://en.wikipedia.org/wiki/Hokkaido')
hokkaido_soup = BeautifulSoup(hokkaido_page.text, 'html.parser')
raw_hok_pop = hokkaido_soup.find_all('td')[14].find_all(text=True, recursive=True)
raw_hok_den = hokkaido_soup.find_all('td')[16].find_all(text=True, recursive=True)
hokkaido_population = f"{raw_hok_pop[0]}"
hokkaido_density = f"{raw_hok_den[0]}{raw_hok_den[1]}"
hokkaido_density_sq = f"{raw_hok_den[2].replace('(', '').replace(')', '')}"
hokkaido_density_sq = hokkaido_density_sq.strip()

aomori_page = requests.get('https://en.wikipedia.org/wiki/Aomori_prefecture')
aomori_soup = BeautifulSoup(aomori_page.text, 'html.parser')
raw_ao_pop = aomori_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_ao_den = aomori_soup.find_all('td')[15].find_all(text=True, recursive=True)
aomori_population = f"{raw_ao_pop[0]}"
aomori_density = f"{raw_ao_den[0]}{raw_ao_den[1]}"
aomori_density_sq = f"{raw_ao_den[2].replace('(', '').replace(')', '')}"
aomori_density_sq = aomori_density_sq.strip()

iwate_page = requests.get('https://en.wikipedia.org/wiki/Iwate_prefecture')
iwate_soup = BeautifulSoup(iwate_page.text, 'html.parser')
raw_iw_pop = iwate_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_iw_den = iwate_soup.find_all('td')[15].find_all(text=True, recursive=True)
iwate_population = f"{raw_iw_pop[0]}"
iwate_density = f"{raw_iw_den[0]}{raw_iw_den[1]}"
iwate_density_sq = f"{raw_iw_den[2].replace('(', '').replace(')', '')}"
iwate_density_sq = iwate_density_sq.strip()

miyagi_page = requests.get('https://en.wikipedia.org/wiki/Miyagi_prefecture')
miyagi_soup = BeautifulSoup(miyagi_page.text, 'html.parser')
raw_mi_pop = miyagi_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_mi_den = miyagi_soup.find_all('td')[15].find_all(text=True, recursive=True)
miyagi_population = f"{raw_mi_pop[0]}"
miyagi_density = f"{raw_mi_den[0]}{raw_mi_den[1]}"
miyagi_density_sq = f"{raw_mi_den[2].replace('(', '').replace(')', '')}"
miyagi_density_sq = miyagi_density_sq.strip()

akita_page = requests.get('https://en.wikipedia.org/wiki/Akita_prefecture')
akita_soup = BeautifulSoup(akita_page.text, 'html.parser')
raw_ak_pop = akita_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_ak_den = akita_soup.find_all('td')[15].find_all(text=True, recursive=True)
akita_population = f"{raw_ak_pop[0]}"
akita_density = f"{raw_ak_den[0]}{raw_ak_den[1]}"
akita_density_sq = f"{raw_ak_den[2].replace('(', '').replace(')', '')}"
akita_density_sq = akita_density_sq.strip()

yamagata_page = requests.get('https://en.wikipedia.org/wiki/Yamagata_prefecture')
yamagata_soup = BeautifulSoup(yamagata_page.text, 'html.parser')
raw_ya_pop = yamagata_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_ya_den = yamagata_soup.find_all('td')[15].find_all(text=True, recursive=True)
yamagata_population = f"{raw_ya_pop[0]}"
yamagata_density = f"{raw_ya_den[0]}{raw_ya_den[1]}"
yamagata_density_sq = f"{raw_ya_den[2].replace('(', '').replace(')', '')}"
yamagata_density_sq = yamagata_density_sq.strip()

fukushima_page = requests.get('https://en.wikipedia.org/wiki/Fukushima_prefecture')
fukushima_soup = BeautifulSoup(fukushima_page.text, 'html.parser')
raw_fu_pop = fukushima_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_fu_den = fukushima_soup.find_all('td')[15].find_all(text=True, recursive=True)
fukushima_population = f"{raw_fu_pop[0]}"
fukushima_density = f"{raw_fu_den[0]}{raw_fu_den[1]}"
fukushima_density_sq = f"{raw_fu_den[2].replace('(', '').replace(')', '')}"
fukushima_density_sq = fukushima_density_sq.strip()

ibaraki_page = requests.get('https://en.wikipedia.org/wiki/Ibaraki_prefecture')
ibaraki_soup = BeautifulSoup(ibaraki_page.text, 'html.parser')
raw_ib_pop = ibaraki_soup.find_all('td')[15].find_all(text=True, recursive=True)
raw_ib_den = ibaraki_soup.find_all('td')[17].find_all(text=True, recursive=True)
ibaraki_population = f"{raw_ib_pop[0]}"
ibaraki_density = f"{raw_ib_den[0]}{raw_ib_den[1]}"
ibaraki_density_sq = f"{raw_ib_den[2].replace('(', '').replace(')', '')}"
ibaraki_density_sq = ibaraki_density_sq.strip()

tochigi_page = requests.get('https://en.wikipedia.org/wiki/Tochigi_prefecture')
tochigi_soup = BeautifulSoup(tochigi_page.text, 'html.parser')
raw_to_pop = tochigi_soup.find_all('td')[15].find_all(text=True, recursive=True)
raw_to_den = tochigi_soup.find_all('td')[17].find_all(text=True, recursive=True)
tochigi_population = f"{raw_to_pop[0]}"
tochigi_density = f"{raw_to_den[0]}{raw_to_den[1]}"
tochigi_density_sq = f"{raw_to_den[2].replace('(', '').replace(')', '')}"
tochigi_density_sq = tochigi_density_sq.strip()

gunma_page = requests.get('https://en.wikipedia.org/wiki/Gunma_prefecture')
gunma_soup = BeautifulSoup(gunma_page.text, 'html.parser')
raw_gu_pop = gunma_soup.find_all('td')[15].find_all(text=True, recursive=True)
raw_gu_den = gunma_soup.find_all('td')[17].find_all(text=True, recursive=True)
gunma_population = f"{raw_gu_pop[0]}"
gunma_density = f"{raw_gu_den[0]}{raw_gu_den[1]}"
gunma_density_sq = f"{raw_gu_den[2].replace('(', '').replace(')', '')}"
gunma_density_sq = gunma_density_sq.strip()

saitama_page = requests.get('https://en.wikipedia.org/wiki/Saitama_prefecture')
saitama_soup = BeautifulSoup(saitama_page.text, 'html.parser')
raw_sa_pop = saitama_soup.find_all('td')[14].find_all(text=True, recursive=True)
raw_sa_den = saitama_soup.find_all('td')[16].find_all(text=True, recursive=True)
saitama_population = f"{raw_sa_pop[0]}"
saitama_density = f"{raw_sa_den[0]}{raw_sa_den[1]}"
saitama_density_sq = f"{raw_sa_den[2].replace('(', '').replace(')', '')}"
saitama_density_sq = saitama_density_sq.strip()

chiba_page = requests.get('https://en.wikipedia.org/wiki/Chiba_prefecture')
chiba_soup = BeautifulSoup(chiba_page.text, 'html.parser')
raw_chi_pop = chiba_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_chi_den = chiba_soup.find_all('td')[15].find_all(text=True, recursive=True)
chiba_population = f"{raw_chi_pop[0]}"
chiba_density = f"{raw_chi_den[0]}{raw_chi_den[1]}"
chiba_density_sq = f"{raw_chi_den[2].replace('(', '').replace(')', '')}"
chiba_density_sq = chiba_density_sq.strip()

tokyo_page = requests.get('https://en.wikipedia.org/wiki/Tokyo')
tokyo_soup = BeautifulSoup(tokyo_page.text, 'html.parser')
raw_to_pop = tokyo_soup.find_all('td')[21].find_all(text=True, recursive=True)
raw_to_den = tokyo_soup.find_all('td')[23].find_all(text=True, recursive=True)
tokyo_population = f"{raw_to_pop[0]}"
tokyo_density = f"{raw_to_den[0]}{raw_to_den[1]}"
tokyo_density_sq = f"{raw_to_den[2].replace('(', '').replace(')', '')}"
tokyo_density_sq = tokyo_density_sq.strip()

kanagawa_page = requests.get('https://en.wikipedia.org/wiki/Kanagawa_Prefecture')
kanagawa_soup = BeautifulSoup(kanagawa_page.text, 'html.parser')
raw_ka_pop = kanagawa_soup.find_all('td')[17].find_all(text=True, recursive=True)
raw_ka_den = kanagawa_soup.find_all('td')[19].find_all(text=True, recursive=True)
kanagawa_population = f"{raw_ka_pop[0]}"
kanagawa_density = f"{raw_ka_den[0]}{raw_ka_den[1]}"
kanagawa_density_sq = f"{raw_ka_den[2].replace('(', '').replace(')', '')}"
kanagawa_density_sq = kanagawa_density_sq.strip()

niigata_page = requests.get('https://en.wikipedia.org/wiki/Niigata_Prefecture')
niigata_soup = BeautifulSoup(niigata_page.text, 'html.parser')
raw_ni_pop = niigata_soup.find_all('td')[15].find_all(text=True, recursive=True)
raw_ni_den = niigata_soup.find_all('td')[17].find_all(text=True, recursive=True)
niigata_population = f"{raw_ni_pop[0]}"
niigata_density = f"{raw_ni_den[0]}{raw_ni_den[1]}"
niigata_density_sq = f"{raw_ni_den[2].replace('(', '').replace(')', '')}"
niigata_density_sq = niigata_density_sq.strip()
