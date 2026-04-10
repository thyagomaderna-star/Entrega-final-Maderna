from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm, EditarPerfilForm
from .models import Perfil


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
    usuario = request.user 

    if request.method == 'POST':

        formulario = EditarPerfilForm(request.POST, instance=usuario)

        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
    else:
        formulario = EditarPerfilForm(instance=usuario)

    return render(request, "core/editar_perfil.html", {"mi_form": formulario})