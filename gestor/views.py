from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login , logout
from .decorador import * 
from .pruebas import * 
from collections import defaultdict

## funciones propias 
from .mail import *
import random


def Login(request):
    # if request.user.is_authenticated:
    #     return redirect('inicio_administrator')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            usuario = Usuario.objects.get(usuario=user)
            
            if usuario.rol == 'administrador':
                return redirect('inicio_administrator')
            
            elif usuario.rol == 'gerente':
                
                return redirect('inicio_manager', usuario.id )
            
            elif usuario.rol == 'miembro':
                return redirect('pagina_miembro')
            else:
                return render(request, 'error.html', {'mensaje': 'Rol no reconocido'})
            
            
            
        else:
            return render(request, './user/login.html', {'error_message': 'Credenciales inválidas. Por favor, inténtalo de nuevo.'})
    else:
        return render(request, "./user/login.html")

def Logout(request):
    logout(request)
    return redirect('main:login')



# def inicio_administrador(request):
#     #usurios = 
#     usuarios = Usuario.objects.select_related('usuario').all()
    
#     # user = request.user()
#     # context = {
#     #     'email': user.email,
#     #     'first_name': user.first_name,
#     # }
#     # context = {
#     #     'email': 'user.email',
#     #     'first_name': 'user.first_name',
#     # }
#     print(usuarios)
#     return render(request, "./user/inicio_administrador.html", usuarios)


def inicio_administrador(request):
    usuarios = Usuario.objects.select_related('usuario').filter(rol='gerente')
    tipos_proyecto = ['Tipo I', 'Tipo II', 'Tipo III', 'Tipo IV']  # Lista de tipos de proyecto

    # Simular datos aleatorios para cada usuario y tipo de proyecto
    proyectos_por_usuario = {}
    for usuario in usuarios:
        proyectos_por_usuario[usuario] = {
            'tipo1': random.randint(0, 10),
            'tipo2': random.randint(0, 10),
            'tipo3': random.randint(0, 10),
            'tipo4': random.randint(0, 10),
        }

    context = {
        'proyectos_por_usuario': proyectos_por_usuario,
        'tipos_proyecto': tipos_proyecto,
    }
    return render(request, './user/inicio_administrador.html', context)


def inicio_gerente(request, id_gerente):
    usuario = Usuario.objects.get(id=id_gerente)
    proyectos = Proyecto.objects.filter(user=usuario)
    
    context = {
        'email': 'user.email',
        'first_name': 'user.first_name',
        'proyectos': proyectos,
    }
    return render(request, "./user/inicio_gerente.html", context)



def nuevoproyecto(request , codigo):
    proyecto = Proyecto.objects.filter(codigo=codigo).first()
    if request.method == 'POST':
        
        
        
        nombre_proyecto = request.POST.get('project-name')
        descripcion_proyecto = request.POST.get('project-description')
        fecha_creacion_proyecto = request.POST.get('project-creation-date')
        fecha_inicio_real = request.POST.get('project-start-date-real')
        fecha_finalizacion_real = request.POST.get('project-end-date-real')
        alcance_proyecto = request.POST.get('project-scope')
        estado_proyecto = request.POST.get('project-status')
        porcentaje_completado = request.POST.get('project-completion-percentage')
        tipo_proyecto = request.POST.get('project-type')
        lider_proyecto = request.POST.get('project-leader')
        grupo_proyecto = request.POST.get('project-group')
        categoria_proyecto = request.POST.get('project-category')
        antecedentes_proyecto = request.POST.get('project-background')
        fase_proyecto = request.POST.get('project-phase')
        comentarios_proyecto = request.POST.get('project-comments')

        
        # Crear una instancia de Proyecto y guardarla en la base de datos
        proyecto = Proyecto(
            name=nombre_proyecto,
            description=descripcion_proyecto,
            fecha_creacion=fecha_creacion_proyecto,
            fecha_inicio_real=fecha_inicio_real,
            fecha_finalizacion_real=fecha_finalizacion_real,
            alcance=alcance_proyecto,
            campo_estado=estado_proyecto,
            porcentaje_completado=porcentaje_completado,
            tipo=tipo_proyecto,
            lider=lider_proyecto,
            categoria=categoria_proyecto,
            antecedentes=antecedentes_proyecto,
            fase=fase_proyecto,
            comentarios=comentarios_proyecto
        )
        
        proyecto.save()
        
        
    contex  = {
        'project' : proyecto 
    }
    
    return render(request, "./user/nuevoproyecto.html" , contex ) 


def crearprojecto(request , codigo):        
    return render(request, './user/createproject.html')

def asignar(request):
    gerentes =Usuario.objects.filter(rol='gerente')
    
    if request.method == 'POST':
        project_name = request.POST.get('project-name')
        project_descrip = request.POST.get('project-descrip')
        project_managers = request.POST.get('project-managers')
        usuario = get_object_or_404(Usuario, id=project_managers)
        proyecto1 = Proyecto.objects.create(
            name= project_name, 
            codigo='PRO123', 
            description=project_descrip, 
            user=usuario, 
                                        )

        proyecto1.save()
        #enviar_correo_post(usuario.user.id,'valor')    
        return redirect('inicio_administrator')
    
    return render(request, './user/asignar.html' , {'gerentes':gerentes})


## pruebas 
def diagrama(request):
    return render(request, './datos.html')

def corre(request):
    enviar_correo_post('pueba','valor')
    return 0 

def gestion(request):
    return render(request, './user/barra_lateral.html')





