# Generated by Django 3.1.1 on 2020-10-03 04:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('pegawai', '0005_auto_20201003_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pangkat',
            name='nomer_urut',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
