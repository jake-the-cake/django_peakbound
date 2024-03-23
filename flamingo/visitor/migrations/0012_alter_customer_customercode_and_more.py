# Generated by Django 5.0.1 on 2024-02-21 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0011_alter_customer_customercode_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customerCode',
            field=models.CharField(default='FnFZPJKAqkqFdgM6', max_length=16, unique=True),
        ),
        migrations.AlterField(
            model_name='session',
            name='session_key',
            field=models.CharField(default='V6xm8E3DVkwD0WHiSGDlYwllRrw7GMYm2C5I', max_length=50),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='visitorCode',
            field=models.CharField(default='5M9LQSlbQwpNNTba', max_length=16, unique=True),
        ),
    ]