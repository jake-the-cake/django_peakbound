# Generated by Django 5.0.2 on 2024-03-07 18:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_alter_item_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 7, 18, 51, 33, 236984, tzinfo=datetime.timezone.utc)),
        ),
    ]