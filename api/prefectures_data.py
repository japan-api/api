import requests
from bs4 import BeautifulSoup

hokkaido_page = requests.get('https://en.wikipedia.org/wiki/Hokkaido')
hokkaido_soup = BeautifulSoup(hokkaido_page.text, 'html.parser')
raw_hok_pop = hokkaido_soup.find_all('td')[14].find_all(text=True, recursive=True)
raw_hok_den = hokkaido_soup.find_all('td')[16].find_all(text=True, recursive=True)
hokkaido_population = f"{raw_hok_pop[0]}"
hokkaido_density = f"{raw_hok_den[0]}{raw_hok_den[1]}"
hokkaido_density_mi = f"{raw_hok_den[2].replace('(', '').replace(')', '')}"
hokkaido_density_mi = hokkaido_density_mi.strip()

aomori_page = requests.get('https://en.wikipedia.org/wiki/Aomori_prefecture')
aomori_soup = BeautifulSoup(aomori_page.text, 'html.parser')
raw_ao_pop = aomori_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_ao_den = aomori_soup.find_all('td')[15].find_all(text=True, recursive=True)
aomori_population = f"{raw_ao_pop[0]}"
aomori_density = f"{raw_ao_den[0]}{raw_ao_den[1]}"
aomori_density_mi = f"{raw_ao_den[2].replace('(', '').replace(')', '')}"
aomori_density_mi = aomori_density_mi.strip()

iwate_page = requests.get('https://en.wikipedia.org/wiki/Iwate_prefecture')
iwate_soup = BeautifulSoup(iwate_page.text, 'html.parser')
raw_iw_pop = iwate_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_iw_den = iwate_soup.find_all('td')[15].find_all(text=True, recursive=True)
iwate_population = f"{raw_iw_pop[0]}"
iwate_density = f"{raw_iw_den[0]}{raw_iw_den[1]}"
iwate_density_mi = f"{raw_iw_den[2].replace('(', '').replace(')', '')}"
iwate_density_mi = iwate_density_mi.strip()

miyagi_page = requests.get('https://en.wikipedia.org/wiki/Miyagi_prefecture')
miyagi_soup = BeautifulSoup(miyagi_page.text, 'html.parser')
raw_mi_pop = miyagi_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_mi_den = miyagi_soup.find_all('td')[15].find_all(text=True, recursive=True)
miyagi_population = f"{raw_mi_pop[0]}"
miyagi_density = f"{raw_mi_den[0]}{raw_mi_den[1]}"
miyagi_density_mi = f"{raw_mi_den[2].replace('(', '').replace(')', '')}"
miyagi_density_mi = miyagi_density_mi.strip()

akita_page = requests.get('https://en.wikipedia.org/wiki/Akita_prefecture')
akita_soup = BeautifulSoup(akita_page.text, 'html.parser')
raw_ak_pop = akita_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_ak_den = akita_soup.find_all('td')[15].find_all(text=True, recursive=True)
akita_population = f"{raw_ak_pop[0]}"
akita_density = f"{raw_ak_den[0]}{raw_ak_den[1]}"
akita_density_mi = f"{raw_ak_den[2].replace('(', '').replace(')', '')}"
akita_density_mi = akita_density_mi.strip()

yamagata_page = requests.get('https://en.wikipedia.org/wiki/Yamagata_prefecture')
yamagata_soup = BeautifulSoup(yamagata_page.text, 'html.parser')
raw_ya_pop = yamagata_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_ya_den = yamagata_soup.find_all('td')[15].find_all(text=True, recursive=True)
yamagata_population = f"{raw_ya_pop[0]}"
yamagata_density = f"{raw_ya_den[0]}{raw_ya_den[1]}"
yamagata_density_mi = f"{raw_ya_den[2].replace('(', '').replace(')', '')}"
yamagata_density_mi = yamagata_density_mi.strip()

fukushima_page = requests.get('https://en.wikipedia.org/wiki/Fukushima_prefecture')
fukushima_soup = BeautifulSoup(fukushima_page.text, 'html.parser')
raw_fu_pop = fukushima_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_fu_den = fukushima_soup.find_all('td')[15].find_all(text=True, recursive=True)
fukushima_population = f"{raw_fu_pop[0]}"
fukushima_density = f"{raw_fu_den[0]}{raw_fu_den[1]}"
fukushima_density_mi = f"{raw_fu_den[2].replace('(', '').replace(')', '')}"
fukushima_density_mi = fukushima_density_mi.strip()

