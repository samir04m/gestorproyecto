from django.contrib.auth.models import User
from .models import Usuario, Equipo, Proyecto, Grupo, Programa, Hito, Tarea, ComentarioTarea, MatrizRiesgo, Documentos, Costos

def cargar_datos_ejemplo():
    # Obtener o crear usuarios de ejemplo
    usuario1, created = User.objects.get_or_create(username='usuario1', email='usuario1@example.com', password='password1')
    usuario2, created = User.objects.get_or_create(username='usuario2', email='usuario2@example.com', password='password2')
    usuario3, created = User.objects.get_or_create(username='usuario3', email='usuario3@example.com', password='password3')
    print("parte 1.")
    
    # Crear equipos de ejemplo
    equipo1 = Equipo.objects.create(nombre='Equipo 1', descripcion='Descripción del Equipo 1')
    equipo2 = Equipo.objects.create(nombre='Equipo 2', descripcion='Descripción del Equipo 2')
    equipo3 = Equipo.objects.create(nombre='Equipo 3', descripcion='Descripción del Equipo 3')
    print("parte 2.")
    # Crear proyectos de ejemplo
    proyecto1 = Proyecto.objects.create(name='Proyecto 1', codigo='PROJ1', description='Descripción del Proyecto 1', estado='abierto', tipo='Proyecto Integración', user=Usuario.objects.first(), lider='Líder del Proyecto 1', categoria='Categoría del Proyecto 1', antecedentes='Antecedentes del Proyecto 1', fase='Fase del Proyecto 1', spi=0.5, es=0.3)
    proyecto2 = Proyecto.objects.create(name='Proyecto 2', codigo='PROJ2', description='Descripción del Proyecto 2', estado='suspendido', tipo='Necesidades entrega operación', user=Usuario.objects.first(), lider='Líder del Proyecto 2', categoria='Categoría del Proyecto 2', antecedentes='Antecedentes del Proyecto 2', fase='Fase del Proyecto 2', spi=0.7, es=0.4)
    proyecto3 = Proyecto.objects.create(name='Proyecto 3', codigo='PROJ3', description='Descripción del Proyecto 3', estado='cerrado', tipo='Cerrado', user=Usuario.objects.first(), lider='Líder del Proyecto 3', categoria='Categoría del Proyecto 3', antecedentes='Antecedentes del Proyecto 3', fase='Fase del Proyecto 3', spi=0.8, es=0.6)
    print("parte 3.")
    # Asignar equipos a usuarios
    usuario1.equipos.add(equipo1)
    usuario2.equipos.add(equipo2)
    usuario3.equipos.add(equipo3)
    print("parte 4.")
    # Crear grupos de ejemplo
    grupo1 = Grupo.objects.create(nombre='Grupo 1', asociados='Asociados del Grupo 1', cluster='Cluster del Grupo 1')
    grupo2 = Grupo.objects.create(nombre='Grupo 2', asociados='Asociados del Grupo 2', cluster='Cluster del Grupo 2')
    grupo3 = Grupo.objects.create(nombre='Grupo 3', asociados='Asociados del Grupo 3', cluster='Cluster del Grupo 3')
    print("parte 5.")
    # Asignar grupos a proyectos
    proyecto1.grupo.add(grupo1)
    proyecto2.grupo.add(grupo2)
    proyecto3.grupo.add(grupo3)
    print("parte 5.")
    # Crear programas de ejemplo
    programa1 = Programa.objects.create(nombre='Programa 1')
    programa2 = Programa.objects.create(nombre='Programa 2')
    programa3 = Programa.objects.create(nombre='Programa 3')
    print("parte 6.")
    # Asignar programas a proyectos
    proyecto1.programas.add(programa1)
    proyecto2.programas.add(programa2)
    proyecto3.programas.add(programa3)
    print("parte 7.")
    # Crear hitos de ejemplo
    hito1 = Hito.objects.create(nombre='Hito 1', descripcion='Descripción del Hito 1', proyecto=proyecto1, fecha_inicio='2024-03-01', fecha_fin='2024-03-15', asignado=Usuario.objects.first())
    hito2 = Hito.objects.create(nombre='Hito 2', descripcion='Descripción del Hito 2', proyecto=proyecto2, fecha_inicio='2024-04-01', fecha_fin='2024-04-15', asignado=Usuario.objects.last())
    hito3 = Hito.objects.create(nombre='Hito 3', descripcion='Descripción del Hito 3', proyecto=proyecto3, fecha_inicio='2024-05-01', fecha_fin='2024-05-15', asignado=Usuario.objects.first())
    print("parte 8.")
    # Crear tareas de ejemplo
    tarea1 = Tarea.objects.create(nombre='Tarea 1', descripcion='Descripción de la Tarea 1', hito=hito1, fecha_inicio='2024-03-01', fecha_fin='2024-03-05', asignado=Usuario.objects.first(), estado='En Proceso')
    tarea2 = Tarea.objects.create(nombre='Tarea 2', descripcion='Descripción de la Tarea 2', hito=hito2, fecha_inicio='2024-04-01', fecha_fin='2024-04-05', asignado=Usuario.objects.last(), estado='Finalizada')
    tarea3 = Tarea.objects.create(nombre='Tarea 3', descripcion='Descripción de la Tarea 3', hito=hito3, fecha_inicio='2024-05-01', fecha_fin='2024-05-05', asignado=Usuario.objects.first(), estado='SIN iniciar')
    print("parte 9.")
    # Crear comentarios de tareas de ejemplo
    comentario1 = ComentarioTarea.objects.create(proyecto=proyecto1, identificando_problema='Problema en la Tarea 1', causa='Causa del Problema 1', solucion='Solución al Problema 1', planes_mejora_aplicados='Planes de Mejora Aplicados 1', resultados_planes_mejora='Resultados de los Planes de Mejora 1')
    comentario2 = ComentarioTarea.objects.create(proyecto=proyecto2, identificando_problema='Problema en la Tarea 2', causa='Causa del Problema 2', solucion='Solución al Problema 2', planes_mejora_aplicados='Planes de Mejora Aplicados 2', resultados_planes_mejora='Resultados de los Planes de Mejora 2')
    comentario3 = ComentarioTarea.objects.create(proyecto=proyecto3, identificando_problema='Problema en la Tarea 3', causa='Causa del Problema 3', solucion='Solución al Problema 3', planes_mejora_aplicados='Planes de Mejora Aplicados 3', resultados_planes_mejora='Resultados de los Planes de Mejora 3')
    print("parte 10.")
    # Crear matrices de riesgo de ejemplo
    matriz_riesgo1 = MatrizRiesgo.objects.create(nombre='Matriz de Riesgo 1', descripcion='Descripción de la Matriz de Riesgo 1', Causas='Causas de la Matriz de Riesgo 1', Plan='Plan de Mitigación de la Matriz de Riesgo 1', Descripcion_tiempo='Descripción del Impacto en el Tiempo 1', Descripcion_alcance='Descripción del Impacto en el Alcance 1', Descripcion_costo='Descripción del Impacto en el Costo 1', probavilidad='bajo1', gravedad='medio', riesgo='apreciable', materializo='No se ha materializado el riesgo 1', proyecto=proyecto1, acciones_mitigacion='Acciones de Mitigación de la Matriz de Riesgo 1')
    matriz_riesgo2 = MatrizRiesgo.objects.create(nombre='Matriz de Riesgo 2', descripcion='Descripción de la Matriz de Riesgo 2', Causas='Causas de la Matriz de Riesgo 2', Plan='Plan de Mitigación de la Matriz de Riesgo 2', Descripcion_tiempo='Descripción del Impacto en el Tiempo 2', Descripcion_alcance='Descripción del Impacto en el Alcance 2', Descripcion_costo='Descripción del Impacto en el Costo 2', probavilidad='medio', gravedad='alto1', riesgo='importante', materializo='No se ha materializado el riesgo 2', proyecto=proyecto2, acciones_mitigacion='Acciones de Mitigación de la Matriz de Riesgo 2')
    matriz_riesgo3 = MatrizRiesgo.objects.create(nombre='Matriz de Riesgo 3', descripcion='Descripción de la Matriz de Riesgo 3', Causas='Causas de la Matriz de Riesgo 3', Plan='Plan de Mitigación de la Matriz de Riesgo 3', Descripcion_tiempo='Descripción del Impacto en el Tiempo 3', Descripcion_alcance='Descripción del Impacto en el Alcance 3', Descripcion_costo='Descripción del Impacto en el Costo 3', probavilidad='alto1', gravedad='alto2', riesgo='grave', materializo='No se ha materializado el riesgo 3', proyecto=proyecto3, acciones_mitigacion='Acciones de Mitigación de la Matriz de Riesgo 3')
    print("parte 11.")
    # Crear documentos de ejemplo
    documento1 = Documentos.objects.create(titulo='Documento 1', descriocion='Descripción del Documento 1', link='https://www.example.com/documento1', proyecto=proyecto1)
    documento2 = Documentos.objects.create(titulo='Documento 2', descriocion='Descripción del Documento 2', link='https://www.example.com/documento2', proyecto=proyecto2)
    documento3 = Documentos.objects.create(titulo='Documento 3', descriocion='Descripción del Documento 3', link='https://www.example.com/documento3', proyecto=proyecto3)
    print("parte 12.")
    # Crear costos de ejemplo
    costo1 = Costos.objects.create(contrato='Contrato 1', objeto='Objeto del Contrato 1', tipo='Tipo del Contrato 1', aliado='Aliado del Contrato 1', contrato_aliado='Contrato Aliado 1', backlog='Backlog del Contrato 1', one_time='Costo One-Time del Contrato 1', recurrente='Costo Recurrente del Contrato 1', meses='Meses del Contrato 1', proyecto=proyecto1)
    costo2 = Costos.objects.create(contrato='Contrato 2', objeto='Objeto del Contrato 2', tipo='Tipo del Contrato 2', aliado='Aliado del Contrato 2', contrato_aliado='Contrato Aliado 2', backlog='Backlog del Contrato 2', one_time='Costo One-Time del Contrato 2', recurrente='Costo Recurrente del Contrato 2', meses='Meses del Contrato 2', proyecto=proyecto2)
    costo3 = Costos.objects.create(contrato='Contrato 3', objeto='Objeto del Contrato 3', tipo='Tipo del Contrato 3', aliado='Aliado del Contrato 3', contrato_aliado='Contrato Aliado 3', backlog='Backlog del Contrato 3', one_time='Costo One-Time del Contrato 3', recurrente='Costo Recurrente del Contrato 3', meses='Meses del Contrato 3', proyecto=proyecto3)
    print("parte 13.")
    print("Datos de ejemplo cargados exitosamente.")
