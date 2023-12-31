# Generated by Django 4.0.6 on 2022-08-04 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitudpropietario',
            name='estado',
            field=models.CharField(choices=[('pendiente', 'Pendiente'), ('aprobado', 'Aprobado'), ('rechazado', 'Rechazado'), ('revision', 'Necesita mas informacion')], default='Pendiente', max_length=20),
        ),
        migrations.AlterField(
            model_name='solicitudpropietario',
            name='year',
            field=models.IntegerField(choices=[(2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023)]),
        ),
    ]