ibaraki_page = requests.get('https://en.wikipedia.org/wiki/Ibaraki_prefecture')
ibaraki_soup = BeautifulSoup(ibaraki_page.text, 'html.parser')
raw_ib_pop = ibaraki_soup.find_all('td')[15].find_all(text=True, recursive=True)
raw_ib_den = ibaraki_soup.find_all('td')[17].find_all(text=True, recursive=True)
ibaraki_population = f"{raw_ib_pop[0]}"
ibaraki_density = f"{raw_ib_den[0]}{raw_ib_den[1]}"
ibaraki_density_mi = f"{raw_ib_den[2].replace('(', '').replace(')', '')}"
ibaraki_density_mi = ibaraki_density_mi.strip()

tochigi_page = requests.get('https://en.wikipedia.org/wiki/Tochigi_prefecture')
tochigi_soup = BeautifulSoup(tochigi_page.text, 'html.parser')
raw_to_pop = tochigi_soup.find_all('td')[15].find_all(text=True, recursive=True)
raw_to_den = tochigi_soup.find_all('td')[17].find_all(text=True, recursive=True)
tochigi_population = f"{raw_to_pop[0]}"
tochigi_density = f"{raw_to_den[0]}{raw_to_den[1]}"
tochigi_density_mi = f"{raw_to_den[2].replace('(', '').replace(')', '')}"
tochigi_density_mi = tochigi_density_mi.strip()

gunma_page = requests.get('https://en.wikipedia.org/wiki/Gunma_prefecture')
gunma_soup = BeautifulSoup(gunma_page.text, 'html.parser')
raw_gu_pop = gunma_soup.find_all('td')[15].find_all(text=True, recursive=True)
raw_gu_den = gunma_soup.find_all('td')[17].find_all(text=True, recursive=True)
gunma_population = f"{raw_gu_pop[0]}"
gunma_density = f"{raw_gu_den[0]}{raw_gu_den[1]}"
gunma_density_mi = f"{raw_gu_den[2].replace('(', '').replace(')', '')}"
gunma_density_mi = gunma_density_mi.strip()

saitama_page = requests.get('https://en.wikipedia.org/wiki/Saitama_prefecture')
saitama_soup = BeautifulSoup(saitama_page.text, 'html.parser')
raw_sa_pop = saitama_soup.find_all('td')[14].find_all(text=True, recursive=True)
raw_sa_den = saitama_soup.find_all('td')[16].find_all(text=True, recursive=True)
saitama_population = f"{raw_sa_pop[0]}"
saitama_density = f"{raw_sa_den[0]}{raw_sa_den[1]}"
saitama_density_mi = f"{raw_sa_den[2].replace('(', '').replace(')', '')}"
saitama_density_mi = saitama_density_mi.strip()

chiba_page = requests.get('https://en.wikipedia.org/wiki/Chiba_prefecture')
chiba_soup = BeautifulSoup(chiba_page.text, 'html.parser')
raw_chi_pop = chiba_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_chi_den = chiba_soup.find_all('td')[15].find_all(text=True, recursive=True)
chiba_population = f"{raw_chi_pop[0]}"
chiba_density = f"{raw_chi_den[0]}{raw_chi_den[1]}"
chiba_density_mi = f"{raw_chi_den[2].replace('(', '').replace(')', '')}"
chiba_density_mi = chiba_density_mi.strip()

tokyo_page = requests.get('https://en.wikipedia.org/wiki/Tokyo')
tokyo_soup = BeautifulSoup(tokyo_page.text, 'html.parser')
raw_tok_pop = tokyo_soup.find_all('td')[21].find_all(text=True, recursive=True)
raw_tok_den = tokyo_soup.find_all('td')[23].find_all(text=True, recursive=True)
tokyo_population = f"{raw_tok_pop[0]}"
tokyo_density = f"{raw_tok_den[0]}{raw_tok_den[1]}"
tokyo_density_mi = f"{raw_tok_den[2].replace('(', '').replace(')', '')}"
tokyo_density_mi = tokyo_density_mi.strip()

