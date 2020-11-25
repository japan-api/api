import requests
from bs4 import BeautifulSoup
# nom - nominal ppp - purchasing power parity,
# den - density, pop - population, gov - governor
# ar - area rank, pr - population rank, dr- density rank

japan_page = requests.get('https://en.wikipedia.org/wiki/Japan')
japan_soup = BeautifulSoup(japan_page.text, 'html.parser')
raw_ja_pop = japan_soup.find_all('td')[20].find_all(text=True, recursive=True)
raw_ja_den = japan_soup.find_all('td')[22].find_all(text=True, recursive=True)
gdp_ppp = japan_soup.find_all('td')[24].find_all(text=True, recursive=True)
gdp_ppp_per = japan_soup.find_all('td')[25].find_all(text=True, recursive=True)
gdp_nom = japan_soup.find_all('td')[27].find_all(text=True, recursive=True)
gdp_nom_per = japan_soup.find_all('td')[28].find_all(text=True, recursive=True)
japan_emperor = japan_soup.find_all('td')[8].find_all(text=True, recursive=True)
japan_minister = japan_soup.find_all('td')[9].find_all(text=True, recursive=True)
raw_gini = japan_soup.find_all('td')[29].find_all(text=True, recursive=True)
raw_hdi = japan_soup.find_all('td')[30].find_all(text=True, recursive=True)
raw_ja_ar = japan_soup.find_all('td')[18].find_all(text=True, recursive=True)
raw_ja_pr = japan_soup.find_all('td')[20].find_all(text=True, recursive=True)
japan_area_rank = f"{raw_ja_ar[-2]}"
japan_population_rank = f"{raw_ja_pr[-2]}"
japan_density_rank = f"{raw_ja_den[-2]}"
japan_gini = f"{raw_gini[0]} - {raw_gini[2]}"
japan_hdi = f"{raw_hdi[0].strip()} - {raw_hdi[2]}"
japan_emperor = f"{japan_emperor[0]}"
japan_minister = f"{japan_minister[0]}"
gdp_nom = f"{gdp_nom[0].strip()}"
gdp_ppp = f"{gdp_ppp[0].strip()}"
gdp_nom_per = f"{gdp_nom_per[0].replace('(', '')}"
gdp_ppp_per = f"{gdp_ppp_per[0].replace('(', '')}"
japan_population = f"{raw_ja_pop[0].strip()}"
japan_density = f"{raw_ja_den[0]}{raw_ja_den[1]}"
japan_density_mi = f"{raw_ja_den[2].replace('(', '').replace(')', '')}"
japan_density_mi = japan_density_mi.strip()
gdp_ppp_per = gdp_ppp_per.strip()
gdp_nom_per = gdp_nom_per.strip()

hokkaido_page = requests.get('https://en.wikipedia.org/wiki/Hokkaido')
hokkaido_soup = BeautifulSoup(hokkaido_page.text, 'html.parser')
raw_hok_pop = hokkaido_soup.find_all('td')[14].find_all(text=True, recursive=True)
raw_hok_den = hokkaido_soup.find_all('td')[16].find_all(text=True, recursive=True)
raw_hok_gov = hokkaido_soup.find_all('td')[11].find_all(text=True, recursive=True)
raw_hok_ar = hokkaido_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_hok_pr = hokkaido_soup.find_all('td')[15].find_all(text=True, recursive=True)
hokkaido_area_rank = int(raw_hok_ar[0].replace('st', ''))
hokkaido_pop_rank = int(raw_hok_pr[0].replace('th', '')) 
hokkaido_governor = f"{raw_hok_gov[0]}"
hokkaido_population = f"{raw_hok_pop[0]}"
hokkaido_density = f"{raw_hok_den[0]}{raw_hok_den[1]}"
hokkaido_density_mi = f"{raw_hok_den[2].replace('(', '').replace(')', '')}"
hokkaido_density_mi = hokkaido_density_mi.strip()

aomori_page = requests.get('https://en.wikipedia.org/wiki/Aomori_prefecture')
aomori_soup = BeautifulSoup(aomori_page.text, 'html.parser')
raw_ao_pop = aomori_soup.find_all('td')[18].find_all(text=True, recursive=True)
raw_ao_den = aomori_soup.find_all('td')[20].find_all(text=True, recursive=True)
raw_ao_gov = aomori_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_ao_ar = aomori_soup.find_all('td')[15].find_all(text=True, recursive=True)
raw_ao_pr = aomori_soup.find_all('td')[19].find_all(text=True, recursive=True)
aomori_area_rank = int(raw_ao_ar[0].replace('th', ''))
aomori_pop_rank = int(raw_ao_pr[0].replace('st', ''))
aomori_governor = f"{raw_ao_gov[0]}"
aomori_population = f"{raw_ao_pop[0]}"
aomori_density = f"{raw_ao_den[0]}{raw_ao_den[1]}"
aomori_density_mi = f"{raw_ao_den[2].replace('(', '').replace(')', '')}"
aomori_density_mi = aomori_density_mi.strip()

iwate_page = requests.get('https://en.wikipedia.org/wiki/Iwate_prefecture')
iwate_soup = BeautifulSoup(iwate_page.text, 'html.parser')
raw_iw_pop = iwate_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_iw_den = iwate_soup.find_all('td')[15].find_all(text=True, recursive=True)
raw_iw_gov = iwate_soup.find_all('td')[10].find_all(text=True, recursive=True)
raw_iw_ar = iwate_soup.find_all('td')[12].find_all(text=True, recursive=True)
raw_iw_pr = iwate_soup.find_all('td')[14].find_all(text=True, recursive=True)
iwate_area_rank = int(raw_iw_ar[0].replace('nd', ''))
iwate_pop_rank = int(raw_iw_pr[0].replace('nd', '')) 
iwate_governor = f"{raw_iw_gov[0]}"
iwate_population = f"{raw_iw_pop[0]}"
iwate_density = f"{raw_iw_den[0]}{raw_iw_den[1]}"
iwate_density_mi = f"{raw_iw_den[2].replace('(', '').replace(')', '')}"
iwate_density_mi = iwate_density_mi.strip()

miyagi_page = requests.get('https://en.wikipedia.org/wiki/Miyagi_prefecture')
miyagi_soup = BeautifulSoup(miyagi_page.text, 'html.parser')
raw_mi_pop = miyagi_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_mi_den = miyagi_soup.find_all('td')[15].find_all(text=True, recursive=True)
raw_mi_gov = miyagi_soup.find_all('td')[10].find_all(text=True, recursive=True)
raw_mi_ar = miyagi_soup.find_all('td')[12].find_all(text=True, recursive=True)
raw_mi_pr = miyagi_soup.find_all('td')[14].find_all(text=True, recursive=True)
miyagi_area_rank = int(raw_mi_ar[0].replace('th', ''))
miyagi_pop_rank = int(raw_mi_pr[0].replace('th', '')) 
miyagi_governor = f"{raw_mi_gov[0]}"
miyagi_population = f"{raw_mi_pop[0]}"
miyagi_density = f"{raw_mi_den[0]}{raw_mi_den[1]}"
miyagi_density_mi = f"{raw_mi_den[2].replace('(', '').replace(')', '')}"
miyagi_density_mi = miyagi_density_mi.strip()

