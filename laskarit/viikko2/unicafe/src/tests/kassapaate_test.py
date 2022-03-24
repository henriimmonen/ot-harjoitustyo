import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(400)

    def test_kassapaatteen_saldo_on_alussa_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kassapaatteen_maukkaat_lounaat_alussa(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kassapaatteen_edulliset_lounaat_alussa(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kassapaatteen_saldo_kasvaa_maksettaessa_kateisella_edullinen_lounas(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_vaihtoraha_on_oikein_maksettaessa_kateisella_edullinen_lounas(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(240), 0)

    def test_edullisten_lounaiden_maara_kasvaa_maksettaessa_kateisella(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_edullisesti_kassapaatteen_saldo_ei_kasva_virheellisella_kateismaksulla(self):
        self.kassapaate.syo_edullisesti_kateisella(230)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_palautus_vaihtorahana_jos_kateinen_ei_riita_edulliseen(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(230), 230)

    def test_edullisten_maara_ei_kasva_jos_kateinen_ei_riita(self):
        self.kassapaate.syo_edullisesti_kateisella(230)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kassapaatteen_saldo_kasvaa_maksettaessa_kateisella_maukas_lounas(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_vaihtoraha_on_oikein_maksettaessa_kateisella_maukas_lounas(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(400), 0)

    def test_maukkaiden_lounaiden_maara_kasvaa_maksettaessa_kateisella(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maukkaasti_kassapaatteen_saldo_ei_kasva_virheellisella_kateismaksulla(self):
        self.kassapaate.syo_maukkaasti_kateisella(399)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_palautus_vaihtorahana_jos_kateinen_ei_riita_maukkaaseen(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(399), 399)

    def test_maukkaiden_maara_ei_kasva_jos_kateinen_ei_riita(self):
        self.kassapaate.syo_maukkaasti_kateisella(399)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_korttimaksu_edullinen_veloitus_onnistuu_kortilta(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "saldo: 1.6")

    def test_korttimaksu_maukas_veloitus_onnistuu_kortilta(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "saldo: 0.0")

    def test_onnistunut_korttimaksu_palauttaa_true_edullisesti(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)

    def test_onnistunut_korttimaksu_palauttaa_true_maukkaasti(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)

    def test_korttimaksulla_myytyjen_maara_kasvaa_edullinen(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_korttimaksulla_myytyjen_maara_kasvaa_maukas(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kortilla_ei_ole_rahaa_saldo_ei_muutu_edullinen(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "saldo: 1.6")

    def test_kortilla_ei_ole_rahaa_saldo_ei_muutu_maukas(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "saldo: 1.6")

    def test_edulliset_ei_kasva_jos_kortilla_ei_ole_rahaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaat_ei_kasva_jos_kortilla_ei_ole_rahaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_korttimaksu_palauttaa_false_jos_rahat_ei_riitä_edulliseen(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), False)

    def test_korttimaksu_palauttaa_false_jos_rahat_ei_riitä_maukkaaseen(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), False)

    def test_kassassa_oleva_saldo_ei_muutu_korttimaksulla_edullinen(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kassassa_oleva_saldo_ei_muutu_korttimaksulla_maukas(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortille_ladattaessa_rahaa_kassan_saldo_kasvaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100100)

    def test_kortille_ladattaessa_rahaa_kortin_saldo_muuttuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)
        self.assertEqual(str(self.maksukortti), "saldo: 5.0")

    def test_kortille_ei_voi_ladata_negatiivista_summaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)
        self.assertEqual(str(self.maksukortti), "saldo: 4.0")