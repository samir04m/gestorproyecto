from django.contrib import admin
from .models import Usuario, Equipo, Proyecto, Grupo, Programa, Hito, Tarea, ComentarioTarea, MatrizRiesgo 

admin.site.register(Usuario)
admin.site.register(Equipo)
admin.site.register(Proyecto)
admin.site.register(Grupo)
admin.site.register(Programa)
admin.site.register(Hito)
admin.site.register(Tarea)
admin.site.register(ComentarioTarea)
admin.site.register(MatrizRiesgo)

