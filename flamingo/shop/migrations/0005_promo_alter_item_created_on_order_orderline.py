# Generated by Django 5.0.1 on 2024-02-20 17:38

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_item_created_on'),
        ('visitor', '0008_alter_customer_customercode_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Promo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=12)),
            ],
        ),
        migrations.AlterField(
            model_name='item',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 20, 17, 38, 28, 750969)),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_code', models.CharField(max_length=24)),
                ('status', models.CharField(max_length=10)),
                ('total', models.FloatField(default=0)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visitor.user')),
                ('promos', models.ManyToManyField(to='shop.promo')),
            ],
        ),
        migrations.CreateModel(
            name='OrderLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.FloatField(default=0)),
                ('promo_price', models.FloatField(default=0)),
                ('promo_code', models.CharField(max_length=12)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.item')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.order')),
            ],
        ),
    ]
