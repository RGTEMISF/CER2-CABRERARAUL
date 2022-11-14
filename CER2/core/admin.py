from django.contrib import admin
from .models import Residencia, Correspondencia


@admin.register(Residencia)                         # Registra el modelo Residencia
class ResideciaAdmin(admin.ModelAdmin):                    # Clase para mostrar las residencias en el panel de admin
    list_display = ('numero','dueño','telefono','mail')    # en una lista ordenada


@admin.register(Correspondencia)
class CorrespondenciaAdmin(admin.ModelAdmin):                         
    list_display = ('fecha_recepcion','conserje','remitente','destinatario','estado','nro_residencia')
