from django.core.management.base import BaseCommand, CommandError
from api.csv_loader import InegiLoader
import csv

LOADERS = {
    'inegi': InegiLoader
}

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('model', nargs=1, type=str)
        parser.add_argument('csv_file', nargs=1, type=str)

    def handle(self, *args, **options):
        lines = []
        with open(options['csv_file'][0], newline='') as csvfile:
            r = csv.reader(csvfile)
            for row in r:
                lines.append(row)
        
        loader = LOADERS[options['model'][0]]()
        loader.set_lines(lines)
        loader.process()