akita_page = requests.get('https://en.wikipedia.org/wiki/Akita_prefecture')
akita_soup = BeautifulSoup(akita_page.text, 'html.parser')
raw_ak_pop = akita_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_ak_den = akita_soup.find_all('td')[15].find_all(text=True, recursive=True)
raw_ak_gov = akita_soup.find_all('td')[10].find_all(text=True, recursive=True)
raw_ak_ar = akita_soup.find_all('td')[12].find_all(text=True, recursive=True)
raw_ak_pr = akita_soup.find_all('td')[14].find_all(text=True, recursive=True)
akita_area_rank = int(raw_ak_ar[0].replace('th', ''))
akita_pop_rank = int(raw_ak_pr[0].replace('th', '')) 
akita_governor = f"{raw_ak_gov[0]}"
akita_population = f"{raw_ak_pop[0]}"
akita_density = f"{raw_ak_den[0]}{raw_ak_den[1]}"
akita_density_mi = f"{raw_ak_den[2].replace('(', '').replace(')', '')}"
akita_density_mi = akita_density_mi.strip()

yamagata_page = requests.get('https://en.wikipedia.org/wiki/Yamagata_prefecture')
yamagata_soup = BeautifulSoup(yamagata_page.text, 'html.parser')
raw_ya_pop = yamagata_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_ya_den = yamagata_soup.find_all('td')[15].find_all(text=True, recursive=True)
raw_ya_gov = yamagata_soup.find_all('td')[10].find_all(text=True, recursive=True)
raw_ya_ar = yamagata_soup.find_all('td')[12].find_all(text=True, recursive=True)
raw_ya_pr = yamagata_soup.find_all('td')[14].find_all(text=True, recursive=True)
yamagata_area_rank = int(raw_ya_ar[0].replace('th', ''))
yamagata_pop_rank = int(raw_ya_pr[0].replace('th', '')) 
yamagata_governor = f"{raw_ya_gov[0]}"
yamagata_population = f"{raw_ya_pop[0]}"
yamagata_density = f"{raw_ya_den[0]}{raw_ya_den[1]}"
yamagata_density_mi = f"{raw_ya_den[2].replace('(', '').replace(')', '')}"
yamagata_density_mi = yamagata_density_mi.strip()

fukushima_page = requests.get('https://en.wikipedia.org/wiki/Fukushima_prefecture')
fukushima_soup = BeautifulSoup(fukushima_page.text, 'html.parser')
raw_fu_pop = fukushima_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_fu_den = fukushima_soup.find_all('td')[15].find_all(text=True, recursive=True)
raw_fu_gov = fukushima_soup.find_all('td')[10].find_all(text=True, recursive=True)
raw_fu_ar = fukushima_soup.find_all('td')[12].find_all(text=True, recursive=True)
raw_fu_pr = fukushima_soup.find_all('td')[14].find_all(text=True, recursive=True)
fukushima_area_rank = int(raw_fu_ar[0].replace('rd', ''))
fukushima_pop_rank = int(raw_fu_pr[0].replace('th', '')) 
fukushima_governor = f"{raw_fu_gov[0]}"
fukushima_population = f"{raw_fu_pop[0]}"
fukushima_density = f"{raw_fu_den[0]}{raw_fu_den[1]}"
fukushima_density_mi = f"{raw_fu_den[2].replace('(', '').replace(')', '')}"
fukushima_density_mi = fukushima_density_mi.strip()

ibaraki_page = requests.get('https://en.wikipedia.org/wiki/Ibaraki_prefecture')
ibaraki_soup = BeautifulSoup(ibaraki_page.text, 'html.parser')
raw_ib_pop = ibaraki_soup.find_all('td')[15].find_all(text=True, recursive=True)
raw_ib_den = ibaraki_soup.find_all('td')[17].find_all(text=True, recursive=True)
raw_ib_gov = ibaraki_soup.find_all('td')[12].find_all(text=True, recursive=True)
raw_ib_ar = ibaraki_soup.find_all('td')[14].find_all(text=True, recursive=True)
raw_ib_pr = ibaraki_soup.find_all('td')[16].find_all(text=True, recursive=True)
ibaraki_area_rank = int(raw_ib_ar[0].replace('th', ''))
ibaraki_pop_rank = int(raw_ib_pr[0].replace('th', '')) 
ibaraki_governor = f"{raw_ib_gov[0]}"
ibaraki_population = f"{raw_ib_pop[0]}"
ibaraki_density = f"{raw_ib_den[0]}{raw_ib_den[1]}"
ibaraki_density_mi = f"{raw_ib_den[2].replace('(', '').replace(')', '')}"
ibaraki_density_mi = ibaraki_density_mi.strip()

tochigi_page = requests.get('https://en.wikipedia.org/wiki/Tochigi_prefecture')
tochigi_soup = BeautifulSoup(tochigi_page.text, 'html.parser')
raw_to_pop = tochigi_soup.find_all('td')[15].find_all(text=True, recursive=True)
raw_to_den = tochigi_soup.find_all('td')[17].find_all(text=True, recursive=True)
raw_to_gov = tochigi_soup.find_all('td')[12].find_all(text=True, recursive=True)
raw_to_ar = tochigi_soup.find_all('td')[14].find_all(text=True, recursive=True)
raw_to_pr = tochigi_soup.find_all('td')[16].find_all(text=True, recursive=True)
tochigi_area_rank = int(raw_to_ar[0].replace('th', ''))
tochigi_pop_rank = int(raw_to_pr[0].replace('th', '')) 
tochigi_governor = f"{raw_to_gov[0]}"
tochigi_population = f"{raw_to_pop[0]}"
tochigi_density = f"{raw_to_den[0]}{raw_to_den[1]}"
tochigi_density_mi = f"{raw_to_den[2].replace('(', '').replace(')', '')}"
tochigi_density_mi = tochigi_density_mi.strip()

gunma_page = requests.get('https://en.wikipedia.org/wiki/Gunma_prefecture')
gunma_soup = BeautifulSoup(gunma_page.text, 'html.parser')
raw_gu_pop = gunma_soup.find_all('td')[15].find_all(text=True, recursive=True)
raw_gu_den = gunma_soup.find_all('td')[17].find_all(text=True, recursive=True)
raw_gu_gov = gunma_soup.find_all('td')[12].find_all(text=True, recursive=True)
raw_gu_ar = gunma_soup.find_all('td')[14].find_all(text=True, recursive=True)
raw_gu_pr = gunma_soup.find_all('td')[16].find_all(text=True, recursive=True)
gunma_area_rank = int(raw_gu_ar[0].replace('st', ''))
gunma_pop_rank = int(raw_gu_pr[0].replace('th', '')) 
gunma_governor = f"{raw_gu_gov[0]}"
gunma_population = f"{raw_gu_pop[0]}"
gunma_density = f"{raw_gu_den[0]}{raw_gu_den[1]}"
gunma_density_mi = f"{raw_gu_den[2].replace('(', '').replace(')', '')}"
gunma_density_mi = gunma_density_mi.strip()

