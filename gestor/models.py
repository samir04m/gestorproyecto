from django.db import models
from django.contrib.auth.models import User
from markupfield.fields import MarkupField
from django.contrib.auth import models as authmodels


class Usuario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    ROLES = (
        ('administrador', 'Administrador'),
        ('gerente', 'Gerente'),
        ('miembro', 'Miembro'),
    )
    rol = models.CharField(max_length=20, choices=ROLES)
    equipos = models.ManyToManyField('Equipo', related_name='miembros')
    
    

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()



class Proyecto(models.Model):
    
    STATES = (
        ('abierto', 'Abierto'),
        ('suspendido', 'Suspendido'),
        ('cerrado', 'Cerrado'),
    )
    
    # Definir las opciones para los campos
    CATEGORIA = (
        ('I', 'Tipo I'),
        ('II', 'Tipo II'),
        ('III', 'Tipo III'),
        ('IV', 'Tipo IV'),
    )

    FASES = (
        ('inicio', 'Inicio'),
        ('planeacion', 'Planeación'),
        ('ejecucion', 'Ejecución'),
        ('monitoreo_control', 'Monitoreo y Control'),
        ('cierre', 'Cierre'),
    )
    # abierto , suspendido  , cerrado
    TYPE =(
        ('abierto', 'Proyectos Integración'),
        ('suspendido', 'Necesidades entrega operación'),
        ('desarollo', 'Proyectos Producto Propio'),
        ('cerrado', 'Cerrado'),
    )
        
    name = models.CharField(max_length=100) 
    codigo = models.CharField(max_length=100) ## auto increment - automatico 
    description = models.TextField() 
    
    fecha_creacion = models.DateField(auto_now_add=True) 
    fecha_inicio_planeada = models.DateField(null=True, blank=True) # 
    fecha_inicio_real = models.DateField(null=True, blank=True) ##  automatica 
    fecha_finalizacion_planeada = models.DateField(null=True, blank=True) 
    fecha_finalizacion_real = models.DateField(null=True, blank=True) # automatica 
    
    alcance = models.TextField()
    estado = models.CharField(max_length=50 , choices=STATES) ## generar tipos 
    
    porcentaje_completado = models.IntegerField(default=0) ## automatico 
    tipo = models.CharField(max_length=50 , choices = TYPE ) ##  proyecto o necesidad 
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE) 
    lider = models.CharField(max_length=100) ## automatico 
    grupo = models.ManyToManyField('Grupo', related_name='proyectos', blank=False) ## grupo asociado lista desplegable - brayan 
    
    categoria = models.CharField(max_length=100 , choices = CATEGORIA) # desplegable  lista desplegable - brayan 
    antecedentes = models.TextField() ### 
    fase = models.CharField(max_length=100 ,choices = FASES) ### lista , brayan los tiene 
    programas = models.ManyToManyField('Programa', related_name='proyectos', blank=False ) # lista falta llegar 
    comentarios = models.TextField(null=True, blank=True) ## 
    spi = models.FloatField(default=0) ## indicador 
    es = models.FloatField(default=0) ## formualdo 
    
    columna = models.BooleanField(default=False) ##  asignado 


#! falta 
class Grupo(models.Model):
    nombre = models.CharField(max_length=100)
    asociados = models.TextField()
    cluster = models.TextField()
    
#! no lo tenemos 
class Programa(models.Model):
    nombre = models.CharField(max_length=100)


