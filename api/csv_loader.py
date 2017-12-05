from .models import *
from django.core.exceptions import FieldDoesNotExist

class CSVParsingError(Exception):
    pass

class CSVLoaderBase(object):
    lines = []
    headers = {}
    overriden_headers = {}

    def set_headers(self, headers):
        index = 0
        for header in headers:
            if header in self.overriden_headers:
                header = self.overriden_headers[header]
            self.headers[header.lower()] = index
            index += 1

    def validate_headers(self):
        for header in self.headers:
            try:
                self.model._meta.get_field(header)
            except FieldDoesNotExist:
                raise CSVParsingError

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
        for line in self.lines:
            instance = self.model(**(self.get_attrs_dict(line)))
            instance.save()

class InegiLoader(CSVLoaderBase):
    model = Inegi
    overriden_headers = {
        'COD_INEGI_MUNICIPIO' : 'inegi_municipio',
        'COD_INEGI_LOCALIDAD':  "inegi_localidad",
        'NOM_ABR': 'estado_abreviado'
    }