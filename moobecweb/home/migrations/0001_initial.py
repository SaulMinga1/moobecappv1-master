# Generated by Django 4.0.6 on 2022-08-04 22:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SolicitudPropietario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transact_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('brand', models.CharField(max_length=25)),
                ('model', models.CharField(max_length=25)),
                ('year', models.CharField(choices=[(2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023)], max_length=25)),
                ('mileage', models.CharField(max_length=25)),
                ('city', models.CharField(max_length=25)),
                ('estado', models.CharField(choices=[('pendiente', 'Pendiente'), ('aprobado', 'Aprobado'), ('rechazado', 'Rechazado'), ('revision', 'Necesita mas informacion')], max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('owner_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Solicitud Propietario',
                'verbose_name_plural': 'Solicitudes Propietarios',
            },
        ),
    ]