saitama_page = requests.get('https://en.wikipedia.org/wiki/Saitama_prefecture')
saitama_soup = BeautifulSoup(saitama_page.text, 'html.parser')
raw_sa_pop = saitama_soup.find_all('td')[14].find_all(text=True, recursive=True)
raw_sa_den = saitama_soup.find_all('td')[16].find_all(text=True, recursive=True)
raw_sa_gov = saitama_soup.find_all('td')[11].find_all(text=True, recursive=True)
raw_sa_ar = saitama_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_sa_pr = saitama_soup.find_all('td')[15].find_all(text=True, recursive=True)
saitama_area_rank = int(raw_sa_ar[0].replace('th', ''))
saitama_pop_rank = int(raw_sa_pr[0].replace('th', '')) 
saitama_governor = f"{raw_sa_gov[0]}"
saitama_population = f"{raw_sa_pop[0]}"
saitama_density = f"{raw_sa_den[0]}{raw_sa_den[1]}"
saitama_density_mi = f"{raw_sa_den[2].replace('(', '').replace(')', '')}"
saitama_density_mi = saitama_density_mi.strip()

chiba_page = requests.get('https://en.wikipedia.org/wiki/Chiba_prefecture')
chiba_soup = BeautifulSoup(chiba_page.text, 'html.parser')
raw_chi_pop = chiba_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_chi_den = chiba_soup.find_all('td')[15].find_all(text=True, recursive=True)
raw_chi_gov = chiba_soup.find_all('td')[10].find_all(text=True, recursive=True)
raw_chi_ar = chiba_soup.find_all('td')[12].find_all(text=True, recursive=True)
raw_chi_pr = chiba_soup.find_all('td')[14].find_all(text=True, recursive=True)
chiba_area_rank = int(raw_chi_ar[0].replace('th', ''))
chiba_pop_rank = int(raw_chi_pr[0].replace('th', '')) 
chiba_governor = f"{raw_chi_gov[0]}"
chiba_population = f"{raw_chi_pop[0]}"
chiba_density = f"{raw_chi_den[0]}{raw_chi_den[1]}"
chiba_density_mi = f"{raw_chi_den[2].replace('(', '').replace(')', '')}"
chiba_density_mi = chiba_density_mi.strip()

tokyo_page = requests.get('https://en.wikipedia.org/wiki/Tokyo')
tokyo_soup = BeautifulSoup(tokyo_page.text, 'html.parser')
raw_tok_pop = tokyo_soup.find_all('td')[21].find_all(text=True, recursive=True)
raw_tok_den = tokyo_soup.find_all('td')[23].find_all(text=True, recursive=True)
raw_tok_gov = tokyo_soup.find_all('td')[14].find_all(text=True, recursive=True)
raw_tok_ar = tokyo_soup.find_all('td')[18].find_all(text=True, recursive=True)
raw_tok_pr = tokyo_soup.find_all('td')[22].find_all(text=True, recursive=True)
tokyo_area_rank = int(raw_tok_ar[0].replace('th in Japan', ''))
tokyo_pop_rank = int(raw_tok_pr[0].replace('st in Japan', '')) 
tokyo_governor = f"{raw_tok_gov[0]}"
tokyo_population = f"{raw_tok_pop[0]}"
tokyo_density = f"{raw_tok_den[0]}{raw_tok_den[1]}"
tokyo_density_mi = f"{raw_tok_den[2].replace('(', '').replace(')', '')}"
tokyo_density_mi = tokyo_density_mi.strip()

kanagawa_page = requests.get('https://en.wikipedia.org/wiki/Kanagawa_Prefecture')
kanagawa_soup = BeautifulSoup(kanagawa_page.text, 'html.parser')
raw_ka_pop = kanagawa_soup.find_all('td')[17].find_all(text=True, recursive=True)
raw_ka_den = kanagawa_soup.find_all('td')[19].find_all(text=True, recursive=True)
raw_ka_gov = kanagawa_soup.find_all('td')[14].find_all(text=True, recursive=True)
raw_ka_ar = kanagawa_soup.find_all('td')[16].find_all(text=True, recursive=True)
raw_ka_pr = kanagawa_soup.find_all('td')[18].find_all(text=True, recursive=True)
kanagawa_area_rank = int(raw_ka_ar[0].replace('rd', ''))
kanagawa_pop_rank = int(raw_ka_pr[0].replace('nd', '')) 
kanagawa_governor = f"{raw_ka_gov[0]}"
kanagawa_population = f"{raw_ka_pop[0]}"
kanagawa_density = f"{raw_ka_den[0]}{raw_ka_den[1]}"
kanagawa_density_mi = f"{raw_ka_den[2].replace('(', '').replace(')', '')}"
kanagawa_density_mi = kanagawa_density_mi.strip()

niigata_page = requests.get('https://en.wikipedia.org/wiki/Niigata_Prefecture')
niigata_soup = BeautifulSoup(niigata_page.text, 'html.parser')
raw_ni_pop = niigata_soup.find_all('td')[15].find_all(text=True, recursive=True)
raw_ni_den = niigata_soup.find_all('td')[17].find_all(text=True, recursive=True)
raw_ni_gov = niigata_soup.find_all('td')[12].find_all(text=True, recursive=True)
raw_ni_ar = niigata_soup.find_all('td')[14].find_all(text=True, recursive=True)
raw_ni_pr = niigata_soup.find_all('td')[16].find_all(text=True, recursive=True)
niigata_area_rank = int(raw_ni_ar[0].replace('th', ''))
niigata_pop_rank = int(raw_ni_pr[0].replace('th', '')) 
niigata_governor = f"{raw_ni_gov[0]}"
niigata_population = f"{raw_ni_pop[0]}"
niigata_density = f"{raw_ni_den[0]}{raw_ni_den[1]}"
niigata_density_mi = f"{raw_ni_den[2].replace('(', '').replace(')', '')}"
niigata_density_mi = niigata_density_mi.strip()

toyama_page = requests.get('https://en.wikipedia.org/wiki/Toyama_prefecture')
toyama_soup = BeautifulSoup(toyama_page.text, 'html.parser')
raw_toy_pop = toyama_soup.find_all('td')[16].find_all(text=True, recursive=True)
raw_toy_den = toyama_soup.find_all('td')[18].find_all(text=True, recursive=True)
raw_toy_gov = toyama_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_toy_ar = toyama_soup.find_all('td')[15].find_all(text=True, recursive=True)
raw_toy_pr = toyama_soup.find_all('td')[17].find_all(text=True, recursive=True)
toyama_area_rank = int(raw_toy_ar[0].replace('rd', ''))
toyama_pop_rank = int(raw_toy_pr[0].replace('th', '')) 
toyama_governor = f"{raw_toy_gov[0]}"
toyama_population = f"{raw_toy_pop[0]}"
toyama_density = f"{raw_toy_den[0]}{raw_toy_den[1]}"
toyama_density_mi = f"{raw_toy_den[2].replace('(', '').replace(')', '')}"
toyama_density_mi = toyama_density_mi.strip()

