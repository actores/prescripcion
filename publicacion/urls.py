from django.urls import path
from . import views


urlpatterns = [
    # path('', views.listarSeries),
    path('', views.series),
    path('api/listar/series/', views.apiListarSeries),
    path('buscarSerie/', views.buscarSerie),
    path('detalleExplotacion/<id>', views.detalleExplotacion, name='detalle_explotacion'),
    path('detalleExplotacion/detalleRepertorio/<idSerie>/<cadena>/<anio>', views.detalleRepertorio, name='detalle_repertorio')
]