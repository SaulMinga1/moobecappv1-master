# Generated by Django 4.0.6 on 2022-08-20 19:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='direccion',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
