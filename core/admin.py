from django.contrib import admin
from .models import Perfil, Equipo, Post

@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'año_fundacion', 'victorias') 
    search_fields = ('nombre',) 
    list_filter = ('año_fundacion',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor')
    search_fields = ('titulo', 'autor')
    list_filter = ('autor',)

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('user', 'equipo_favorito')
    search_fields = ('user__username',)