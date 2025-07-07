from django.db import models

# models.py
class Paciente(models.Model):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    ]

    nombres = models.CharField(max_length=100, unique=True)
    apellidos = models.CharField(max_length=100, unique=True)
    expediente = models.CharField(max_length=20, unique=True)
    sala = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    cama = models.CharField(max_length=20)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    direccion = models.TextField()
    telefono = models.CharField(max_length=20)
    profesion = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombres} {self.apellidos} ({self.expediente})"

class HistoriaClinica(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='historias_clinicas')
    antecedentes_medicos = models.TextField()
    fuma = models.BooleanField()
    signos_vitales = models.TextField()
    peso = models.FloatField()
    talla = models.FloatField()
    carnet = models.CharField(max_length=50)
    resena_paciente = models.TextField()
    procedimiento = models.TextField()
    tratamiento = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Historia de {self.paciente} - {self.fecha_creacion.date()}"