ishikawa_page = requests.get('https://en.wikipedia.org/wiki/Ishikawa_prefecture')
ishikawa_soup = BeautifulSoup(ishikawa_page.text, 'html.parser')
raw_ish_pop = ishikawa_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_ish_den = ishikawa_soup.find_all('td')[15].find_all(text=True, recursive=True)
raw_ish_gov = ishikawa_soup.find_all('td')[10].find_all(text=True, recursive=True)
raw_ish_ar = ishikawa_soup.find_all('td')[12].find_all(text=True, recursive=True)
raw_ish_pr = ishikawa_soup.find_all('td')[14].find_all(text=True, recursive=True)
ishikawa_area_rank = int(raw_ish_ar[0].replace('th', ''))
ishikawa_pop_rank = int(raw_ish_pr[0].replace('th', '')) 
ishikawa_governor = f"{raw_ish_gov[0]}"
ishikawa_population = f"{raw_ish_pop[0]}"
ishikawa_density = f"{raw_ish_den[0]}{raw_ish_den[1]}"
ishikawa_density_mi = f"{raw_ish_den[2].replace('(', '').replace(')', '')}"
ishikawa_density_mi = ishikawa_density_mi.strip()

fukui_page = requests.get('https://en.wikipedia.org/wiki/Fukui_prefecture')
fukui_soup = BeautifulSoup(fukui_page.text, 'html.parser')
raw_fuk_pop = fukui_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_fuk_den = fukui_soup.find_all('td')[15].find_all(text=True, recursive=True)
raw_fuk_gov = fukui_soup.find_all('td')[10].find_all(text=True, recursive=True)
raw_fuk_ar = fukui_soup.find_all('td')[12].find_all(text=True, recursive=True)
raw_fuk_pr = fukui_soup.find_all('td')[14].find_all(text=True, recursive=True)
fukui_area_rank = int(raw_fuk_ar[0].replace('th', ''))
fukui_pop_rank = int(raw_fuk_pr[0].replace('rd', '')) 
fukui_governor = f"{raw_fuk_gov[0]}"
fukui_population = f"{raw_fuk_pop[0]}"
fukui_density = f"{raw_fuk_den[0]}{raw_fuk_den[1]}"
fukui_density_mi = f"{raw_fuk_den[2].replace('(', '').replace(')', '')}"
fukui_density_mi = fukui_density_mi.strip()

yamanashi_page = requests.get('https://en.wikipedia.org/wiki/Yamanashi_prefecture')
yamanashi_soup = BeautifulSoup(yamanashi_page.text, 'html.parser')
raw_yam_pop = yamanashi_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_yam_den = yamanashi_soup.find_all('td')[15].find_all(text=True, recursive=True)
raw_yam_gov = yamanashi_soup.find_all('td')[10].find_all(text=True, recursive=True)
raw_yam_ar = yamanashi_soup.find_all('td')[12].find_all(text=True, recursive=True)
raw_yam_pr = yamanashi_soup.find_all('td')[14].find_all(text=True, recursive=True)
yamanashi_area_rank = int(raw_yam_ar[0].replace('nd', ''))
yamanashi_pop_rank = int(raw_yam_pr[0].replace('st', '')) 
yamanashi_governor = f"{raw_yam_gov[0]}"
yamanashi_population = f"{raw_yam_pop[0]}"
yamanashi_density = f"{raw_yam_den[0]}{raw_yam_den[1]}"
yamanashi_density_mi = f"{raw_yam_den[2].replace('(', '').replace(')', '')}"
yamanashi_density_mi = yamanashi_density_mi.strip()

nagano_page = requests.get('https://en.wikipedia.org/wiki/Nagano_prefecture')
nagano_soup = BeautifulSoup(nagano_page.text, 'html.parser')
raw_na_pop = nagano_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_na_den = nagano_soup.find_all('td')[15].find_all(text=True, recursive=True)
raw_na_gov = nagano_soup.find_all('td')[10].find_all(text=True, recursive=True)
raw_na_ar = nagano_soup.find_all('td')[12].find_all(text=True, recursive=True)
raw_na_pr = nagano_soup.find_all('td')[14].find_all(text=True, recursive=True)
nagano_area_rank = int(raw_na_ar[0].replace('th', ''))
nagano_pop_rank = int(raw_na_pr[0].replace('th', '')) 
nagano_governor = f"{raw_na_gov[0]}"
nagano_population = f"{raw_na_pop[0]}"
nagano_density = f"{raw_na_den[0]}{raw_na_den[1]}"
nagano_density_mi = f"{raw_na_den[2].replace('(', '').replace(')', '')}"
nagano_density_mi = nagano_density_mi.strip()

gifu_page = requests.get('https://en.wikipedia.org/wiki/Gifu_prefecture')
gifu_soup = BeautifulSoup(gifu_page.text, 'html.parser')
raw_gi_pop = gifu_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_gi_den = gifu_soup.find_all('td')[15].find_all(text=True, recursive=True)
raw_gi_gov = gifu_soup.find_all('td')[10].find_all(text=True, recursive=True)
raw_gi_ar = gifu_soup.find_all('td')[12].find_all(text=True, recursive=True)
raw_gi_pr = gifu_soup.find_all('td')[14].find_all(text=True, recursive=True)
gifu_area_rank = int(raw_gi_ar[0].replace('th', ''))
gifu_pop_rank = int(raw_gi_pr[0].replace('th', '')) 
gifu_governor = f"{raw_gi_gov[0]}"
gifu_population = f"{raw_gi_pop[0]}"
gifu_density = f"{raw_gi_den[0]}{raw_gi_den[1]}"
gifu_density_mi = f"{raw_gi_den[2].replace('(', '').replace(')', '')}"
gifu_density_mi = gifu_density_mi.strip()

shizuoka_page = requests.get('https://en.wikipedia.org/wiki/Shizuoka_prefecture')
shizuoka_soup = BeautifulSoup(shizuoka_page.text, 'html.parser')
raw_shi_pop = shizuoka_soup.find_all('td')[16].find_all(text=True, recursive=True)
raw_shi_den = shizuoka_soup.find_all('td')[18].find_all(text=True, recursive=True)
raw_shi_gov = shizuoka_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_shi_ar = shizuoka_soup.find_all('td')[15].find_all(text=True, recursive=True)
raw_shi_pr = shizuoka_soup.find_all('td')[17].find_all(text=True, recursive=True)
shizuoka_area_rank = int(raw_shi_ar[0].replace('th', ''))
shizuoka_pop_rank = int(raw_shi_pr[0].replace('th', '')) 
shizuoka_governor = f"{raw_shi_gov[0]}"
shizuoka_population = f"{raw_shi_pop[0]}"
shizuoka_density = f"{raw_shi_den[0]}{raw_shi_den[1]}"
shizuoka_density_mi = f"{raw_shi_den[2].replace('(', '').replace(')', '')}"
shizuoka_density_mi = shizuoka_density_mi.strip()

