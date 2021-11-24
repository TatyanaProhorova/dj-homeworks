from django.db import models
from django.http import HttpResponse


class Phone(models.Model):
    id = models.IntegerField(primary_key=80)
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    image = models.CharField(max_length=200)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=200)


def list_phone(request):
    phone_objects = Phone.objects.all()
    phones = [f'{p.name}' for p in phone_objects]
    return HttpResponse('<br>'.join(phones))





