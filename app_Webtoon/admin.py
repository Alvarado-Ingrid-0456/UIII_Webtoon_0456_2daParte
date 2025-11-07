from django.contrib import admin
from .models import Usuario, Webtoon
from django.utils.html import format_html

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id','nombre_usuario', 'email', 'tipo_usuario', 'fecha_registro')

@admin.register(Webtoon)
class WebtoonAdmin(admin.ModelAdmin):
    list_display = ('id','titulo', 'genero', 'autor', 'fecha_publicacion', 'estado', 'miniatura')
    list_filter = ('estado', 'genero')
    search_fields = ('titulo', 'genero')

    def miniatura(self, obj):
        if obj.portada:
            return format_html('<img src="{}" width="60" height="60" style="object-fit:cover;border-radius:6px" />', obj.portada)
        return "Sin portada"
    miniatura.short_description = "Portada"
