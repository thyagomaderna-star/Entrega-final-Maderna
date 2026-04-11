from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm, EditarPerfilForm
from .models import Perfil, Equipo, Post, User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
#Inicio

def inicio(request):
    return render(request, 'core/inicio.html')

#Registro de usaurio
def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            Perfil.objects.create(user=user)
            login(request, user)
            return redirect('inicio')
    else:
        form = RegistroForm()
    return render(request, 'core/registro.html', {'form': form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("inicio")
    else:
        form = AuthenticationForm()
    return render(request, "core/login.html", {"form": form})

@login_required
def editar_perfil(request):
    perfil, created = Perfil.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        formulario = EditarPerfilForm(request.POST, request.FILES, instance=perfil)

        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
    else:
        formulario = EditarPerfilForm(instance=perfil)
    return render(request, "core/editar_perfil.html", {"form": formulario})

class PerfilDetailView(LoginRequiredMixin, DetailView):
    model = Perfil
    template_name = "core/perfil_detail.html"
    context_object_name = "perfil"

    def get_object(self):
        perfil, created = Perfil.objects.get_or_create(user=self.request.user)
        return perfil

class UserListView(LoginRequiredMixin,ListView):
    model = User
    template_name = 'core/user_list.html'
    context_object_name = 'usuarios'

#Equipos

#Lista de todos los equipos
class EquipoListView(LoginRequiredMixin,ListView):
    model = Equipo
    template_name = "core/equipos/equipo_list.html"
    context_object_name = "equipos"

#Detalle de equipo
class EquipoDetailView(LoginRequiredMixin,DetailView):
    model = Equipo
    template_name = "core/equipos/equipo_detail.html"

#Crear equipo
class EquipoCreateView(LoginRequiredMixin, CreateView):
    model = Equipo
    fields = ['nombre', 'victorias', 'año_fundacion', 'escudo']
    template_name = "core/equipos/equipo_form.html"
    success_url = reverse_lazy('equipo_list')

#Editar equipo
class EquipoUpdateView(LoginRequiredMixin, UpdateView):
    model = Equipo
    fields = ['nombre', 'victorias', 'año_fundacion', 'escudo']
    template_name = "core/equipos/equipo_form.html"
    success_url = reverse_lazy('equipo_list')

#Borrar un equipo
class EquipoDeleteView(LoginRequiredMixin, DeleteView):
    model = Equipo
    template_name = "core/equipos/equipo_confirm_delete.html"
    success_url = reverse_lazy('equipo_list')

# Post

#Lista de Todos los Posts

class PostListView(LoginRequiredMixin,ListView):
    model = Post
    template_name = "core/post/post_list.html"
    context_object_name = "post"

#Detalle Post

class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post
    template_name = "core/post/post_detail.html"

#Crear Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["titulo", "subtitulo", "contenido", "autor"] 
    template_name = "core/post/post_form.html"
    success_url = reverse_lazy('post_list')

#Editar Post

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ["titulo", "subtitulo", "contenido", "autor"] 
    template_name = "core/post/post_form.html"
    success_url = reverse_lazy('post_list')

#Borrar Equipo

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    template_name = "core/post/post_confirm_delete.html"
    success_url = reverse_lazy('post_list')