aichi_page = requests.get('https://en.wikipedia.org/wiki/Aichi_prefecture')
aichi_soup = BeautifulSoup(aichi_page.text, 'html.parser')
raw_ai_pop = aichi_soup.find_all('td')[15].find_all(text=True, recursive=True)
raw_ai_den = aichi_soup.find_all('td')[17].find_all(text=True, recursive=True)
raw_ai_gov = aichi_soup.find_all('td')[12].find_all(text=True, recursive=True)
raw_ai_ar = aichi_soup.find_all('td')[14].find_all(text=True, recursive=True)
raw_ai_pr = aichi_soup.find_all('td')[16].find_all(text=True, recursive=True)
aichi_area_rank = int(raw_ai_ar[0].replace('th', ''))
aichi_pop_rank = int(raw_ai_pr[0].replace('th', '')) 
aichi_governor = f"{raw_ai_gov[0]}"
aichi_population = f"{raw_ai_pop[0]}"
aichi_density = f"{raw_ai_den[0]}{raw_ai_den[1]}"
aichi_density_mi = f"{raw_ai_den[2].replace('(', '').replace(')', '')}"
aichi_density_mi = aichi_density_mi.strip()

mie_page = requests.get('https://en.wikipedia.org/wiki/Mie_prefecture')
mie_soup = BeautifulSoup(mie_page.text, 'html.parser')
raw_mie_pop = mie_soup.find_all('td')[14].find_all(text=True, recursive=True)
raw_mie_den = mie_soup.find_all('td')[16].find_all(text=True, recursive=True)
raw_mie_gov = mie_soup.find_all('td')[11].find_all(text=True, recursive=True)
raw_mie_ar = mie_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_mie_pr = mie_soup.find_all('td')[15].find_all(text=True, recursive=True)
mie_area_rank = int(raw_mie_ar[0].replace('th', ''))
mie_pop_rank = int(raw_mie_pr[0].replace('nd', '')) 
mie_governor = f"{raw_mie_gov[0]}"
mie_population = f"{raw_mie_pop[0]}"
mie_density = f"{raw_mie_den[0]}{raw_mie_den[1]}"
mie_density_mi = f"{raw_mie_den[2].replace('(', '').replace(')', '')}"
mie_density_mi = mie_density_mi.strip()

shiga_page = requests.get('https://en.wikipedia.org/wiki/Shiga_prefecture')
shiga_soup = BeautifulSoup(shiga_page.text, 'html.parser')
raw_shig_pop = shiga_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_shig_den = shiga_soup.find_all('td')[15].find_all(text=True, recursive=True)
raw_shig_gov = shiga_soup.find_all('td')[10].find_all(text=True, recursive=True)
raw_shig_ar = shiga_soup.find_all('td')[12].find_all(text=True, recursive=True)
raw_shig_pr = shiga_soup.find_all('td')[14].find_all(text=True, recursive=True)
shiga_area_rank = int(raw_shig_ar[0].replace('th', ''))
shiga_pop_rank = int(raw_shig_pr[0].replace('th', '')) 
shiga_governor = f"{raw_shig_gov[0]}"
shiga_population = f"{raw_shig_pop[0]}"
shiga_density = f"{raw_shig_den[0]}{raw_shig_den[1]}"
shiga_density_mi = f"{raw_shig_den[2].replace('(', '').replace(')', '')}"
shiga_density_mi = shiga_density_mi.strip()

kyoto_page = requests.get('https://en.wikipedia.org/wiki/Kyoto_prefecture')
kyoto_soup = BeautifulSoup(kyoto_page.text, 'html.parser')
raw_ky_pop = kyoto_soup.find_all('td')[15].find_all(text=True, recursive=True)
raw_ky_den = kyoto_soup.find_all('td')[17].find_all(text=True, recursive=True)
raw_ky_gov = kyoto_soup.find_all('td')[12].find_all(text=True, recursive=True)
raw_ky_ar = kyoto_soup.find_all('td')[14].find_all(text=True, recursive=True)
raw_ky_pr = kyoto_soup.find_all('td')[16].find_all(text=True, recursive=True)
kyoto_area_rank = int(raw_ky_ar[0].replace('st', ''))
kyoto_pop_rank = int(raw_ky_pr[0].replace('th', '')) 
kyoto_governor = f"{raw_ky_gov[0]}"
kyoto_population = f"{raw_ky_pop[0]}"
kyoto_density = f"{raw_ky_den[0]}{raw_ky_den[1]}"
kyoto_density_mi = f"{raw_ky_den[2].replace('(', '').replace(')', '')}"
kyoto_density_mi = kyoto_density_mi.strip()

osaka_page = requests.get('https://en.wikipedia.org/wiki/Osaka_prefecture')
osaka_soup = BeautifulSoup(osaka_page.text, 'html.parser')
raw_os_pop = osaka_soup.find_all('td')[14].find_all(text=True, recursive=True)
raw_os_den = osaka_soup.find_all('td')[16].find_all(text=True, recursive=True)
raw_os_gov = osaka_soup.find_all('td')[11].find_all(text=True, recursive=True)
raw_os_ar = osaka_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_os_pr = osaka_soup.find_all('td')[15].find_all(text=True, recursive=True)
osaka_area_rank = int(raw_os_ar[0].replace('th', ''))
osaka_pop_rank = int(raw_os_pr[0].replace('rd', '')) 
osaka_governor = f"{raw_os_gov[0]}"
osaka_population = f"{raw_os_pop[0]}"
osaka_density = f"{raw_os_den[0]}{raw_os_den[1]}"
osaka_density_mi = f"{raw_os_den[2].replace('(', '').replace(')', '')}"
osaka_density_mi = osaka_density_mi.strip()

hyogo_page = requests.get('https://en.wikipedia.org/wiki/Hyogo_prefecture')
hyogo_soup = BeautifulSoup(hyogo_page.text, 'html.parser')
raw_hy_pop = hyogo_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_hy_den = hyogo_soup.find_all('td')[15].find_all(text=True, recursive=True)
raw_hy_gov = hyogo_soup.find_all('td')[10].find_all(text=True, recursive=True)
raw_hy_ar = hyogo_soup.find_all('td')[12].find_all(text=True, recursive=True)
raw_hy_pr = hyogo_soup.find_all('td')[14].find_all(text=True, recursive=True)
hyogo_area_rank = int(raw_hy_ar[0].replace('th', ''))
hyogo_pop_rank = int(raw_hy_pr[0].replace('th', '')) 
hyogo_governor = f"{raw_hy_gov[0]}"
hyogo_population = f"{raw_hy_pop[0]}"
hyogo_density = f"{raw_hy_den[0]}{raw_hy_den[1]}"
hyogo_density_mi = f"{raw_hy_den[2].replace('(', '').replace(')', '')}"
hyogo_density_mi = hyogo_density_mi.strip()

nara_page = requests.get('https://en.wikipedia.org/wiki/Nara_prefecture')
nara_soup = BeautifulSoup(nara_page.text, 'html.parser')
raw_nar_pop = nara_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_nar_den = nara_soup.find_all('td')[15].find_all(text=True, recursive=True)
raw_nar_gov = nara_soup.find_all('td')[10].find_all(text=True, recursive=True)
raw_nar_ar = nara_soup.find_all('td')[12].find_all(text=True, recursive=True)
raw_nar_pr = nara_soup.find_all('td')[14].find_all(text=True, recursive=True)
nara_area_rank = int(raw_nar_ar[0].replace('th', ''))
nara_pop_rank = int(raw_nar_pr[0].replace('th', '')) 
nara_governor = f"{raw_nar_gov[0]}"
nara_population = f"{raw_nar_pop[0]}"
nara_density = f"{raw_nar_den[0]}{raw_nar_den[1]}"
nara_density_mi = f"{raw_nar_den[2].replace('(', '').replace(')', '')}"
nara_density_mi = nara_density_mi.strip()

