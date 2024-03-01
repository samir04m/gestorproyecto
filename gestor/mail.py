from django.core.mail import send_mail
from django.template.loader import render_to_string

def enviar_correo_post(correo_destino, contexto, tipo_correo):
    
    
    plantillas = {
        'tipo1': 'correos/asignacion_proyect.html',
        'tipo2': 'correos/asignacion_proyect.html',
        
    }
    
    
    if tipo_correo in plantillas:
        plantilla_seleccionada = plantillas[tipo_correo]
    else:
        raise ValueError("El tipo de correo especificado no existe")
    
    
    contenido_correo = render_to_string(plantilla_seleccionada, {'contexto': contexto})
    
    
    send_mail(
        'Asunto del Correo',
        contenido_correo,
        'notificaciones_colvacor@colvatel.com.co',  
        [correo_destino], 
        html_message=contenido_correo,
        fail_silently=False,  
    )





# def enviar_correo_post( correo_destino, contexto ) :
#     # Genera el contenido del correo electrónico desde una plantilla
#     contenido_correo = render_to_string('correos/prueba.html', {'contexto': contexto})
    
#     send_mail(
#         'Asunto del Correo',
#         'contenido_correo',
#         'notificaciones_colvacor@colvatel.com.co',  # Dirección de correo electrónico del remitente
#         [correo_destino],  # Lista de direcciones de correo electrónico de los destinatarios
#         html_message=contenido_correo,
#         fail_silently=False,  # Cambiar a True si quieres manejar errores de forma silenciosa
#     )