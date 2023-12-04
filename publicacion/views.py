from django.db import connection
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import Serie,Explotacion,Repertorio
# # from .models import Obra,DetalleObra
from django.db.models import Q

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

def detalleExplotacion(request, id):
    # Asegúrate de obtener la Serie correctamente
    serie = get_object_or_404(Serie, id=id)

    # Ejecutar la consulta SQL cruda
    consulta_sql = """SELECT cadena, anio FROM publicacion_explotacion WHERE serie_id = %s GROUP BY cadena, anio;"""

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

    sql_query = """
    SELECT r.*, e.cadena, e.anio
    FROM publicacion_repertorio AS r
    INNER JOIN publicacion_explotacion AS e ON r.explotacion_id = e.id
    WHERE e.serie_id = %s AND e.cadena = %s AND e.anio = %s;
    """
    repertorio = Repertorio.objects.raw(sql_query, [idSerie, cadena, anio])
    
    return render(request, "repertorio.html", {
        'serie': serie,
        'repertorio': repertorio
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