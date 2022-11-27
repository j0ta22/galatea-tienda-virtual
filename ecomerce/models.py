from email.policy import default
from tabnanny import verbose
from django.db import models

# Create your models here.
class CategoriaProd(models.Model):
    nombre = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="categoriaprod"
        verbose_name_plural="categoriasprod"

    def __str__(self):
        return self.nombre

class Articulo(models.Model):
    codigo = models.CharField(max_length=6)
    nombre = models.CharField(max_length=20)
    categorias = models.ForeignKey(CategoriaProd, on_delete = models.CASCADE)
    detalle = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to = 'ecomerce', null=True, blank=True)
    precio = models.FloatField()
    disponibilidad = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="articulo"
        verbose_name_plural="articulos"
        

    #def __str__(self):
        #return 'El nombre es %s, la seccion es %s y el precio es %s' % (self.detalle, self.seccion, self.precio)

