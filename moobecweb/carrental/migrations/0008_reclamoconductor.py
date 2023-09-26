# Generated by Django 4.0.6 on 2022-08-12 00:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('carrental', '0007_reservas'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReclamoConductor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transact_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('incident_type', models.CharField(max_length=25)),
                ('claim_status', models.CharField(max_length=25)),
                ('cost', models.FloatField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Reclamo',
                'verbose_name_plural': 'Reclamo Conductor',
            },
        ),
    ]
