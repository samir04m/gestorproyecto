from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login , logout
from .decorador import * 
from .pruebas import * 

def Login(request):
    if request.user.is_authenticated:
        return redirect('inicio')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('inicio')
        else:
            return render(request, './user/login.html', {'error_message': 'Credenciales inválidas. Por favor, inténtalo de nuevo.'})
    else:
        return render(request, "./user/login.html")

def Logout(request):
    logout(request)
    return redirect('main:login')


@login_required
def inicio(request):
    user = request.user
    context = {
        'email': user.email,
        'first_name': user.first_name,
    }
    return render(request, "./user/inicio.html", context)

def nuevoproyecto(request):
    return render(request, "./user/nuevoproyecto.html")


def crearprojecto(request):
    return render(request, './user/createproject.html')

def asignar(request):
    gerentes =Usuario.objects.filter(rol='gerente')
    if request.method == 'POST':
        project_name = request.POST.get('project-name')
        project_descrip = request.POST.get('project-descrip')
        
        
        
        
    return render(request, './user/asignar.html' , {'gerentes':gerentes})


## pruebas 
def diagrama(request):
    return render(request, './datos.html')

