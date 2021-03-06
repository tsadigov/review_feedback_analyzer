# Generated by Django 2.2.6 on 2019-11-18 13:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyzer', '0014_auto_20191118_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='analyze_date',
            field=models.DateField(default='1990-10-10', verbose_name=datetime.datetime(2019, 11, 18, 17, 41, 26, 625086)),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='product',
            name='url',
            field=models.CharField(default='null', max_length=1000),
        ),
    ]