kanagawa_page = requests.get('https://en.wikipedia.org/wiki/Kanagawa_Prefecture')
kanagawa_soup = BeautifulSoup(kanagawa_page.text, 'html.parser')
raw_ka_pop = kanagawa_soup.find_all('td')[17].find_all(text=True, recursive=True)
raw_ka_den = kanagawa_soup.find_all('td')[19].find_all(text=True, recursive=True)
kanagawa_population = f"{raw_ka_pop[0]}"
kanagawa_density = f"{raw_ka_den[0]}{raw_ka_den[1]}"
kanagawa_density_mi = f"{raw_ka_den[2].replace('(', '').replace(')', '')}"
kanagawa_density_mi = kanagawa_density_mi.strip()

niigata_page = requests.get('https://en.wikipedia.org/wiki/Niigata_Prefecture')
niigata_soup = BeautifulSoup(niigata_page.text, 'html.parser')
raw_ni_pop = niigata_soup.find_all('td')[15].find_all(text=True, recursive=True)
raw_ni_den = niigata_soup.find_all('td')[17].find_all(text=True, recursive=True)
niigata_population = f"{raw_ni_pop[0]}"
niigata_density = f"{raw_ni_den[0]}{raw_ni_den[1]}"
niigata_density_mi = f"{raw_ni_den[2].replace('(', '').replace(')', '')}"
niigata_density_mi = niigata_density_mi.strip()

toyama_page = requests.get('https://en.wikipedia.org/wiki/Toyama_prefecture')
toyama_soup = BeautifulSoup(toyama_page.text, 'html.parser')
raw_toy_pop = toyama_soup.find_all('td')[16].find_all(text=True, recursive=True)
raw_toy_den = toyama_soup.find_all('td')[18].find_all(text=True, recursive=True)
toyama_population = f"{raw_toy_pop[0]}"
toyama_density = f"{raw_toy_den[0]}{raw_toy_den[1]}"
toyama_density_mi = f"{raw_toy_den[2].replace('(', '').replace(')', '')}"
toyama_density_mi = toyama_density_mi.strip()

ishikawa_page = requests.get('https://en.wikipedia.org/wiki/Ishikawa_prefecture')
ishikawa_soup = BeautifulSoup(ishikawa_page.text, 'html.parser')
raw_is_pop = ishikawa_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_is_den = ishikawa_soup.find_all('td')[15].find_all(text=True, recursive=True)
ishikawa_population = f"{raw_is_pop[0]}"
ishikawa_density = f"{raw_is_den[0]}{raw_is_den[1]}"
ishikawa_density_mi = f"{raw_is_den[2].replace('(', '').replace(')', '')}"
ishikawa_density_mi = ishikawa_density_mi.strip()

fukui_page = requests.get('https://en.wikipedia.org/wiki/Fukui_prefecture')
fukui_soup = BeautifulSoup(fukui_page.text, 'html.parser')
raw_fuk_pop = fukui_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_fuk_den = fukui_soup.find_all('td')[15].find_all(text=True, recursive=True)
fukui_population = f"{raw_fuk_pop[0]}"
fukui_density = f"{raw_fuk_den[0]}{raw_fuk_den[1]}"
fukui_density_mi = f"{raw_fuk_den[2].replace('(', '').replace(')', '')}"
fukui_density_mi = fukui_density_mi.strip()

yamanashi_page = requests.get('https://en.wikipedia.org/wiki/Yamanashi_prefecture')
yamanashi_soup = BeautifulSoup(yamanashi_page.text, 'html.parser')
raw_yam_pop = yamanashi_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_yam_den = yamanashi_soup.find_all('td')[15].find_all(text=True, recursive=True)
yamanashi_population = f"{raw_yam_pop[0]}"
yamanashi_density = f"{raw_yam_den[0]}{raw_yam_den[1]}"
yamanashi_density_mi = f"{raw_yam_den[2].replace('(', '').replace(')', '')}"
yamanashi_density_mi = yamanashi_density_mi.strip()

nagano_page = requests.get('https://en.wikipedia.org/wiki/Nagano_prefecture')
nagano_soup = BeautifulSoup(nagano_page.text, 'html.parser')
raw_na_pop = nagano_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_na_den = nagano_soup.find_all('td')[15].find_all(text=True, recursive=True)
nagano_population = f"{raw_na_pop[0]}"
nagano_density = f"{raw_na_den[0]}{raw_na_den[1]}"
nagano_density_mi = f"{raw_na_den[2].replace('(', '').replace(')', '')}"
nagano_density_mi = nagano_density_mi.strip()

