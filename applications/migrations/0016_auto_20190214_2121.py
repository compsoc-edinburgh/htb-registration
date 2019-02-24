# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2019-02-14 21:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0015_merge_20190214_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='description',
            field=models.TextField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='application',
            name='diet',
            field=models.CharField(choices=[('None', 'No requirements'), ('Vegeterian', 'Vegeterian'), ('Vegan', 'Vegan'), ('Gluten-free', 'Gluten-free'), ('Other', 'Other')], default='None', max_length=300),
        ),
        migrations.AlterField(
            model_name='application',
            name='projects',
            field=models.TextField(blank=True, max_length=1500, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='tshirt_size',
            field=models.CharField(choices=[('W-XS', "Women's - XS"), ('W-S', "Women's - S"), ('W-M', "Women's - M"), ('W-L', "Women's - L"), ('W-XL', "Women's - XL"), ('W-XXL', "Women's - XXL"), ('XS', 'Unisex - XS'), ('S', 'Unisex - S'), ('M', 'Unisex - M'), ('L', 'Unisex - L'), ('XL', 'Unisex - XL'), ('XXL', 'Unisex - XXL')], default='M', max_length=5),
        ),
    ]