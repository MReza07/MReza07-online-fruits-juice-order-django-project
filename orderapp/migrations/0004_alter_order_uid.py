# Generated by Django 4.1.2 on 2022-11-09 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderapp', '0003_remove_order_deliverycharge_remove_order_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='uid',
            field=models.IntegerField(default=0),
        ),
    ]
