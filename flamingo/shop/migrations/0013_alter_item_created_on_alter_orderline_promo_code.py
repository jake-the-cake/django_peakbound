# Generated by Django 5.0.1 on 2024-02-22 17:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_remove_orderline_order_order_lines_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 22, 17, 58, 33, 906305)),
        ),
        migrations.AlterField(
            model_name='orderline',
            name='promo_code',
            field=models.CharField(default='xxxxxxxx', max_length=12),
        ),
    ]
