# Generated by Django 5.0.3 on 2024-03-23 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0017_alter_customer_customer_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_code',
            field=models.CharField(default='1mxKkZ6al3Bjv1rw', max_length=16, unique=True),
        ),
        migrations.AlterField(
            model_name='session',
            name='session_key',
            field=models.CharField(default='AnfqiiOVVVPVgPvfft171SDixgh2K1kptAH4', max_length=50),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='visitorCode',
            field=models.CharField(default='kLIlRU6shSdksEOBPYw8vhZZ', max_length=16, unique=True),
        ),
    ]
