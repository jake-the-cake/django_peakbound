# Generated by Django 5.0.1 on 2024-02-21 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0009_alter_customer_customercode_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customerCode',
            field=models.CharField(default='hJzV8HZHYkeTccPd', max_length=16, unique=True),
        ),
        migrations.AlterField(
            model_name='session',
            name='session_key',
            field=models.CharField(default='lH8rVJaB78kCZ6strWI0UUbego10ocjEBn1k', max_length=50),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='visitorCode',
            field=models.CharField(default='LHkI7kdmHnj4isXR', max_length=16, unique=True),
        ),
    ]