gifu_page = requests.get('https://en.wikipedia.org/wiki/Gifu_prefecture')
gifu_soup = BeautifulSoup(gifu_page.text, 'html.parser')
raw_gi_pop = gifu_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_gi_den = gifu_soup.find_all('td')[15].find_all(text=True, recursive=True)
gifu_population = f"{raw_gi_pop[0]}"
gifu_density = f"{raw_gi_den[0]}{raw_gi_den[1]}"
gifu_density_mi = f"{raw_gi_den[2].replace('(', '').replace(')', '')}"
gifu_density_mi = gifu_density_mi.strip()

shizuoka_page = requests.get('https://en.wikipedia.org/wiki/Shizuoka_prefecture')
shizuoka_soup = BeautifulSoup(shizuoka_page.text, 'html.parser')
raw_shi_pop = shizuoka_soup.find_all('td')[15].find_all(text=True, recursive=True)
raw_shi_den = shizuoka_soup.find_all('td')[17].find_all(text=True, recursive=True)
shizuoka_population = f"{raw_shi_pop[0]}"
shizuoka_density = f"{raw_shi_den[0]}{raw_shi_den[1]}"
shizuoka_density_mi = f"{raw_shi_den[2].replace('(', '').replace(')', '')}"
shizuoka_density_mi = shizuoka_density_mi.strip()

aichi_page = requests.get('https://en.wikipedia.org/wiki/Aichi_prefecture')
aichi_soup = BeautifulSoup(aichi_page.text, 'html.parser')
raw_ai_pop = aichi_soup.find_all('td')[14].find_all(text=True, recursive=True)
raw_ai_den = aichi_soup.find_all('td')[16].find_all(text=True, recursive=True)
aichi_population = f"{raw_ai_pop[0]}"
aichi_density = f"{raw_ai_den[0]}{raw_ai_den[1]}"
aichi_density_mi = f"{raw_ai_den[2].replace('(', '').replace(')', '')}"
aichi_density_mi = aichi_density_mi.strip()

mie_page = requests.get('https://en.wikipedia.org/wiki/Mie_prefecture')
mie_soup = BeautifulSoup(mie_page.text, 'html.parser')
raw_mie_pop = mie_soup.find_all('td')[14].find_all(text=True, recursive=True)
raw_mie_den = mie_soup.find_all('td')[16].find_all(text=True, recursive=True)
mie_population = f"{raw_mie_pop[0]}"
mie_density = f"{raw_mie_den[0]}{raw_mie_den[1]}"
mie_density_mi = f"{raw_mie_den[2].replace('(', '').replace(')', '')}"
mie_density_mi = mie_density_mi.strip()

shiga_page = requests.get('https://en.wikipedia.org/wiki/Shiga_prefecture')
shiga_soup = BeautifulSoup(shiga_page.text, 'html.parser')
raw_shig_pop = shiga_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_shig_den = shiga_soup.find_all('td')[15].find_all(text=True, recursive=True)
shiga_population = f"{raw_shig_pop[0]}"
shiga_density = f"{raw_shig_den[0]}{raw_shig_den[1]}"
shiga_density_mi = f"{raw_shig_den[2].replace('(', '').replace(')', '')}"
shiga_density_mi = shiga_density_mi.strip()

kyoto_page = requests.get('https://en.wikipedia.org/wiki/Kyoto_prefecture')
kyoto_soup = BeautifulSoup(kyoto_page.text, 'html.parser')
raw_ky_pop = kyoto_soup.find_all('td')[14].find_all(text=True, recursive=True)
raw_ky_den = kyoto_soup.find_all('td')[16].find_all(text=True, recursive=True)
kyoto_population = f"{raw_ky_pop[0]}"
kyoto_density = f"{raw_ky_den[0]}{raw_ky_den[1]}"
kyoto_density_mi = f"{raw_ky_den[2].replace('(', '').replace(')', '')}"
kyoto_density_mi = kyoto_density_mi.strip()

