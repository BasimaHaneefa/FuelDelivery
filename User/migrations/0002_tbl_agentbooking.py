# Generated by Django 4.2.7 on 2024-01-23 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0010_tbl_admin'),
        ('Guest', '0005_tbl_user'),
        ('TowingAgent', '0003_alter_tbl_vehicledetails_agent'),
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_agentbooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abooking_address', models.CharField(max_length=100)),
                ('abooking_date', models.DateField(auto_now_add=True)),
                ('abooking_status', models.CharField(default=0, max_length=5)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_location')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
                ('vdetails', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TowingAgent.tbl_vehicledetails')),
            ],
        ),
    ]
