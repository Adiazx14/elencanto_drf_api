# Generated by Django 3.2.5 on 2021-08-23 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_order_is_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_method',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
