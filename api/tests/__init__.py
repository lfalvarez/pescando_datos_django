from django.test import TestCase
from api.models import *
from api.csv_loader import *
from django.core.management import call_command

class ModelsTestCase(TestCase):
    def test_inegi(self):
        i = Inegi.objects.create(inegi_municipio="12", inegi_localidad="13", cod_inegi="1230")
        self.assertTrue(i)

    def test_permiso(self):
        p = Permiso.objects.create(rnpa="12")
        self.assertTrue(p)

    def test_beneficiario(self):
        b = Beneficiario.objects.create(rnpa="12", nombre="Persons")
        self.assertTrue(b)

    def test_beneficiario_permiso(self):
        b = Beneficiario.objects.create(rnpa="12", nombre="Persons")
        p = Permiso.objects.create(rnpa="12", beneficiario=b)
        self.assertTrue(p)

    def test_activo(self):
        a = Activo.objects.create(rnpa="12", nombre="hola")
        self.assertTrue(a)

    def test_activo_beneficiario(self):
        b = Beneficiario.objects.create(rnpa="12", nombre="Persons")
        a = Activo.objects.create(rnpa="12", nombre="hola")
        a.beneficiario = b
        a.save()
        a.refresh_from_db()
        a = Activo.objects.get(id=a.id)
        self.assertEquals(a.beneficiario, b)

    def test_embarcacion(self):
        e = Embarcacion.objects.create(rnpa="12", nombre="hola")
        self.assertTrue(e)

    def test_embarcacion_beneficiario(self):
        b = Beneficiario.objects.create(rnpa="12", nombre="Persons")
        e = Embarcacion.objects.create(rnpa="12", nombre="hola", beneficiario=b)
        self.assertTrue(e)

    def test_marginacion(self):
        m = Marginacion(cod_inegi="12")
        m.poblacion_total = 13
        m.viviendas_particulares = 13
        m.analfabeta = 13
        m.sin_primaria = 13
        m.sin_excusado = 13
        m.sin_energia_electrica = 13
        m.sin_agua_entubada = 13
        m.ocupantes_por_cuarto = 13
        m.sin_piso_tierra = 13
        m.sin_refrigerador = 13
        m.indice_marginacion_2010 = 13
        m.indice_marginacion = 13
        m.lugar_en_nacional = 13
        m.lugar_en_estatal = 13
        m.save()
        self.assertTrue(m)

    def test_beneficiario_diesel(self):
        b = BeneficiariosDiesel.objects.create(ano="2017", monto=12.0)
        self.assertTrue(b)

    def test_beneficiario_diesel_beneficiario(self):
        b_ = Beneficiario.objects.create(rnpa="12", nombre="Persons")
        b = BeneficiariosDiesel.objects.create(ano="2017", monto=12.0)
        self.assertTrue(b)

    def test_beneficiario_gasolina(self):
        b = BeneficiariosGasolina.objects.create(ano="2017", monto=12.0)
        self.assertTrue(b)


INEGI_lines = [["id","COD_INEGI_MUNICIPIO","COD_INEGI_LOCALIDAD","COD_ESTADO","ESTADO","NOM_ABR","COD_MUNICIPIO","MUNICIPIO","COD_LOCALIDAD","LOCALIDAD","AMBITO","LATITUD","LONGITUD","ALTITUD","CVE_CARTA","COD_INEGI"],
["2","001001","001001001","1","AGUASCALIENTES","Ags.","1","AGUASCALIENTES","1","AGUASCALIENTES","U","215247362","1021745768","1878","F13D19","1001001"],
["3","001001","001001904","1","AGUASCALIENTES","Ags.",'1',"AGUASCALIENTES","904","GRANJA ADELITA","R","215218749","1022224710","1902","F13D18","1001904"]]


class CsvLoaders(TestCase):
    def test_headers_and_stuff(self):
        i_l = InegiLoader()
        i_l.set_lines(INEGI_lines)
        headers = i_l.headers
        self.assertEquals(headers["id"], 0)
        self.assertEquals(headers["inegi_municipio"], 1)
        self.assertEquals(headers["inegi_localidad"], 2)
        self.assertEquals(headers["cod_estado"], 3)
        self.assertEquals(headers["estado"], 4)
        self.assertEquals(headers["estado_abreviado"], 5)
        self.assertEquals(headers["cod_municipio"], 6)
        self.assertEquals(headers["municipio"], 7)
        self.assertEquals(headers["cod_localidad"], 8)
        self.assertEquals(headers["localidad"], 9)
        self.assertEquals(headers["ambito"], 10)
        self.assertEquals(headers["latitud"], 11)
        self.assertEquals(headers["longitud"], 12)
        self.assertEquals(headers["altitud"], 13)
        self.assertEquals(headers["cve_carta"], 14)
        self.assertEquals(headers["cod_inegi"], 15)

    def test_raises_exception_when_headers_are_wrong(self):
        lines = [["od","perrito"],
                ["1","gatito"],]
        i_l = InegiLoader()
        with self.assertRaises(CSVParsingError):
            i_l.set_lines(lines)


    def test_load_inegi_from_csv(self):
        i_l = InegiLoader()
        i_l.set_lines(INEGI_lines)
        i_l.process()
        self.assertEquals(Inegi.objects.count(), 2)
        i = Inegi.objects.get(id=2)
        self.assertEquals(i.inegi_municipio, "001001")
        self.assertEquals(i.inegi_localidad, "001001001")
        self.assertEquals(i.cod_estado, "1")
        self.assertEquals(i.estado, "AGUASCALIENTES")
        self.assertEquals(i.estado_abreviado, "Ags.")
        self.assertEquals(i.cod_municipio, "1")
        self.assertEquals(i.municipio, "AGUASCALIENTES")
        self.assertEquals(i.cod_localidad, "1")
        self.assertEquals(i.localidad, "AGUASCALIENTES")
        self.assertEquals(i.ambito, "U")
        self.assertEquals(i.latitud, "215247362")
        self.assertEquals(i.longitud, "1021745768")
        self.assertEquals(i.altitud, "1878")
        self.assertEquals(i.cve_carta, "F13D19")
        self.assertEquals(i.cod_inegi, "1001001")

        i2 = Inegi.objects.get(id=3)
        self.assertEquals(i2.localidad,"GRANJA ADELITA")
        self.assertEquals(i2.cod_inegi,"1001904")

    def test_command_line_loader(self):
        call_command("load_csv", 'inegi', 'api/tests/csv_tests/inegi.csv')
        self.assertTrue(Inegi.objects.exists())