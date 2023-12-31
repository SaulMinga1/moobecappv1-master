# Generated by Django 4.0.6 on 2022-08-19 04:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DOB', models.DateField(null=True)),
                ('birth_place', models.CharField(max_length=50, null=True)),
                ('licencia_conductor', models.CharField(max_length=50, null=True)),
                ('fecha_emision_licencia', models.DateField(null=True)),
                ('pais_emision_licencia', models.CharField(max_length=50, null=True)),
                ('numero_telefono', models.CharField(max_length=12, null=True)),
                ('direccion', models.CharField(max_length=12, null=True)),
                ('ciudad', models.CharField(max_length=12, null=True)),
                ('pais', models.CharField(max_length=12, null=True)),
                ('bio', models.TextField()),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
