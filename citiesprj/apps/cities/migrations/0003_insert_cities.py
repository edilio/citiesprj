# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-26 11:41
from __future__ import unicode_literals

import csv

from django.db import migrations


def insert_cities(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    City = apps.get_model("cities", "City")
    path = 'citiesprj/apps/cities/migrations/'
    with open(path + 'zbp13totals.txt') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['city']:
                City.objects.create(city=row['city'], state=row['stabbr'], zip_code=row['zip'])



class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0002_auto_20160425_1119'),
    ]

    operations = [
        migrations.RunPython(insert_cities),
    ]