wakayama_page = requests.get('https://en.wikipedia.org/wiki/Wakayama_prefecture')
wakayama_soup = BeautifulSoup(wakayama_page.text, 'html.parser')
raw_wa_pop = wakayama_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_wa_den = wakayama_soup.find_all('td')[15].find_all(text=True, recursive=True)
raw_wa_gov = wakayama_soup.find_all('td')[10].find_all(text=True, recursive=True)
raw_wa_ar = wakayama_soup.find_all('td')[12].find_all(text=True, recursive=True)
raw_wa_pr = wakayama_soup.find_all('td')[14].find_all(text=True, recursive=True)
wakayama_area_rank = int(raw_wa_ar[0].replace('th', ''))
wakayama_pop_rank = int(raw_wa_pr[0].replace('th', '')) 
wakayama_governor = f"{raw_wa_gov[0]}"
wakayama_population = f"{raw_wa_pop[0]}"
wakayama_density = f"{raw_wa_den[0]}{raw_wa_den[1]}"
wakayama_density_mi = f"{raw_wa_den[2].replace('(', '').replace(')', '')}"
wakayama_density_mi = wakayama_density_mi.strip()

tottori_page = requests.get('https://en.wikipedia.org/wiki/Tottori_prefecture')
tottori_soup = BeautifulSoup(tottori_page.text, 'html.parser')
raw_tot_pop = tottori_soup.find_all('td')[14].find_all(text=True, recursive=True)
raw_tot_den = tottori_soup.find_all('td')[16].find_all(text=True, recursive=True)
raw_tot_gov = tottori_soup.find_all('td')[11].find_all(text=True, recursive=True)
raw_tot_ar = tottori_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_tot_pr = tottori_soup.find_all('td')[15].find_all(text=True, recursive=True)
tottori_area_rank = int(raw_tot_ar[0].replace('st', ''))
tottori_pop_rank = int(raw_tot_pr[0].replace('th', '')) 
tottori_governor = f"{raw_tot_gov[0]}"
tottori_population = f"{raw_tot_pop[0]}"
tottori_density = f"{raw_tot_den[0]}{raw_tot_den[1]}"
tottori_density_mi = f"{raw_tot_den[2].replace('(', '').replace(')', '')}"
tottori_density_mi = tottori_density_mi.strip()

shimane_page = requests.get('https://en.wikipedia.org/wiki/Shimane_prefecture')
shimane_soup = BeautifulSoup(shimane_page.text, 'html.parser')
raw_shim_pop = shimane_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_shim_den = shimane_soup.find_all('td')[15].find_all(text=True, recursive=True)
raw_shim_gov = shimane_soup.find_all('td')[10].find_all(text=True, recursive=True)
raw_shim_ar = shimane_soup.find_all('td')[12].find_all(text=True, recursive=True)
raw_shim_pr = shimane_soup.find_all('td')[14].find_all(text=True, recursive=True)
shimane_area_rank = int(raw_shim_ar[0].replace('th', ''))
shimane_pop_rank = int(raw_shim_pr[0].replace('th', '')) 
shimane_governor = f"{raw_shim_gov[0]}"
shimane_population = f"{raw_shim_pop[0]}"
shimane_density = f"{raw_shim_den[0]}{raw_shim_den[1]}"
shimane_density_mi = f"{raw_shim_den[2].replace('(', '').replace(')', '')}"
shimane_density_mi = shimane_density_mi.strip()

okayama_page = requests.get('https://en.wikipedia.org/wiki/Okayama_prefecture')
okayama_soup = BeautifulSoup(okayama_page.text, 'html.parser')
raw_ok_pop = okayama_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_ok_den = okayama_soup.find_all('td')[15].find_all(text=True, recursive=True)
raw_ok_gov = okayama_soup.find_all('td')[10].find_all(text=True, recursive=True)
raw_ok_ar = okayama_soup.find_all('td')[12].find_all(text=True, recursive=True)
raw_ok_pr = okayama_soup.find_all('td')[14].find_all(text=True, recursive=True)
okayama_area_rank = int(raw_ok_ar[0].replace('th', ''))
okayama_pop_rank = int(raw_ok_pr[0].replace('st', '')) 
okayama_governor = f"{raw_ok_gov[0]}"
okayama_population = f"{raw_ok_pop[0]}"
okayama_density = f"{raw_ok_den[0]}{raw_ok_den[1]}"
okayama_density_mi = f"{raw_ok_den[2].replace('(', '').replace(')', '')}"
okayama_density_mi = okayama_density_mi.strip()

hiroshima_page = requests.get('https://en.wikipedia.org/wiki/Hiroshima_prefecture')
hiroshima_soup = BeautifulSoup(hiroshima_page.text, 'html.parser')
raw_hi_pop = hiroshima_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_hi_den = hiroshima_soup.find_all('td')[15].find_all(text=True, recursive=True)
raw_hi_gov = hiroshima_soup.find_all('td')[10].find_all(text=True, recursive=True)
raw_hi_ar = hiroshima_soup.find_all('td')[12].find_all(text=True, recursive=True)
raw_hi_pr = hiroshima_soup.find_all('td')[14].find_all(text=True, recursive=True)
hiroshima_area_rank = int(raw_hi_ar[0].replace('th', ''))
hiroshima_pop_rank = int(raw_hi_pr[0].replace('th', '')) 
hiroshima_governor = f"{raw_hi_gov[0]}"
hiroshima_population = f"{raw_hi_pop[0]}"
hiroshima_density = f"{raw_hi_den[0]}{raw_hi_den[1]}"
hiroshima_density_mi = f"{raw_hi_den[2].replace('(', '').replace(')', '')}"
hiroshima_density_mi = hiroshima_density_mi.strip()

yamaguchi_page = requests.get('https://en.wikipedia.org/wiki/Yamaguchi_prefecture')
yamaguchi_soup = BeautifulSoup(yamaguchi_page.text, 'html.parser')
raw_yama_pop = yamaguchi_soup.find_all('td')[14].find_all(text=True, recursive=True)
raw_yama_den = yamaguchi_soup.find_all('td')[16].find_all(text=True, recursive=True)
raw_yama_gov = yamaguchi_soup.find_all('td')[11].find_all(text=True, recursive=True)
raw_yama_ar = yamaguchi_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_yama_pr = yamaguchi_soup.find_all('td')[15].find_all(text=True, recursive=True)
yamaguchi_area_rank = int(raw_yama_ar[0].replace('rd', ''))
yamaguchi_pop_rank = int(raw_yama_pr[0].replace('th', '')) 
yamaguchi_governor = f"{raw_mi_gov[0]}"
yamaguchi_population = f"{raw_yama_pop[0]}"
yamaguchi_density = f"{raw_yama_den[0]}{raw_yama_den[1]}"
yamaguchi_density_mi = f"{raw_yama_den[2].replace('(', '').replace(')', '')}"
yamaguchi_density_mi = yamaguchi_density_mi.strip()

