import csv
from django.template.defaultfilters import slugify
from slugify import slugify
from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        global Phone
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))
        for item in phones:
            slug_name = slugify(item['name'])
            created = Phone.objects.create(
                id=item['id'],
                name=item['name'],
                price=item['price'],
                image=item['image'],
                release_date=item['release_date'],
                lte_exists=item['lte_exists'],
                slug=slug_name,
                )


            # create = Phone()
            # create.name = item['name'],
            # create.price = item['price'],
            # create.image = item['image'],
            # create.release_date = item['release_date'],
            # create.lte_exists = item['lte_exists'],
            # create.slug = item['name'],
            # create.save()




