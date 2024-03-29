# Generated by Django 5.0.1 on 2024-02-06 21:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_code', models.CharField(max_length=24)),
                ('created_on', models.DateTimeField(default=datetime.datetime(2024, 2, 6, 21, 40, 14, 195817))),
                ('created_by', models.CharField(default='Jason', max_length=100)),
                ('cost', models.FloatField(default=0)),
                ('price', models.FloatField(default=0)),
                ('stock', models.IntegerField(default=1)),
                ('description', models.TextField(default='description')),
            ],
        ),
    ]