tokushima_page = requests.get('https://en.wikipedia.org/wiki/Tokushima_prefecture')
tokushima_soup = BeautifulSoup(tokushima_page.text, 'html.parser')
raw_toku_pop = tokushima_soup.find_all('td')[16].find_all(text=True, recursive=True)
raw_toku_den = tokushima_soup.find_all('td')[18].find_all(text=True, recursive=True)
raw_toku_gov = tokushima_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_toku_ar = tokushima_soup.find_all('td')[15].find_all(text=True, recursive=True)
raw_toku_pr = tokushima_soup.find_all('td')[17].find_all(text=True, recursive=True)
tokushima_area_rank = int(raw_toku_ar[0].replace('th', ''))
tokushima_pop_rank = int(raw_toku_pr[0].replace('th', '')) 
tokushima_governor = f"{raw_toku_gov[0]}"
tokushima_population = f"{raw_toku_pop[0]}"
tokushima_density = f"{raw_toku_den[0]}{raw_toku_den[1]}"
tokushima_density_mi = f"{raw_toku_den[2].replace('(', '').replace(')', '')}"
tokushima_density_mi = tokushima_density_mi.strip()

kagawa_page = requests.get('https://en.wikipedia.org/wiki/Kagawa_prefecture')
kagawa_soup = BeautifulSoup(kagawa_page.text, 'html.parser')
raw_kag_pop = kagawa_soup.find_all('td')[15].find_all(text=True, recursive=True)
raw_kag_den = kagawa_soup.find_all('td')[17].find_all(text=True, recursive=True)
raw_kag_gov = kagawa_soup.find_all('td')[12].find_all(text=True, recursive=True)
raw_kag_ar = kagawa_soup.find_all('td')[14].find_all(text=True, recursive=True)
raw_kag_pr = kagawa_soup.find_all('td')[16].find_all(text=True, recursive=True)
kagawa_area_rank = int(raw_kag_ar[0].replace('th', ''))
kagawa_pop_rank = int(raw_kag_pr[0].replace('th', '')) 
kagawa_governor = f"{raw_kag_gov[0]}"
kagawa_population = f"{raw_kag_pop[0]}"
kagawa_density = f"{raw_kag_den[0]}{raw_kag_den[1]}"
kagawa_density_mi = f"{raw_kag_den[2].replace('(', '').replace(')', '')}"
kagawa_density_mi = kagawa_density_mi.strip()

ehime_page = requests.get('https://en.wikipedia.org/wiki/Ehime_prefecture')
ehime_soup = BeautifulSoup(ehime_page.text, 'html.parser')
raw_eh_pop = ehime_soup.find_all('td')[15].find_all(text=True, recursive=True)
raw_eh_den = ehime_soup.find_all('td')[17].find_all(text=True, recursive=True)
raw_eh_gov = ehime_soup.find_all('td')[12].find_all(text=True, recursive=True)
raw_eh_ar = ehime_soup.find_all('td')[14].find_all(text=True, recursive=True)
raw_eh_pr = ehime_soup.find_all('td')[16].find_all(text=True, recursive=True)
ehime_area_rank = int(raw_eh_ar[0].replace('th', ''))
ehime_pop_rank = int(raw_eh_pr[0].replace('th', '')) 
ehime_governor = f"{raw_eh_gov[0]}"
ehime_population = f"{raw_eh_pop[0]}"
ehime_density = f"{raw_eh_den[0]}{raw_eh_den[1]}"
ehime_density_mi = f"{raw_eh_den[2].replace('(', '').replace(')', '')}"
ehime_density_mi = ehime_density_mi.strip()

kochi_page = requests.get('https://en.wikipedia.org/wiki/Kochi_prefecture')
kochi_soup = BeautifulSoup(kochi_page.text, 'html.parser')
raw_ko_pop = kochi_soup.find_all('td')[16].find_all(text=True, recursive=True)
raw_ko_den = kochi_soup.find_all('td')[18].find_all(text=True, recursive=True)
raw_ko_gov = kochi_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_ko_ar = kochi_soup.find_all('td')[15].find_all(text=True, recursive=True)
raw_ko_pr = kochi_soup.find_all('td')[17].find_all(text=True, recursive=True)
kochi_area_rank = int(raw_ko_ar[0].replace('th', ''))
kochi_pop_rank = int(raw_ko_pr[0].replace('th', '')) 
kochi_governor = f"{raw_ko_gov[0]}"
kochi_population = f"{raw_ko_pop[0]}"
kochi_density = f"{raw_ko_den[0]}{raw_ko_den[1]}"
kochi_density_mi = f"{raw_ko_den[2].replace('(', '').replace(')', '')}"
kochi_density_mi = kochi_density_mi.strip()

fukuoka_page = requests.get('https://en.wikipedia.org/wiki/Fukuoka_prefecture')
fukuoka_soup = BeautifulSoup(fukuoka_page.text, 'html.parser')
raw_fuku_pop = fukuoka_soup.find_all('td')[16].find_all(text=True, recursive=True)
raw_fuku_den = fukuoka_soup.find_all('td')[18].find_all(text=True, recursive=True)
raw_fuku_gov = fukuoka_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_fuku_ar = fukuoka_soup.find_all('td')[15].find_all(text=True, recursive=True)
raw_fuku_pr = fukuoka_soup.find_all('td')[17].find_all(text=True, recursive=True)
fukuoka_area_rank = int(raw_fuku_ar[0].replace('th', ''))
fukuoka_pop_rank = int(raw_fuku_pr[0].replace('th', '')) 
fukuoka_governor = f"{raw_fuku_gov[0]}"
fukuoka_population = f"{raw_fuku_pop[0]}"
fukuoka_density = f"{raw_fuku_den[0]}{raw_fuku_den[1]}"
fukuoka_density_mi = f"{raw_fuku_den[2].replace('(', '').replace(')', '')}"
fukuoka_density_mi = fukuoka_density_mi.strip()

saga_page = requests.get('https://en.wikipedia.org/wiki/Saga_prefecture')
saga_soup = BeautifulSoup(saga_page.text, 'html.parser')
raw_sag_pop = saga_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_sag_den = saga_soup.find_all('td')[15].find_all(text=True, recursive=True)
raw_sag_gov = saga_soup.find_all('td')[10].find_all(text=True, recursive=True)
raw_sag_ar = saga_soup.find_all('td')[12].find_all(text=True, recursive=True)
raw_sag_pr = saga_soup.find_all('td')[14].find_all(text=True, recursive=True)
saga_area_rank = int(raw_sag_ar[0].replace('nd', ''))
saga_pop_rank = int(raw_sag_pr[0].replace('nd', '')) 
saga_governor = f"{raw_sag_gov[0]}"
saga_population = f"{raw_sag_pop[0]}"
saga_density = f"{raw_sag_den[0]}{raw_sag_den[1]}"
saga_density_mi = f"{raw_sag_den[2].replace('(', '').replace(')', '')}"
saga_density_mi = saga_density_mi.strip()

