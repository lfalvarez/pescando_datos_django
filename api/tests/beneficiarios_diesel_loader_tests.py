from django.test import TestCase
from api.models import *
from api.csv_loader import *
from django.core.management import call_command


cabecera = ['id', 'ano', 'beneficiario', 'rfc', 'rnpa', 'Llave única', 'estado', 'municipio', 'localidad', 'monto', 'cod_inegi_municipio',
            'cod_inegi_localidad', 'sexo', 'actividad productiva', 'Programa', 'Componente']
lines = [cabecera, ['1', '2011', '11 DE DICIEMBRE DE 1996 SPR DE RI', 'ODM971201ST1', '2602001881', '2602001881', 'SONORA', 'CAJEME', 'CIUDAD OBREGON', '300000', '26018', '26018001', '', '', '', ''],
         ['2', '2011', 'ABRAHAM BARCELO JORGE BAIDABE', '', '3102001041', '3102001041', 'YUCATAN', 'DZILAM DE BRAVO', 'DZILAM DE BRAVO', '254000', '31028', '31028001', '', '', '', '']]


class BeneficiarioDieselLoaderCsvLoaders(TestCase):
    def test_headers_and_stuff(self):
        i_l = BeneficiarioDieselLoader()
        i_l.set_lines(lines)
        headers = i_l.headers
        self.assertEquals(headers["id"], 0)
        self.assertEquals(headers["ano"], 1)
        self.assertEquals(headers["beneficiario"], 2)
        self.assertEquals(headers["rfc"], 3)
        self.assertEquals(headers["rnpa"], 4)
        self.assertEquals(headers["llave_unica"], 5)
        self.assertEquals(headers["estado"], 6)
        self.assertEquals(headers["municipio"], 7)
        self.assertEquals(headers["localidad"], 8)
        self.assertEquals(headers["monto"], 9)
        self.assertEquals(headers["inegi_localidad"], 11)
        self.assertEquals(headers["inegi_municipio"], 10)
        
        self.assertEquals(headers["sexo"], 12)
        self.assertEquals(headers["actividad_productiva"], 13)
        self.assertEquals(headers["programa"], 14)
        self.assertEquals(headers["componente"], 15)

    def test_command_line_loader(self):
        call_command("load_csv", 'diesel', 'api/tests/csv_fixtures/beneficiarios_diesel.csv')
        self.assertTrue(BeneficiariosDiesel.objects.exists())