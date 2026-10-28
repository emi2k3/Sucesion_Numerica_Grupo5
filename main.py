"""
Punto de entrada del programa, ejecuta todos los experimentos del trabajo en orden y deja los 
gráficos en la carpeta "figuras/".
Uso: python main.py
"""
import runpy

from graficos_utils import crear_carpeta_figuras

SECCIONES = [
    ('Sección 1: Metodo Euler', 'euler.py'),
    ('Sección 4: Gestión de vulnerabilidades', 'gestion_vulnerabilidades.py'),
    ('Sección 5: Modelo discreto', 'modelo_discreto.py'),
]

def ejecutar_todo():
    # Corre cada sección como si se hubiera ejecutado por separado.
    crear_carpeta_figuras()
    for titulo, archivo in SECCIONES:
        print(f"\n{'=' * 60}\n{titulo}\n{'=' * 60}")
        runpy.run_path(archivo, run_name='__main__')
    print("\nPronto! Los gráficos están en la carpeta 'figuras/'.")

if __name__ == "__main__":
    ejecutar_todo()