nagasaki_page = requests.get('https://en.wikipedia.org/wiki/Nagasaki_prefecture')
nagasaki_soup = BeautifulSoup(nagasaki_page.text, 'html.parser')
raw_nag_pop = nagasaki_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_nag_den = nagasaki_soup.find_all('td')[15].find_all(text=True, recursive=True)
raw_nag_gov = nagasaki_soup.find_all('td')[10].find_all(text=True, recursive=True)
raw_nag_ar = nagasaki_soup.find_all('td')[12].find_all(text=True, recursive=True)
raw_nag_pr = nagasaki_soup.find_all('td')[14].find_all(text=True, recursive=True)
nagasaki_area_rank = int(raw_nag_ar[0].replace('th', ''))
nagasaki_pop_rank = int(raw_nag_pr[0].replace('th', '')) 
nagasaki_governor = f"{raw_nag_gov[0]}"
nagasaki_population = f"{raw_nag_pop[0]}"
nagasaki_density = f"{raw_nag_den[0]}{raw_nag_den[1]}"
nagasaki_density_mi = f"{raw_nag_den[2].replace('(', '').replace(')', '')}"
nagasaki_density_mi = nagasaki_density_mi.strip()

kumamoto_page = requests.get('https://en.wikipedia.org/wiki/Kumamoto_prefecture')
kumamoto_soup = BeautifulSoup(kumamoto_page.text, 'html.parser')
raw_ku_pop = kumamoto_soup.find_all('td')[14].find_all(text=True, recursive=True)
raw_ku_den = kumamoto_soup.find_all('td')[16].find_all(text=True, recursive=True)
raw_ku_gov = kumamoto_soup.find_all('td')[11].find_all(text=True, recursive=True)
raw_ku_ar = kumamoto_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_ku_pr = kumamoto_soup.find_all('td')[15].find_all(text=True, recursive=True)
kumamoto_area_rank = int(raw_ku_ar[0].replace('th', ''))
kumamoto_pop_rank = int(raw_ku_pr[0].replace('rd', '')) 
kumamoto_governor = f"{raw_ku_gov[0]}"
kumamoto_population = f"{raw_ku_pop[0]}"
kumamoto_density = f"{raw_ku_den[0]}{raw_ku_den[1]}"
kumamoto_density_mi = f"{raw_ku_den[2].replace('(', '').replace(')', '')}"
kumamoto_density_mi = kumamoto_density_mi.strip()

oita_page = requests.get('https://en.wikipedia.org/wiki/Oita_prefecture')
oita_soup = BeautifulSoup(oita_page.text, 'html.parser')
raw_oi_pop = oita_soup.find_all('td')[14].find_all(text=True, recursive=True)
raw_oi_den = oita_soup.find_all('td')[16].find_all(text=True, recursive=True)
raw_oi_gov = oita_soup.find_all('td')[11].find_all(text=True, recursive=True)
raw_oi_ar = oita_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_oi_pr = oita_soup.find_all('td')[15].find_all(text=True, recursive=True)
oita_area_rank = int(raw_oi_ar[0].replace('nd', ''))
oita_pop_rank = int(raw_oi_pr[0].replace('rd', '')) 
oita_governor = f"{raw_oi_gov[0]}"
oita_population = f"{raw_oi_pop[0]}"
oita_density = f"{raw_oi_den[0]}{raw_oi_den[1]}"
oita_density_mi = f"{raw_oi_den[2].replace('(', '').replace(')', '')}"
oita_density_mi = oita_density_mi.strip()

miyazaki_page = requests.get('https://en.wikipedia.org/wiki/Miyazaki_prefecture')
miyazaki_soup = BeautifulSoup(miyazaki_page.text, 'html.parser')
raw_miya_pop = miyazaki_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_miya_den = miyazaki_soup.find_all('td')[15].find_all(text=True, recursive=True)
raw_miya_gov = miyazaki_soup.find_all('td')[10].find_all(text=True, recursive=True)
raw_miya_ar = miyazaki_soup.find_all('td')[12].find_all(text=True, recursive=True)
raw_miya_pr = miyazaki_soup.find_all('td')[14].find_all(text=True, recursive=True)
miyazaki_area_rank = int(raw_miya_ar[0].replace('th', ''))
miyazaki_pop_rank = int(raw_miya_pr[0].replace('th', '')) 
miyazaki_governor = f"{raw_miya_gov[0]}"
miyazaki_population = f"{raw_miya_pop[0]}"
miyazaki_density = f"{raw_miya_den[0]}{raw_miya_den[1]}"
miyazaki_density_mi = f"{raw_miya_den[2].replace('(', '').replace(')', '')}"
miyazaki_density_mi = miyazaki_density_mi.strip()

kagoshima_page = requests.get('https://en.wikipedia.org/wiki/Kagoshima_prefecture')
kagoshima_soup = BeautifulSoup(kagoshima_page.text, 'html.parser')
raw_kago_pop = kagoshima_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_kago_den = kagoshima_soup.find_all('td')[15].find_all(text=True, recursive=True)
raw_kago_gov = kagoshima_soup.find_all('td')[10].find_all(text=True, recursive=True)
raw_kago_ar = kagoshima_soup.find_all('td')[12].find_all(text=True, recursive=True)
raw_kago_pr = kagoshima_soup.find_all('td')[14].find_all(text=True, recursive=True)
kagoshima_area_rank = int(raw_kago_ar[0].replace('th', ''))
kagoshima_pop_rank = int(raw_kago_pr[0].replace('th', '')) 
kagoshima_governor = f"{raw_kago_gov[0]}"
kagoshima_population = f"{raw_kago_pop[0]}"
kagoshima_density = f"{raw_kago_den[0]}{raw_kago_den[1]}"
kagoshima_density_mi = f"{raw_kago_den[2].replace('(', '').replace(')', '')}"
kagoshima_density_mi = kagoshima_density_mi.strip()

okinawa_page = requests.get('https://en.wikipedia.org/wiki/Okinawa_prefecture')
okinawa_soup = BeautifulSoup(okinawa_page.text, 'html.parser')
raw_oki_pop = okinawa_soup.find_all('td')[15].find_all(text=True, recursive=True)
raw_oki_den = okinawa_soup.find_all('td')[17].find_all(text=True, recursive=True)
raw_oki_gov = okinawa_soup.find_all('td')[12].find_all(text=True, recursive=True)
raw_oki_ar = okinawa_soup.find_all('td')[14].find_all(text=True, recursive=True)
raw_oki_pr = okinawa_soup.find_all('td')[16].find_all(text=True, recursive=True)
okinawa_area_rank = int(raw_oki_ar[0].replace('th', ''))
okinawa_pop_rank = int(raw_oki_pr[0].replace('th', '')) 
okinawa_governor = f"{raw_oki_gov[0]}"
okinawa_population = f"{raw_oki_pop[0]}"
okinawa_density = f"{raw_oki_den[0]}{raw_oki_den[1]}"
okinawa_density_mi = f"{raw_oki_den[2].replace('(', '').replace(')', '')}"
okinawa_density_mi = okinawa_density_mi.strip()
