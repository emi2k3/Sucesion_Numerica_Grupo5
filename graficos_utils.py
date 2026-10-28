import os
import matplotlib.pyplot as plt


def crear_carpeta_figuras(carpeta='figuras'):
    os.makedirs(carpeta, exist_ok=True)


def guardar_figura(fig, nombre, carpeta='figuras', dpi=300):
    crear_carpeta_figuras(carpeta)
    fig.tight_layout()
    fig.savefig(f'{carpeta}/{nombre}', dpi=dpi, bbox_inches='tight')
    plt.close(fig)
