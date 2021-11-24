# Generated by Django 3.2.9 on 2021-11-21 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.IntegerField(primary_key=80, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('image', models.CharField(max_length=200)),
                ('release_date', models.DateField()),
                ('lte_exists', models.BooleanField()),
                ('slug', models.SlugField(max_length=200)),
            ],
        ),
    ]
