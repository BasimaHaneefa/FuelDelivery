# Generated by Django 5.0.1 on 2024-01-16 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0002_tbl_fueltype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_fueltype',
            name='fueltype_name',
            field=models.CharField(max_length=20),
        ),
    ]
