import sys
sys.path.append("../api")
from prefectures_data import *
import unittest
# nom - nominal ppp - purchasing power parity,
# den - density, pop - population, gov - governor


class TestPrefectures(unittest.TestCase):
    def test_japan(self):
        self.assertEqual(japan_emperor, 'Naruhito')
        self.assertEqual(japan_minister, 'Shinzō Abe')
        self.assertEqual(japan_population, '126,150,000')
        self.assertEqual(japan_density, '334/km2')
        self.assertEqual(japan_density_mi, '865.1/sq\xa0mi')
        self.assertEqual(gdp_nom, '$5.413 trillion')
        self.assertEqual(gdp_ppp, '$5.888 trillion')
        self.assertEqual(gdp_nom_per, '$43,043')
        self.assertEqual(gdp_ppp_per, '$46,827')
        self.assertEqual(japan_gini, '33.9 - medium')
        self.assertEqual(japan_hdi, '0.915 - very high')

    def test_hokkaido(self):
        self.assertEqual(raw_hok_pop, ['5,281,297'])
        self.assertEqual(raw_hok_den, ['63/km', '2', ' (160/sq\xa0mi)'])
        self.assertEqual(raw_hok_gov, ['Naomichi Suzuki'])

    def test_aomori(self):
        self.assertEqual(raw_ao_pop, ['1,249,314'])
        self.assertEqual(raw_ao_den, ['130/km', '2', ' (340/sq\xa0mi)'])
        self.assertEqual(raw_ao_gov, ['Shingo Mimura'])

    def test_iwate(self):
        self.assertEqual(raw_iw_pop, ['1,229,432'])
        self.assertEqual(raw_iw_den, ['80/km', '2', ' (210/sq\xa0mi)'])
        self.assertEqual(raw_iw_gov, ['Takuya Tasso'])

    def test_miyagi(self):
        self.assertEqual(raw_mi_pop, ['2,305,596'])
        self.assertEqual(raw_mi_den, ['320/km', '2', ' (820/sq\xa0mi)'])
        self.assertEqual(raw_mi_gov, ['Yoshihiro Murai'])

    def test_akita(self):
        self.assertEqual(raw_ak_pop, ['966,000'])
        self.assertEqual(raw_ak_den, ['83/km', '2', ' (210/sq\xa0mi)'])
        self.assertEqual(raw_ak_gov, ['Norihisa Satake'])

    def test_yamagata(self):
        self.assertEqual(raw_ya_pop, ['1,079,950'])
        self.assertEqual(raw_ya_den, ['120/km', '2', ' (300/sq\xa0mi)'])
        self.assertEqual(raw_ya_gov, ['Mieko Yoshimura'])

    def test_fukushima(self):
        self.assertEqual(raw_fu_pop, ['1,848,257'])
        self.assertEqual(raw_fu_den, ['130/km', '2', ' (350/sq\xa0mi)'])
        self.assertEqual(raw_fu_gov, ['Masao Uchibori'])

    def test_ibaraki(self):
        self.assertEqual(raw_ib_pop, ['2,871,199'])
        self.assertEqual(raw_ib_den, ['470/km', '2', ' (1,200/sq\xa0mi)'])
        self.assertEqual(raw_ib_gov, ['Kazuhiko Ōigawa'])

    def test_tochigi(self):
        self.assertEqual(raw_to_pop, ['1,943,886'])
        self.assertEqual(raw_to_den, ['300/km', '2', ' (790/sq\xa0mi)'])
        self.assertEqual(raw_to_gov, ['Tomikazu Fukuda'])

    def test_gunma(self):
        self.assertEqual(raw_gu_pop, ['1,937,626'])
        self.assertEqual(raw_gu_den, ['300/km', '2', ' (790/sq\xa0mi)'])
        self.assertEqual(raw_gu_gov, ['Ichita Yamamoto'])

    def test_saitama(self):
        self.assertEqual(raw_sa_pop, ['7,338,536'])
        self.assertEqual(raw_sa_den, ['1,900/km', '2', ' (5,000/sq\xa0mi)'])
        self.assertEqual(raw_sa_gov, ['Motohiro Ōno'])

    def test_chiba(self):
        self.assertEqual(raw_chi_pop, ['6,278,060'])
        self.assertEqual(raw_chi_den, ['1,200/km', '2', ' (3,200/sq\xa0mi)'])
        self.assertEqual(raw_chi_gov, ['Kensaku Morita'])

    def test_tokyo(self):
        self.assertEqual(raw_tok_pop, ['13,929,280'])
        self.assertEqual(raw_tok_den, ['6,349/km', '2', ' (16,440/sq\xa0mi)'])
        self.assertEqual(raw_tok_gov[0], 'Yuriko Koike')

    def test_kanagawa(self):
        self.assertEqual(raw_ka_pop, ['9,058,094'])
        self.assertEqual(raw_ka_den, ['3,770/km', '2', ' (9,800/sq\xa0mi)'])
        self.assertEqual(raw_ka_gov[0], 'Yūji Kuroiwa')

    def test_niigata(self):
        self.assertEqual(raw_ni_pop, ['2,227,496'])
        self.assertEqual(raw_ni_den, ['180/km', '2', ' (460/sq\xa0mi)'])
        self.assertEqual(raw_ni_gov, ['Hideyo Hanazumi'])

    def test_toyama(self):
        self.assertEqual(raw_toy_pop, ['1,044,588'])
        self.assertEqual(raw_toy_den, ['250/km', '2', ' (640/sq\xa0mi)'])
        self.assertEqual(raw_toy_gov, ['Takakazu Ishii'])

    def test_ishikawa(self):
        self.assertEqual(raw_ish_pop, ['1,140,573'])
        self.assertEqual(raw_ish_den, ['272.47/km', '2', ' (705.7/sq\xa0mi)'])
        self.assertEqual(raw_ish_gov, ['Masanori Tanimoto'])

    def test_fukui(self):
        self.assertEqual(raw_fuk_pop, ['778,943'])
        self.assertEqual(raw_fuk_den, ['185.95/km', '2', ' (481.6/sq\xa0mi)'])
        self.assertEqual(raw_fuk_gov, ['Tatsuji Sugimoto'])

    def test_yamanashi(self):
        self.assertEqual(raw_yam_pop, ['817,192'])
        self.assertEqual(raw_yam_den, ['183/km', '2', ' (470/sq\xa0mi)'])
        self.assertEqual(raw_yam_gov[0], 'Kotaro Nagasaki')

    def test_nagano(self):
        self.assertEqual(raw_na_pop, ['2,052,493'])
        self.assertEqual(raw_na_den, ['150/km', '2', ' (390/sq\xa0mi)'])
        self.assertEqual(raw_na_gov, ['Shuichi Abe'])

    def test_gifu(self):
        self.assertEqual(raw_gi_pop, ['1,991,390'])
        self.assertEqual(raw_gi_den, ['190/km', '2', ' (490/sq\xa0mi)'])
        self.assertEqual(raw_gi_gov[0], 'Hajime Furuta')

    def test_shizuoka(self):
        self.assertEqual(raw_shi_pop, ['3,637,998'])
        self.assertEqual(raw_shi_den, ['470/km', '2', ' (1,200/sq\xa0mi)'])
        self.assertEqual(raw_shi_gov, ['Heita Kawakatsu'])

    def test_aichi(self):
        self.assertEqual(raw_ai_pop, ['7,552,873'])
        self.assertEqual(raw_ai_den, ['1,500/km', '2', ' (3,800/sq\xa0mi)'])
        self.assertEqual(raw_ai_gov[0], 'Hideaki Ōmura')

    def test_mie(self):
        self.assertEqual(raw_mie_pop, ['1,781,948'])
        self.assertEqual(raw_mie_den, ['310/km', '2', ' (800/sq\xa0mi)'])
        self.assertEqual(raw_mie_gov[0], 'Eikei Suzuki')

    def test_shiga(self):
        self.assertEqual(raw_shig_pop, ['1,412,916'])
        self.assertEqual(raw_shig_den, ['350/km', '2', ' (910/sq\xa0mi)'])
        self.assertEqual(raw_shig_gov[0], 'Taizō Mikazuki')

    def test_kyoto(self):
        self.assertEqual(raw_ky_pop, ['2,610,353'])
        self.assertEqual(raw_ky_den, ['566/km', '2', ' (1,470/sq\xa0mi)'])
        self.assertEqual(raw_ky_gov[0], 'Takatoshi Nishiwaki')

    def test_osaka(self):
        self.assertEqual(raw_os_pop, ['8,823,358'])
        self.assertEqual(raw_os_den, ['4,600/km', '2', ' (12,000/sq\xa0mi)'])
        self.assertEqual(raw_os_gov[0], 'Hirofumi Yoshimura')

    def test_hyogo(self):
        self.assertEqual(raw_hy_pop, ['5,469,762'])
        self.assertEqual(raw_hy_den, ['650/km', '2', ' (1,700/sq\xa0mi)'])
        self.assertEqual(raw_hy_gov[0], 'Toshizō Ido')

    def test_nara(self):
        self.assertEqual(raw_nar_pop, ['1,348,930'])
        self.assertEqual(raw_nar_den, ['365.46/km', '2', ' (946.5/sq\xa0mi)'])
        self.assertEqual(raw_nar_gov[0], 'Shōgo Arai')

    def test_wakayama(self):
        self.assertEqual(raw_wa_pop, ['944,320'])
        self.assertEqual(raw_wa_den, ['199.87/km', '2', ' (517.7/sq\xa0mi)'])
        self.assertEqual(raw_wa_gov[0], 'Yoshinobu Nisaka')

    def test_tottori(self):
        self.assertEqual(raw_tot_pop, ['570,569'])
        self.assertEqual(raw_tot_den, ['163/km', '2', ' (420/sq\xa0mi)'])
        self.assertEqual(raw_tot_gov[0], 'Shinji Hirai')

    def test_shimane(self):
        self.assertEqual(raw_shim_pop, ['689,963'])
        self.assertEqual(raw_shim_den, ['102.85/km', '2', ' (266.4/sq\xa0mi)'])
        self.assertEqual(raw_shim_gov[0], 'Tatsuya Maruyama')

    def test_okayama(self):
        self.assertEqual(raw_ok_pop, ['1,906,464'])
        self.assertEqual(raw_ok_den, ['270/km', '2', ' (690/sq\xa0mi)'])
        self.assertEqual(raw_ok_gov[0], 'Ryūta Ibaragi')

    def test_hiroshima(self):
        self.assertEqual(raw_hi_pop, ['2,811,410'])
        self.assertEqual(raw_hi_den, ['330/km', '2', ' (860/sq\xa0mi)'])
        self.assertEqual(raw_hi_gov[0], 'Hidehiko Yuzaki')

    def test_yamaguchi(self):
        self.assertEqual(raw_yama_pop, ['1,377,631'])
        self.assertEqual(raw_yama_den, ['225.43/km', '2', ' (583.9/sq\xa0mi)'])
        self.assertEqual(raw_yama_gov[0], 'Tsugumasa Muraoka')

    def test_tokushima(self):
        self.assertEqual(raw_toku_pop, ['728,633'])
        self.assertEqual(raw_toku_den, ['180/km', '2', ' (460/sq\xa0mi)'])
        self.assertEqual(raw_toku_gov[0], 'Kamon Iizumi')

    def test_kagawa(self):
        self.assertEqual(raw_kag_pop, ['957,430'])
        self.assertEqual(raw_kag_den, ['510/km', '2', ' (1,300/sq\xa0mi)'])
        self.assertEqual(raw_kag_gov[0], 'Keizō Hamada')

    def test_ehime(self):
        self.assertEqual(raw_eh_pop, ['1,342,011'])
        self.assertEqual(raw_eh_den, ['240/km', '2', ' (610/sq\xa0mi)'])
        self.assertEqual(raw_eh_gov[0], 'Tokihiro Nakamura')

    def test_kochi(self):
        self.assertEqual(raw_ko_pop, ['757,914'])
        self.assertEqual(raw_ko_den, ['106.68/km', '2', ' (276.3/sq\xa0mi)'])
        self.assertEqual(raw_ko_gov[0], 'Seiji Hamada')

    def test_fukuoka(self):
        self.assertEqual(raw_fuku_pop, ['5,109,323'])
        self.assertEqual(raw_fuku_den, ['1,000/km', '2', ' (2,700/sq\xa0mi)'])
        self.assertEqual(raw_fuku_gov[0], 'Hiroshi Ogawa')

    def test_saga(self):
        self.assertEqual(raw_sag_pop, ['813,590'])
        self.assertEqual(raw_sag_den, ['330/km', '2', ' (860/sq\xa0mi)'])
        self.assertEqual(raw_sag_gov[0], 'Yoshinori Yamaguchi')

    def test_nagasaki(self):
        self.assertEqual(raw_nag_pop, ['1,328,478'])
        self.assertEqual(raw_nag_den, ['320/km', '2', ' (830/sq\xa0mi)'])
        self.assertEqual(raw_nag_gov[0], 'Hōdō Nakamura')

    def test_kumamoto(self):
        self.assertEqual(raw_ku_pop, ['1,748,134'])
        self.assertEqual(raw_ku_den, ['240/km', '2', ' (610/sq\xa0mi)'])
        self.assertEqual(raw_ku_gov[0], 'Ikuo Kabashima')

    def test_oita(self):
        self.assertEqual(raw_oi_pop, ['1,136,245'])
        self.assertEqual(raw_oi_den, ['180/km', '2', ' (460/sq\xa0mi)'])
        self.assertEqual(raw_oi_gov[0], 'Katsusada Hirose')

    def test_miyazaki(self):
        self.assertEqual(raw_miya_pop, ['1,073,054'])
        self.assertEqual(raw_miya_den, ['140/km', '2', ' (360/sq\xa0mi)'])
        self.assertEqual(raw_miya_gov[0], 'Shunji Kōno')

    def test_kagoshima(self):
        self.assertEqual(raw_kago_pop, ['1,599,779'])
        self.assertEqual(raw_kago_den, ['170/km', '2', ' (450/sq\xa0mi)'])
        self.assertEqual(raw_kago_gov[0], 'Satoshi Mitazono')

    def test_okinawa(self):
        self.assertEqual(raw_oki_pop, ['1,457,162'])
        self.assertEqual(raw_oki_den, ['640/km', '2', ' (1,700/sq\xa0mi)'])
        self.assertEqual(raw_oki_gov[0], 'Denny Tamaki')


if __name__ == '__main__':
    unittest.main()
