import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_on_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_rahan_lataamisen_jalkeen_saldo_on_oikein(self):
        self.maksukortti.lataa_rahaa(100)
        self.assertEqual(str(self.maksukortti), "saldo: 1.1")

    def test_rahan_ottamisen_jalkeen_saldo_on_oikein(self):
        self.maksukortti.ota_rahaa(10)
        self.assertEqual(str(self.maksukortti), "saldo: 0.0")

    def test_saldo_ei_muutu_jos_rahaa_ei_ole_tarpeeksi(self):
        self.maksukortti.ota_rahaa(11)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_onnistuneen_rahan_oton_palautus_on_true(self):
        self.assertEqual(self.maksukortti.ota_rahaa(10), True)

    def test_epaonnistuneen_rahan_oton_palautus_on_false(self):
        self.assertEqual(self.maksukortti.ota_rahaa(11), False)