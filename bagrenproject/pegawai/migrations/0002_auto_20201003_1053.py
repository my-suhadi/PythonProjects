# Generated by Django 3.1.1 on 2020-10-03 03:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('pegawai', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pangkat',
            name='pangkat_id',
            field=models.CharField(editable=False, max_length=40, primary_key=True, serialize=False),
        ),
    ]