class Hito(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    asignado = models.ForeignKey(Usuario,on_delete=models.CASCADE) ## general una relacion de uno a muchos 



#! validar hitos donde se encuentran 
class Tarea(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    hito = models.ForeignKey(Hito, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    asignado = models.ForeignKey(Usuario , on_delete=models.CASCADE)
    estado = models.CharField(max_length=100)  # Lista desplegable: SIN iniciar, En Proceso, Finalizada 
    dependencias = models.ManyToManyField('self', symmetrical=False, blank=True)





#* leciones aprendidas 
class ComentarioTarea(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    identificando_problema = models.TextField()
    causa = models.TextField()
    solucion = models.TextField()
    planes_mejora_aplicados = models.TextField()
    resultados_planes_mejora = models.TextField()
    
    def str(self):
        return f"Comentario para {self.tarea.nombre}"

class MatrizRiesgo(models.Model):
    # muy grave -- rojo 
    # importante -- naraja
    # apreciable -- amarillo 
    # marginal -- verde 
    
    RIESGOS = (
        ('grave', 'Muy grave'),
        ('importante', 'Importante'),
        ('apreciable', 'Apreciable'),
        ('marginal', 'Marginal'),
    )
    
    
        
    GAVEDAD = {
        ('Bajo2', 'Muy Bajo'),
        ('bajo1', 'Bajo'),
        ('medio', 'Medio'),
        ('alto1', 'Alto'),
        ('alto2', 'Muy Alto'),
    }
    
    
    #*Nombre Del Riesgo identificado	
    #*Descripción del riesgo	
    #* Causas del Riesgo	
    #* Plan de mitigacion	
    #*Descripcion del impacto en alcance	
    #* Descripcion del impacto en Tiempo	
    #* Descripcion del Impacto costo	
    #* Probabilidad (Ocurrencia)	
    #* Gravedad Impacto	
    #* Valor de riesgo	
    #* Nivel de Riesgo
	#* Riesgo se materializo

    
    
    nombre = models.CharField(max_length=200 )
    descripcion = models.TextField()
    Causas = models.CharField(max_length=200 )
    Plan = models.CharField(max_length=200 )
    Descripcion_tiempo = models.CharField(max_length=200 )
    Descripcion_alcance = models.CharField(max_length=200 )
    Descripcion_costo = models.CharField(max_length=200 )
    probavilidad = models.CharField(max_length=20, choices=GAVEDAD)
    gravedad = models.CharField(max_length=20, choices=GAVEDAD)
    riesgo = models.CharField(max_length=20, choices=RIESGOS)
    materializo = models.CharField(max_length=200 ) 
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    acciones_mitigacion = models.TextField()

    def str(self):
        return f"Matriz de Riesgo para {self.proyecto.name}"


class Documentos(models.Model):
    titulo = models.CharField(max_length = 100)
    descriocion = models.TextField()
    link = models.URLField()
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)

class Costos(models.Model):
    contrato = models.CharField(max_length = 100)
    objeto = models.TextField()
    tipo = models.CharField(max_length = 100)
    aliado = models.CharField(max_length = 200)
    contrato_aliado = models.CharField(max_length = 100)
    backlog = models.TextField()
    one_time = models.TextField()
    recurrente = models.TextField()
    meses = models.CharField(max_length = 100)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    
    


## prueba 

class Tablero(models.Model):
    titulo = models.CharField(max_length=200)
    proyect =  models.OneToOneField(Proyecto, on_delete=models.CASCADE, related_name='tablero')

    def __str__(self):
        return self.titulo

    def nueva_columna(self, titulo):
        c = Columna(titulo=titulo, tablero=self)
        c.save()
        return c

class Columna(models.Model):
    titulo = models.CharField(max_length=200)
    tablero = models.ForeignKey(Tablero, related_name='columnas', on_delete=models.CASCADE)  

    def __str__(self):
        return "%s - %s" % (self.titulo, self.tablero)

    def nueva_tarjeta(self, titulo, descripcion):
        t = Tarjeta(titulo=titulo, descripcion=descripcion, columna=self)
        t.save()
        return t

class Postit(models.Model):
    titulo = models.CharField(max_length=200)
    columna = models.ForeignKey(Columna, related_name='tarjetas', on_delete=models.CASCADE)  
    actividad = models.ForeignKey(Hito, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.titulo

class Tarjeta(Postit):
    descripcion = MarkupField()
    participantes = models.ManyToManyField(authmodels.User)

    def __str__(self):
        return self.titulo

class Recurso(models.Model):
    nombre = models.CharField(max_length=200)
    archivo = models.FileField(upload_to='recursos')
    tarjeta = models.ForeignKey(Tarjeta, on_delete=models.CASCADE)

