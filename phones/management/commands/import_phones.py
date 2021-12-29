import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:

            phones = csv.reader(file, delimiter=';')
            next(phones)

            for line in phones:
                slug = '-'.join(line[1].split()).lower()
                Phone.objects.create(name=line[1], price=line[3], image=line[2], release_date=line[4], lte_exists=line[5], slug=slug)
