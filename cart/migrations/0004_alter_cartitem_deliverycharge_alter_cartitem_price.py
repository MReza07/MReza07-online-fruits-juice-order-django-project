# Generated by Django 4.1.2 on 2022-11-06 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_alter_cartitem_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='deliveryCharge',
            field=models.IntegerField(default=70),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]