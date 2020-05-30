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


if __name__ == '__main__':
    unittest.main()
