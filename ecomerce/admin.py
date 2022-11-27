from django.contrib import admin
from .models import CategoriaProd, Articulo

# Register your models here.
class CategoriaProdAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class ArticuloAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(CategoriaProd, CategoriaProdAdmin)
admin.site.register(Articulo, ArticuloAdmin)



