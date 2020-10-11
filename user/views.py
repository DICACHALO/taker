from django.shortcuts import render, redirect
from django.contrib.auth import logout as do_logout, authenticate, login as do_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from .forms import Myform, Myformregistro


# Create your views here.
def welcome(request):
    if request.user.is_authenticated:
        return render(request, "user/welcome.html")
    # En otro caso redireccionamos al login
    return redirect('/login')


def register(request):
    # Creamos el formulario de autenticación vacío
    form = Myformregistro()
    if request.method == "POST":

        # Añadimos los datos recibidos al formulario
        form = Myformregistro(data=request.POST)

        # Si el formulario es válido...
        if form.is_valid():

            # Creamos la nueva cuenta de usuario
            user = form.save()

            # Si el usuario se crea correctamente
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si llegamos al final renderizamos el formulario

    return render(request, "user/register.html", {'form': form})


def login(request):
    # Creamos el formulario de autenticación vacío
    form = Myform()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = Myform(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "user/login.html", {'form': form})


def logout(request):

    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')