osaka_page = requests.get('https://en.wikipedia.org/wiki/Osaka_prefecture')
osaka_soup = BeautifulSoup(osaka_page.text, 'html.parser')
raw_os_pop = osaka_soup.find_all('td')[14].find_all(text=True, recursive=True)
raw_os_den = osaka_soup.find_all('td')[16].find_all(text=True, recursive=True)
osaka_population = f"{raw_os_pop[0]}"
osaka_density = f"{raw_os_den[0]}{raw_os_den[1]}"
osaka_density_mi = f"{raw_os_den[2].replace('(', '').replace(')', '')}"
osaka_density_mi = osaka_density_mi.strip()

hyogo_page = requests.get('https://en.wikipedia.org/wiki/Hyogo_prefecture')
hyogo_soup = BeautifulSoup(hyogo_page.text, 'html.parser')
raw_hy_pop = hyogo_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_hy_den = hyogo_soup.find_all('td')[15].find_all(text=True, recursive=True)
hyogo_population = f"{raw_hy_pop[0]}"
hyogo_density = f"{raw_hy_den[0]}{raw_hy_den[1]}"
hyogo_density_mi = f"{raw_hy_den[2].replace('(', '').replace(')', '')}"
hyogo_density_mi = hyogo_density_mi.strip()

nara_page = requests.get('https://en.wikipedia.org/wiki/Nara_prefecture')
nara_soup = BeautifulSoup(nara_page.text, 'html.parser')
raw_nar_pop = nara_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_nar_den = nara_soup.find_all('td')[15].find_all(text=True, recursive=True)
nara_population = f"{raw_nar_pop[0]}"
nara_density = f"{raw_nar_den[0]}{raw_nar_den[1]}"
nara_density_mi = f"{raw_nar_den[2].replace('(', '').replace(')', '')}"
nara_density_mi = nara_density_mi.strip()

wakayama_page = requests.get('https://en.wikipedia.org/wiki/Wakayama_prefecture')
wakayama_soup = BeautifulSoup(wakayama_page.text, 'html.parser')
raw_wa_pop = wakayama_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_wa_den = wakayama_soup.find_all('td')[15].find_all(text=True, recursive=True)
wakayama_population = f"{raw_wa_pop[0]}"
wakayama_density = f"{raw_wa_den[0]}{raw_wa_den[1]}"
wakayama_density_mi = f"{raw_wa_den[2].replace('(', '').replace(')', '')}"
wakayama_density_mi = wakayama_density_mi.strip()

tottori_page = requests.get('https://en.wikipedia.org/wiki/Tottori_prefecture')
tottori_soup = BeautifulSoup(tottori_page.text, 'html.parser')
raw_tot_pop = tottori_soup.find_all('td')[14].find_all(text=True, recursive=True)
raw_tot_den = tottori_soup.find_all('td')[16].find_all(text=True, recursive=True)
tottori_population = f"{raw_tot_pop[0]}"
tottori_density = f"{raw_tot_den[0]}{raw_tot_den[1]}"
tottori_density_mi = f"{raw_tot_den[2].replace('(', '').replace(')', '')}"
tottori_density_mi = tottori_density_mi.strip()

shimane_page = requests.get('https://en.wikipedia.org/wiki/Shimane_prefecture')
shimane_soup = BeautifulSoup(shimane_page.text, 'html.parser')
raw_shim_pop = shimane_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_shim_den = shimane_soup.find_all('td')[15].find_all(text=True, recursive=True)
shimane_population = f"{raw_shim_pop[0]}"
shimane_density = f"{raw_shim_den[0]}{raw_shim_den[1]}"
shimane_density_mi = f"{raw_shim_den[2].replace('(', '').replace(')', '')}"
shimane_density_mi = tottori_density_mi.strip()

okayama_page = requests.get('https://en.wikipedia.org/wiki/Okayama_prefecture')
okayama_soup = BeautifulSoup(okayama_page.text, 'html.parser')
raw_ok_pop = okayama_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_ok_den = okayama_soup.find_all('td')[15].find_all(text=True, recursive=True)
okayama_population = f"{raw_ok_pop[0]}"
okayama_density = f"{raw_ok_den[0]}{raw_ok_den[1]}"
okayama_density_mi = f"{raw_ok_den[2].replace('(', '').replace(')', '')}"
okayama_density_mi = okayama_density_mi.strip()

