# Generated by Django 4.2.5 on 2023-09-11 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_orders_paid_orders_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='paid',
            field=models.CharField(default='Not specified', max_length=100),
        ),
    ]
