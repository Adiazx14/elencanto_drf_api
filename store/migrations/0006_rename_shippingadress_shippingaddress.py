# Generated by Django 3.2.5 on 2021-07-23 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_orderitem_order'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ShippingAdress',
            new_name='ShippingAddress',
        ),
    ]
