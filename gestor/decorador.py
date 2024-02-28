from functools import wraps
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect

def tipo_usuario_requerido(tipo_usuario):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if request.user.tipo == tipo_usuario:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('nombre_de_tu_url_de_login')  # Redirige al inicio de sesión
        return wrapper
    return decorator

