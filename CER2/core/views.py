from django.shortcuts import render
from django.http import HttpResponse
from .models import Correspondencia 


def home(request):
    busqueda = request.POST.get("buscar")            # Variable que contiene el valor de la busqueda por la barra de busqueda

    CorrespondenciasLista = Correspondencia.objects.all()    # CorrespondenciasLista almacena la tabla correspondencia
                                                             # para pasarsela como parametro al template "index" y poder listar
                                                             # sus elementos (correspondencias)   

    if busqueda:                                                                  # se filtran las correspondencias por la "busqueda"
       CorrespondenciasLista = Correspondencia.objects.filter(nro_residencia = busqueda)                                                              
    return render(request,'core/index.html',{"correspondencias": CorrespondenciasLista})    # Reinderiza el template index.hmtl
                                                                                            # para ser mostrado 
    