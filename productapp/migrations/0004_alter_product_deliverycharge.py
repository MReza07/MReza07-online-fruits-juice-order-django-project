# Generated by Django 4.1.2 on 2022-11-06 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0003_product_deliverycharge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='deliveryCharge',
            field=models.IntegerField(default=70),
        ),
    ]