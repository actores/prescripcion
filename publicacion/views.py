from django.db import connection
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import Serie,Explotacion,Repertorio,Distribucion,RepertorioOld
# # from .models import Obra,DetalleObra
from django.db.models import Q
# from django.http.response import JsonResponse

# # Create your views here.
# def home(request):
#     obras = Obra.objects.all()
#     return render(request, "obras.html", {
#         'obras': obras
#     })

# Create your views here.
def listarSeries(request):
    series = Serie.objects.all()
    return render(request, "series.html", {
        'series' : series
    })

def inicio(request):
    return render(request, 'index.html')


# def series(request):
#     return render(request, 'series.html')

def seriesOld(request):
    seriesOld = RepertorioOld.objects.all()
    return render(request, 'seriesOld.html', {
        'seriesOld' : seriesOld
    })

def series(request):
    # series = list(Serie.objects.values())
    # seriesOld = list(RepertorioOld.objects.values())
    series = Serie.objects.all()
    seriesOld = RepertorioOld.objects.all()

    # data = {
    #     'series':series,
    #     'seriesOld' : seriesOld
    #     }
    # return JsonResponse(data)
    return render(request, 'series.html', {
        'series':series,
        'seriesOld' : seriesOld
    })


def detalleDistribucion(request,id):
    serie = get_object_or_404(Serie, id=id)
    distribuciones = (
        Explotacion.objects
        .filter(serie_id=36811)
        .values('distribucion_id', 'distribucion__anio', 'distribucion__tipo')
        .distinct()
    )
    return render(request, "distribuciones.html", {
        "distribuciones" : distribuciones,
        "serie": serie
    })

def detalleExplotacion(request, id):
    # Asegúrate de obtener la Serie correctamente
    serie = get_object_or_404(Serie, id=id)

    # Ejecutar la consulta SQL cruda
    consulta_sql = """SELECT cadena, anio, created_at FROM publicacion_explotacion WHERE serie_id = %s GROUP BY cadena, anio, created_at;"""

    try:
        with connection.cursor() as cursor:
            cursor.execute(consulta_sql, [id])
            explotaciones = cursor.fetchall()

        # Imprime los resultados de manera más detallada
        for explotacion in explotaciones:
            print(explotacion)

    except Exception as e:
        print(f"Error al ejecutar la consulta SQL: {e}")
        explotaciones = []

    return render(request, "explotaciones.html", {
        'serie': serie,
        'explotaciones': explotaciones
    })



def detalleRepertorio(request, idSerie, cadena, anio):
    serie = Serie.objects.get(id=idSerie)

    noIdentificados = Repertorio.objects.filter(
        explotacion__serie_id=idSerie,
        explotacion__cadena=cadena,
        explotacion__anio=anio,
        numeroActor=0
    ).values('personaje', 'nombreActor').distinct()

    noSocios = Repertorio.objects.filter(
        explotacion__serie_id=idSerie,
        explotacion__cadena=cadena,
        explotacion__anio=anio,
        Q(numeroActor__gt=0) & ~Q(numeroActor='F')  # Aquí encapsulamos todo en el filter
    ).values('personaje', 'nombreActor').distinct()
    
    fallecidos = Repertorio.objects.filter(
        explotacion__serie_id=idSerie,
        explotacion__cadena=cadena,
        explotacion__anio=anio,
        numeroActor='F'
    ).values('personaje', 'nombreActor').distinct()

    return render(request, "repertorio.html", {
        'serie': serie,
        'noIdentificados': noIdentificados,
        'noSocios': noSocios,
        'cadena': cadena,
        'anio': anio,
        'fallecidos': fallecidos
    })

# def detalleObra(request, id):
#     detallado = DetalleObra.objects.filter(obra_id=id)
#     return render(request, "detalleObra.html",{
#         'detallado':detallado
#     })

# def buscarObra(request):
#     obraBusqueda = request.POST['busqueda']
#     print(request)
#     # obras = Obra.objects.filter(titulo__icontains=obraBusqueda)
#     obras = Obra.objects.filter(
#             Q(titulo__icontains=obraBusqueda) |
#             Q(numeroObra__icontains=obraBusqueda) |
#             Q(numeroExplotacion__icontains=obraBusqueda) |
#             Q(pais__icontains=obraBusqueda)
#         )
#     return render(request, "obras.html", {
#         'obras': obras
#     })


def buscarSerie(request):
    serieBusqueda = request.POST['busqueda']
    series = Serie.objects.filter(
            Q(id__icontains=serieBusqueda) |
            Q(titulo__icontains=serieBusqueda) |
            Q(pais__icontains=serieBusqueda) 
        )
    return render(request, "series.html", {
        'series': series
    })