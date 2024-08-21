import os
import django

# Configura el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tu_proyecto.settings')
django.setup()

from web.models import Inmueble, Region

# Abrir un archivo para guardar los resultados
with open('inmuebles_por_region.txt', 'w') as file:
    # Obtener todas las regiones
    regiones = Region.objects.all()
    
    for region in regiones:
        # Obtener inmuebles por region
        inmuebles = Inmueble.objects.filter(fk_reg=region)
        
        if inmuebles.exists():
            file.write(f"\n--- {region.reg_region} ---\n")
            
            for inmueble in inmuebles:
                file.write(f"Nombre: {inmueble.inm_nombre}\n")
                file.write(f"Descripción: {inmueble.inm_descripcion}\n\n")

print("Archivo 'inmuebles_por_region.txt' generado con éxito.")
