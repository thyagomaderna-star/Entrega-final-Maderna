from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Perfil, Post, Equipo

#SECCIÓN USUARIOS

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email")
    first_name = forms.CharField(max_length=30, required=True, label="Nombre")
    last_name = forms.CharField(max_length=30, required=True, label="Apellido")
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class EditarPerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['avatar', 'biografia', 'fecha_nacimiento', 'equipo_favorito'] 

#SECCIÓN EQUIPOS 

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['nombre', 'año_fundacion', 'victorias', 'escudo']

class BuscarEquipoForm(forms.Form):
    nombre = forms.CharField(required=False, label="Nombre del equipo")


#SECCIÓN POSTS

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'subtitulo', 'contenido']

class BuscarPostForm(forms.Form):
    titulo = forms.CharField(required=False, label="Título del post")