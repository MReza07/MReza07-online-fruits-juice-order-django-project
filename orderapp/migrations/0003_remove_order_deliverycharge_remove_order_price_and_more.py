# Generated by Django 4.1.2 on 2022-11-09 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orderapp', '0002_order_deliverycharge_order_price_order_qty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='deliveryCharge',
        ),
        migrations.RemoveField(
            model_name='order',
            name='price',
        ),
        migrations.RemoveField(
            model_name='order',
            name='qty',
        ),
    ]