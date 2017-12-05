from .models import *
from django.core.exceptions import FieldDoesNotExist
from django.utils.text import slugify

class CSVParsingError(Exception):
    pass

class CSVLoaderBase:

    def __init__(self):
        self.lines = []
        self.headers = {}
        self.overriden_headers = {}

    def set_headers(self, headers):
        index = 0
        for header in headers:
            if header in self.overriden_headers:
                header = self.overriden_headers[header]
            header = slugify(header.replace(" ", "_"))
            self.headers[header] = index
            index += 1

    def validate_headers(self):
        for header in self.headers:
            try:
                self.model._meta.get_field(header)
            except FieldDoesNotExist:
                raise CSVParsingError("El campo `"+ header + "` no está")

    def set_lines(self, lines):
        self.set_headers(lines[0])
        self.validate_headers()
        self.lines = lines[1:]

    def get_attrs_dict(self, line):
        result = {}
        for header in self.headers:
            result[header] = line[self.headers[header]]
        return result

    def process(self):
        errors = []
        line_counter = 0
        for line in self.lines:
            instance = self.model(**(self.get_attrs_dict(line)))
            try:
                instance.save()
            except Exception as e:
                errors.append("Error con la línea " + str(line_counter) + " el error es "+ str(e))
            line_counter += 1
        if errors:
            print(errors)

class BeneficiarioDieselLoader(CSVLoaderBase):

    def __init__(self):
        super().__init__()
        self.model = BeneficiariosDiesel
        self.overriden_headers = {
            'cod_inegi_municipio' : 'inegi_municipio',
            'cod_inegi_localidad':  "inegi_localidad",
        }

class BeneficiarioGasolinaLoader(CSVLoaderBase):
    def __init__(self):
        super().__init__()
        self.model = BeneficiariosGasolina
        self.overriden_headers = {
            'cod_inegi_municipio' : 'inegi_municipio',
            'cod_inegi_localidad':  "inegi_localidad",
            "Número de RNP_EMB por RNPA": 'npa_emb',
            'clave_uni': 'llave_unica',
            'Suma de Litros Asignados': 'suma_litros_asignados'
        }

class InegiLoader(CSVLoaderBase):
    def __init__(self):
        super().__init__()
        self.model = Inegi
        self.overriden_headers = {
            'COD_INEGI_MUNICIPIO' : 'inegi_municipio',
            'COD_INEGI_LOCALIDAD':  "inegi_localidad",
            'NOM_ABR': 'estado_abreviado'
        }

