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
        self.assertEqual(japan_density, '')
        self.assertEqual(gdp_nom, '')
        self.assertEqual(gdp_ppp, '')

    def test_hokkaido(self):
        self.assertEqual(raw_hok_pop, ['5,281,297'])
        self.assertEqual(raw_hok_den, ['63/km', '2', ' (160/sq\xa0mi)'])
        self.assertEqual(raw_hok_gov, ['Naomichi Suzuki'])


if __name__ == '__main__':
    unittest.main()