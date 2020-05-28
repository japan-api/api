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
        self.assertEqual(raw_ib_den, ['470/km', '2', ' (1200/sq\xa0mi)'])
        self.assertEqual(raw_ib_gov, ['Kazuhiko Ōigawa'])


if __name__ == '__main__':
    unittest.main()
