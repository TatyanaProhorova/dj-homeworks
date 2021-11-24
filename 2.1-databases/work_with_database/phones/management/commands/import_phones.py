import csv
from slugify import slugify
from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))
        for item in phones:
                phone = Phone(
                id = item['id'],
                name = item['name'],
                price = item['price'],
                image = item['image'],
                release_date = item['release_date'],
                lte_exists = item['lte_exists'],
                # slug = slugify(item['name']),
                slug = item['name']
                )



