from django.db import models
from .choices import estados


class Residencia(models.Model):
    numero = models.IntegerField(primary_key= True)
    dueño = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    mail = models.EmailField()

    def __str__(self):
        return str(self.numero)




class Correspondencia(models.Model):
    fecha_recepcion = models.DateField()
    conserje = models.CharField(max_length=50)
    remitente= models.CharField(max_length=50)
    destinatario = models.CharField(max_length=50)
    estado = models.CharField(max_length=2, choices=estados, default='NE')
    nro_residencia = models.ForeignKey(Residencia, on_delete=models.RESTRICT)
       
    def __str__(self):
        return str(self.nro_residencia)


