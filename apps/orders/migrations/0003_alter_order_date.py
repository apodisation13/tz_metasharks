# Generated by Django 3.2.8 on 2022-10-12 15:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20221012_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата оформления заказ'),
        ),
    ]
