import os
import django

# Configura el entorno Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'arriendo_inmuebles.settings')
django.setup()

from web.models import Inmueble, Comuna

# Abrir un archivo para guardar los resultados
with open('inmuebles_por_comuna.txt', 'w') as file:
    # Obtener todas las comunas
    comunas = Comuna.objects.all()
    
    for comuna in comunas:
        # Obtener inmuebles por comuna
        inmuebles = Inmueble.objects.filter(fk_com=comuna)
        
        if inmuebles.exists():
            file.write(f"\n--- {comuna.com_comuna} ---\n")
            
            for inmueble in inmuebles:
                file.write(f"Nombre: {inmueble.inm_nombre}\n")
                file.write(f"Descripción: {inmueble.inm_descripcion}\n\n")

print("Archivo 'inmuebles_por_comuna.txt' generado con éxito.")