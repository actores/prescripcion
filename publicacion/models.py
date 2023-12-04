from django.db import models

# Create your models here.
# class Obra(models.Model):
#     id = models.AutoField(primary_key=True)
#     numeroObra = models.CharField(max_length=50)
#     numeroExplotacion = models.CharField(max_length=50)
#     titulo = models.CharField(max_length=255, verbose_name='Título')
#     pais = models.CharField(max_length=50, verbose_name='País')
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
#     updated_at = models.DateTimeField(auto_now=True, verbose_name='Actualizado el')

#     def __str__(self):
#         texto = "{0} ({1})"
#         return texto.format(self.titulo, self.pais)
    

# from django.db import models

# class DetalleObra(models.Model):
#     id = models.AutoField(primary_key=True)
#     obra = models.ForeignKey('Obra', on_delete=models.CASCADE, related_name='detalles')
#     artista = models.CharField(max_length=255)
#     personaje = models.CharField(max_length=255)
#     estado = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         texto = "{0} - {1} ({2})"
#         return texto.format(self.obra.titulo, self.personaje, self.estado)


class Serie(models.Model):
    titulo = models.CharField(max_length=255, verbose_name='Título')
    pais = models.CharField(max_length=50, verbose_name='País')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Actualizado el')
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.titulo, self.pais)
    
class Explotacion(models.Model):
    cadena = models.CharField(max_length=50, verbose_name='Cadena')
    anio = models.CharField(max_length=50, verbose_name='Año')
    serie = models.ForeignKey('Serie', on_delete=models.CASCADE, related_name='explotacion_serie')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Actualizado el')

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.cadena, self.anio)

class Repertorio(models.Model):
    tituloCapitulo = models.CharField(max_length=255, verbose_name='Título')
    numeroActor = models.CharField(max_length=50)
    personaje = models.CharField(max_length=255, verbose_name='Personaje')
    nombreActor = models.CharField(max_length=255, verbose_name='NombreActor')
    numeroObra =  models.CharField(max_length=50)
    explotacion = models.ForeignKey('Explotacion', on_delete=models.CASCADE, related_name='repertorio_explotacion')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Actualizado el')

    def __str__(self):
        texto = "{0}"
        return texto.format(self.tituloCapitulo
    )