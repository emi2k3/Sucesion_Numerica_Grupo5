import numpy as np
import matplotlib.pyplot as plt

from graficos_utils import guardar_figura


def ejecutar_actividad_5():
    print('\n--- EJECUTANDO ACTIVIDAD 5 ---')

    V0 = 1000
    n_pasos = 15
    n_eje = np.arange(0, n_pasos + 1)
    hk_casos = [0.3, 0.7, 1.0, 1.4, 2.05]

    fig, ax = plt.subplots(figsize=(8, 5))

    for hk in hk_casos:
        V_seq = V0 * ((1 - hk) ** n_eje)
        ax.plot(n_eje, V_seq, 'o--', label=f'$hk = {hk}$')

    ax.axhline(0, color='black', linewidth=0.8, linestyle=':')
    ax.set_title('Modelo Discreto $V_{n+1} = (1 - hk)V_n$ para distintos valores de $hk$')
    ax.set_xlabel('Paso $n$')
    ax.set_ylabel('Equipos vulnerables $V_n$')
    ax.grid(True, ls='--', alpha=0.6)
    ax.legend()

    guardar_figura(fig, 'act5_modelo_discreto.png')
    print("Gráficas de Actividad 5 exportadas en 'figuras/act5_modelo_discreto.png'.")


if __name__ == '__main__':
    ejecutar_actividad_5()
