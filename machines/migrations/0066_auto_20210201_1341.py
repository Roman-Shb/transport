# Generated by Django 3.0 on 2021-02-01 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0065_auto_20210129_1259'),
    ]

    operations = [
        migrations.RenameField(
            model_name='minute_interval',
            old_name='end',
            new_name='ending',
        ),
        migrations.RenameField(
            model_name='minute_interval',
            old_name='start',
            new_name='starting',
        ),
    ]