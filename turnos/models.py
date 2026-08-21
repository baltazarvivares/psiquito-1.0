from django.contrib.auth.models import AbstractUser
from django.db import models


class Persona(AbstractUser):
    # first_name, last_name, email y username ya vienen de AbstractUser
    dni = models.CharField(max_length=20, unique=True)
    genero = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class ObraSocial(models.Model):
    numero = models.CharField(max_length=20, primary_key=True)
    nombreObraSocial = models.CharField(max_length=100)

    def __str__(self):
        return self.nombreObraSocial


class Paciente(Persona):
    fechaNacimiento = models.DateField()
    # relación "tiene" (1 a 1) con obraSocial; aporte es atributo de la relación
    obraSocial = models.OneToOneField(
        ObraSocial,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="paciente",
    )
    aporte = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )  # lo que la obra social le paga al profesional


class Psicologo(Persona):
    matricula = models.CharField(max_length=50, unique=True)


class Horario(models.Model):
    id = models.AutoField(primary_key=True)
    nomDia = models.CharField(max_length=20)
    horaInicio = models.TimeField()
    horaFin = models.TimeField()
    # relación "atiende" (1 psicologo a N horarios)
    psicologo = models.ForeignKey(
        Psicologo, on_delete=models.CASCADE, related_name="horarios"
    )

    class Meta:
        unique_together = ("nomDia", "psicologo")

    def __str__(self):
        return f"{self.nomDia} ({self.horaInicio}-{self.horaFin})"


class Turno(models.Model):
    idTurno = models.AutoField(primary_key=True)
    fecha = models.DateField()
    hora = models.TimeField()
    modalidad = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    # relación "asiste" (1 paciente a N turnos)
    paciente = models.ForeignKey(
        Paciente, on_delete=models.CASCADE, related_name="turnos"
    )
    # relación "atiende" (1 psicologo a N turnos)
    psicologo = models.ForeignKey(
        Psicologo, on_delete=models.CASCADE, related_name="turnos"
    )

    def __str__(self):
        return f"Turno {self.idTurno} - {self.fecha} {self.hora}"


class Factura(models.Model):
    numeroFactura = models.AutoField(primary_key=True)
    hora = models.TimeField()
    fecha = models.DateField()
    # relación "genera" (1 a 1 con turno)
    turno = models.OneToOneField(
        Turno, on_delete=models.CASCADE, related_name="factura"
    )

    def __str__(self):
        return f"Factura {self.numeroFactura}"