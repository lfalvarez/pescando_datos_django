from django.test import TestCase
from .models import *


class ModelsTestCase(TestCase):
    def test_inegi(self):
        i = Inegi.objects.create(inegi_municipio="12", inegi_localidad="13")
        self.assertTrue(i)

    def test_permiso(self):
        p = Permiso.objects.create(rnpa="12")
        self.assertTrue(p)

    def test_beneficiario(self):
        b = Beneficiario.objects.create(rnpa="12", nombre="Persons")
        self.assertTrue(b)

    def test_activo(self):
        a = Activo.objects.create(rnpa="12", nombre="hola")
        self.assertTrue(a)

    def test_embarcacion(self):
        e = Embarcacion.objects.create(rnpa="12", nombre="hola")
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

    def test_beneficiario_gasolina(self):
        b = BeneficiariosGasolina.objects.create(ano="2017", monto=12.0)
        self.assertTrue(b)