hiroshima_page = requests.get('https://en.wikipedia.org/wiki/Hiroshima_prefecture')
hiroshima_soup = BeautifulSoup(hiroshima_page.text, 'html.parser')
raw_hi_pop = hiroshima_soup.find_all('td')[13].find_all(text=True, recursive=True)
raw_hi_den = hiroshima_soup.find_all('td')[15].find_all(text=True, recursive=True)
hiroshima_population = f"{raw_hi_pop[0]}"
hiroshima_density = f"{raw_hi_den[0]}{raw_hi_den[1]}"
hiroshima_density_mi = f"{raw_hi_den[2].replace('(', '').replace(')', '')}"
hiroshima_density_mi = hiroshima_density_mi.strip()

yamaguchi_page = requests.get('https://en.wikipedia.org/wiki/Yamaguchi_prefecture')
yamaguchi_soup = BeautifulSoup(yamaguchi_page.text, 'html.parser')
raw_yama_pop = yamaguchi_soup.find_all('td')[14].find_all(text=True, recursive=True)
raw_yama_den = yamaguchi_soup.find_all('td')[16].find_all(text=True, recursive=True)
yamaguchi_population = f"{raw_yama_pop[0]}"
yamaguchi_density = f"{raw_yama_den[0]}{raw_yama_den[1]}"
yamaguchi_density_mi = f"{raw_yama_den[2].replace('(', '').replace(')', '')}"
yamaguchi_density_mi = yamaguchi_density_mi.strip()

tokushima_page = requests.get('https://en.wikipedia.org/wiki/Tokushima_prefecture')
tokushima_soup = BeautifulSoup(tokushima_page.text, 'html.parser')
raw_toku_pop = tokushima_soup.find_all('td')[15].find_all(text=True, recursive=True)
raw_toku_den = tokushima_soup.find_all('td')[17].find_all(text=True, recursive=True)
tokushima_population = f"{raw_toku_pop[0]}"
tokushima_density = f"{raw_toku_den[0]}{raw_toku_den[1]}"
tokushima_density_mi = f"{raw_toku_den[2].replace('(', '').replace(')', '')}"
tokushima_density_mi = tokushima_density_mi.strip()

kagawa_page = requests.get('https://en.wikipedia.org/wiki/Kagawa_prefecture')
kagawa_soup = BeautifulSoup(kagawa_page.text, 'html.parser')
raw_kag_pop = kagawa_soup.find_all('td')[15].find_all(text=True, recursive=True)
raw_kag_den = kagawa_soup.find_all('td')[17].find_all(text=True, recursive=True)
kagawa_population = f"{raw_kag_pop[0]}"
kagawa_density = f"{raw_kag_den[0]}{raw_kag_den[1]}"
kagawa_density_mi = f"{raw_kag_den[2].replace('(', '').replace(')', '')}"
kagawa_density_mi = kagawa_density_mi.strip()

ehime_page = requests.get('https://en.wikipedia.org/wiki/Ehime_prefecture')
ehime_soup = BeautifulSoup(ehime_page.text, 'html.parser')
raw_eh_pop = ehime_soup.find_all('td')[15].find_all(text=True, recursive=True)
raw_eh_den = ehime_soup.find_all('td')[17].find_all(text=True, recursive=True)
ehime_population = f"{raw_eh_pop[0]}"
ehime_density = f"{raw_eh_den[0]}{raw_eh_den[1]}"
ehime_density_mi = f"{raw_eh_den[2].replace('(', '').replace(')', '')}"
ehime_density_mi = ehime_density_mi.strip()

kochi_page = requests.get('https://en.wikipedia.org/wiki/Kochi_prefecture')
kochi_soup = BeautifulSoup(kochi_page.text, 'html.parser')
raw_ko_pop = kochi_soup.find_all('td')[16].find_all(text=True, recursive=True)
raw_ko_den = kochi_soup.find_all('td')[18].find_all(text=True, recursive=True)
kochi_population = f"{raw_ko_pop[0]}"
kochi_density = f"{raw_ko_den[0]}{raw_ko_den[1]}"
kochi_density_mi = f"{raw_ko_den[2].replace('(', '').replace(')', '')}"
kochi_density_mi = kochi_density_mi.strip()
