# Generated by Django 3.0 on 2020-11-26 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sanctuary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connection_data',
            name='ip',
            field=models.CharField(max_length=100, verbose_name='IP адрес'),
        ),
        migrations.AlterField(
            model_name='object_list',
            name='description',
            field=models.CharField(max_length=100, verbose_name='Обозначение'),
        ),
        migrations.AlterField(
            model_name='object_list',
            name='ip',
            field=models.CharField(max_length=100, verbose_name='IP адрес'),
        ),
    ]
