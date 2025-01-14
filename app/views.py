from django.shortcuts import render
from .models import Empresa, Trabajador, Documento

def explorer_view(request):
    empresas = Empresa.objects.all()
    trabajadores = Trabajador.objects.all()
    documentos = Documento.objects.all()

    # Se obtienen todos los campos para filtrar
    return render(request, 'app/seleccion_tablas.html', {
        'empresas': empresas,
        'trabajadores': trabajadores,
        'documentos': documentos,
    })


def filtros(request):
    cargo_filtrado = request.GET.get('cargo', '')
    trabajadores = Trabajador.objects.all()

    if cargo_filtrado:
        trabajadores = trabajadores.filter(cargo=cargo_filtrado)

    cargos = Trabajador.objects.values_list('cargo', flat=True).distinct()

    return render(request, 'app/seleccion_tablas.html', {'trabajadores': trabajadores, 'cargos': cargos})