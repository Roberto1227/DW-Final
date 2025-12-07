"""
Archivo WSGI de ejemplo para PythonAnywhere

INSTRUCCIONES:
1. Copia este archivo y su contenido
2. En PythonAnywhere, ve a tu web app
3. Haz clic en "WSGI configuration file"
4. Reemplaza TODO el contenido con el código de abajo
5. Guarda el archivo

NOTA: Este archivo ya está configurado con tu usuario: SrRoberto
"""

import os
import sys

# Ruta del proyecto (ya configurada con tu usuario: SrRoberto)
path = '/home/SrRoberto/EduRetoSV'
if path not in sys.path:
    sys.path.insert(0, path)

# Configurar Django
os.environ['DJANGO_SETTINGS_MODULE'] = 'eduretosv.settings'
os.environ['ON_PYTHONANYWHERE'] = 'True'  # Activa modo producción

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

