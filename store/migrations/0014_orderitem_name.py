# Generated by Django 3.2.5 on 2021-08-04 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_auto_20210728_2032'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]