# Generated by Django 4.1.2 on 2022-11-06 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0002_alter_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='deliveryCharge',
            field=models.IntegerField(default=0.0),
        ),
    ]