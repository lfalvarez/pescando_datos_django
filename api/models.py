from django.db import models

# Create your models here.

class Inegi(models.Model):
    inegi_municipio = models.CharField(max_length=255, blank=True)
    inegi_localidad = models.CharField(max_length=255, blank=True)
    cod_estado = models.CharField(max_length=255, blank=True)
    estado = models.CharField(max_length=255, blank=True)
    estado_abreviado = models.CharField(max_length=255, blank=True)
    cod_municipio = models.CharField(max_length=255, blank=True)
    municipio = models.CharField(max_length=255, blank=True)
    cod_localidad = models.CharField(max_length=255, blank=True)
    localidad = models.CharField(max_length=255, blank=True)
    ambito = models.CharField(max_length=255, blank=True)
    latitud = models.CharField(max_length=255, blank=True)
    longitud = models.CharField(max_length=255, blank=True)
    altitud = models.CharField(max_length=255, blank=True)
    cve_carta = models.CharField(max_length=255, blank=True)
    inegi_localidad = models.CharField(max_length=255, blank=True)
    inegi_municipio = models.CharField(max_length=255, blank=True)


class Permiso(models.Model):
    tipo_embarcacion = models.CharField(max_length=255, blank=True)
    tipo_permiso = models.CharField(max_length=255, blank=True)
    estado = models.CharField(max_length=255, blank=True)
    municipio = models.CharField(max_length=255, blank=True)
    localidad = models.CharField(max_length=255, blank=True)
    area = models.CharField(max_length=255, blank=True)
    rnpa = models.CharField(max_length=255, blank=True)
    titular = models.CharField(max_length=255, blank=True)
    especie = models.CharField(max_length=255, blank=True)
    inicio = models.CharField(max_length=255, blank=True)
    termino = models.CharField(max_length=255, blank=True)
    inegi_localidad = models.CharField(max_length=255, blank=True)
    inegi_municipio = models.CharField(max_length=255, blank=True)

class Beneficiario(models.Model):
    rnpa = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)
 

class Activo(models.Model):
    rnpa = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    municipio = models.CharField(max_length=255)
    localidad = models.CharField(max_length=255)
    ano = models.CharField(max_length=255)
    inegi_localidad = models.CharField(max_length=255)
    inegi_municipio = models.CharField(max_length=255)

class Embarcacion(models.Model):
    rnpa = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)
    rnpa_unidad_economica = models.CharField(max_length=255)
    nombre_unidad_economica = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    municipio = models.CharField(max_length=255)
    localidad = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    fecha_registro = models.CharField(max_length=255)
    inegi_localidad = models.CharField(max_length=255)
    inegi_municipio = models.CharField(max_length=255)


class Marginacion(models.Model):
    cod_inegi = models.CharField(max_length=255, blank=True)
    cod_estado = models.CharField(max_length=255, blank=True)
    estado = models.CharField(max_length=255, blank=True)
    cod_municipio = models.CharField(max_length=255, blank=True)
    municipio = models.CharField(max_length=255, blank=True)
    cod_localidad = models.CharField(max_length=255, blank=True)
    localidad = models.CharField(max_length=255, blank=True)
    poblacion_total = models.IntegerField()
    viviendas_particulares = models.IntegerField()
    analfabeta = models.IntegerField()
    sin_primaria = models.IntegerField()
    sin_excusado = models.IntegerField()
    sin_energia_electrica = models.IntegerField()
    sin_agua_entubada = models.IntegerField()
    ocupantes_por_cuarto = models.IntegerField()
    sin_piso_tierra = models.IntegerField()
    sin_refrigerador = models.IntegerField()
    indice_marginacion_2010 = models.IntegerField()
    grado_marginacion = models.CharField(max_length=255, blank=True)
    indice_marginacion = models.IntegerField()
    lugar_en_nacional = models.IntegerField()
    lugar_en_estatal = models.IntegerField()

class BeneficiariosDiesel(models.Model):
    ano = models.CharField(max_length=255, blank=True)
    beneficiario = models.CharField(max_length=255, blank=True)
    rfc = models.CharField(max_length=255, blank=True)
    rnpa = models.CharField(max_length=255, blank=True)
    estado  = models.CharField(max_length=255, blank=True)
    municipio  = models.CharField(max_length=255, blank=True)
    localidad  = models.CharField(max_length=255, blank=True)
    monto = models.FloatField()
    inegi_localidad = models.CharField(max_length=255, blank=True)
    inegi_municipio = models.CharField(max_length=255, blank=True)

class BeneficiariosGasolina(models.Model):
    ano = models.CharField(max_length=255, blank=True)
    beneficiario = models.CharField(max_length=255, blank=True)
    rfc = models.CharField(max_length=255, blank=True)
    rnpa = models.CharField(max_length=255, blank=True)
    estado  = models.CharField(max_length=255, blank=True)
    municipio  = models.CharField(max_length=255, blank=True)
    localidad  = models.CharField(max_length=255, blank=True)
    monto = models.FloatField()
    inegi_localidad = models.CharField(max_length=255, blank=True)
    inegi_municipio = models.CharField(max_length=255, blank=True)

