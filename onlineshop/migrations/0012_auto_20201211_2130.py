# Generated by Django 3.1.2 on 2020-12-11 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlineshop', '0011_auto_20201211_2126'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='division',
            new_name='region',
        ),
    ]
