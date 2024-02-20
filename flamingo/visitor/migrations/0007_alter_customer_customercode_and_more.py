# Generated by Django 5.0.1 on 2024-02-20 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0006_alter_customer_customercode_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customerCode',
            field=models.CharField(default='JWXGAgOSgLZWArIz', max_length=16, unique=True),
        ),
        migrations.AlterField(
            model_name='session',
            name='session_key',
            field=models.CharField(default='6eItzTT5fC1JqoSVhjMIuV3nWzx8ulNMH0Xc', max_length=50),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='visitorCode',
            field=models.CharField(default='SmOuGirhBLKiGCwv', max_length=16, unique=True),
        ),
    ]
