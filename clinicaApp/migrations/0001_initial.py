# Generated by Django 5.2.4 on 2025-07-06 04:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('expediente', models.CharField(max_length=20, unique=True)),
                ('sala', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField()),
                ('cama', models.CharField(max_length=20)),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')], max_length=1)),
                ('direccion', models.TextField()),
                ('telefono', models.CharField(max_length=20)),
                ('profesion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='HistoriaClinica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('antecedentes_medicos', models.TextField()),
                ('fuma', models.BooleanField()),
                ('signos_vitales', models.TextField()),
                ('peso', models.FloatField()),
                ('talla', models.FloatField()),
                ('carnet', models.CharField(max_length=50)),
                ('resena_paciente', models.TextField()),
                ('procedimiento', models.TextField()),
                ('tratamiento', models.TextField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='historias_clinicas', to='clinicaApp.paciente')),
            ],
        ),
    ]
