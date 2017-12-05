from django.test import TestCase
from api.models import *
from api.csv_loader import *
from django.core.management import call_command


lines = [['id', 'ano', 'beneficiario', 'rfc', 'rnpa_emb', 'rnpa', 'clave_uni', 'estado', 'municipio', 'localidad', 'monto', 'cod_inegi_localidad', 'cod_inegi_municipio', 'Folio', 'Número de RNP_EMB por RNPA', 'Suma de Litros Asignados'],
         ['1', '2011', 'LEON SAINZ JESUS ISRAEL', '', '3007051', '308000462', '308000462', 'BAJA CALIFORNIA SUR', 'Comondu', 'Puerto Adolfo Lopez Mateos', '11200', '', '', '', '', ''],
         ['2', '2011', 'LIERA VELAZQUEZ SALVADOR MARTIN', '', '3007515', '3011002791', '3011002791', 'BAJA CALIFORNIA SUR', 'La Paz', 'La Paz', '7000', '', '', '', '', '']]


class BeneficiarioGasolinaLoaderCsvLoaders(TestCase):
    def test_headers_and_stuff(self):
        i_l = BeneficiarioGasolinaLoader()
        i_l.set_lines(lines)
        headers = i_l.headers
        self.assertEquals(headers["id"], 0)
        self.assertEquals(headers["ano"], 1)
        self.assertEquals(headers["beneficiario"], 2)
        self.assertEquals(headers["rfc"], 3)
        self.assertEquals(headers["rnpa_emb"], 4)
        self.assertEquals(headers["rnpa"], 5)
        self.assertEquals(headers["llave_unica"], 6)
        self.assertEquals(headers["estado"], 7)
        self.assertEquals(headers["municipio"], 8)
        self.assertEquals(headers["localidad"], 9)
        self.assertEquals(headers["monto"], 10)
        self.assertEquals(headers["inegi_localidad"], 11)
        self.assertEquals(headers["inegi_municipio"], 12)
        self.assertEquals(headers["folio"], 13)
        self.assertEquals(headers["npa_emb"], 14)

        self.assertEquals(headers["suma_litros_asignados"], 15)