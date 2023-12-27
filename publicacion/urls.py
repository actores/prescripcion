from django.urls import path
from . import views


urlpatterns = [
    
    # path('', views.listarSeries),
    path('obras/', views.series),
    path('obras/anteriores/', views.seriesOld),
    path('distribuciones/<id>', views.detalleDistribucion, name='detalle_distribucion'),
    path('detalleExplotacion/<id>', views.detalleExplotacion, name='detalle_explotacion'),
    path('detalleRepertorio/<idSerie>/<cadena>/<anio>', views.detalleRepertorio, name='detalle_repertorio'),


    # path('', views.series),
    path('', views.inicio),
    


]