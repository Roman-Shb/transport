# Generated by Django 3.0 on 2020-11-26 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0062_auto_20201118_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='main_channel',
            field=models.CharField(blank=True, choices=[], max_length=5, null=True, verbose_name='Канал'),
        ),
    ]
