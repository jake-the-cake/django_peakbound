# Generated by Django 5.0.1 on 2024-02-20 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0008_alter_customer_customercode_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customerCode',
            field=models.CharField(default='MYbHYujNbqzjxsRJ', max_length=16, unique=True),
        ),
        migrations.AlterField(
            model_name='session',
            name='session_key',
            field=models.CharField(default='OZ6BBrR4GEA8s4wEJKCHQn58LPD5Q4vXshez', max_length=50),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='visitorCode',
            field=models.CharField(default='atkInjxb7hJeZcKH', max_length=16, unique=True),
        ),
    ]