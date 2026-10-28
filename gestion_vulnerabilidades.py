import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from euler import euler
from graficos_utils import guardar_figura



def solucion_exacta(t, V0, k):
    """Solución exacta para V'(t) = -k V(t), con V(0) = V0."""
    return V0 * np.exp(-k * t)


def graficar_organizacion(org, k, V0=1000, t0=0, tf=20,
                        h_valores=(1.0, 0.5, 0.1), tiempos_eval=(5, 10, 15)):
    fig, ax = plt.subplots(figsize=(8, 5))

    t_teorico = np.linspace(t0, tf, 500)
    V_teorico = solucion_exacta(t_teorico, V0, k)
    ax.plot(t_teorico, V_teorico, 'k--', label=f'Teórica ($1000 e^{{-{k}t}}$)', linewidth=2)

    f = lambda t, V: -k * V
    resultados = []

    for h in h_valores:
        n_pasos, V_num, t_num = euler(f, V0, t0, tf, h)
        ax.plot(t_num, V_num, label=f'Euler ($h={h}$)', alpha=0.8)

        for t_target in tiempos_eval:
            idx = int(round(t_target / h))
            v_aprox = V_num[idx]
            v_real = solucion_exacta(t_target, V0, k)
            err_abs = abs(v_real - v_aprox)

            resultados.append({
                'Org': org,
                'k': k,
                'h': h,
                't': t_target,
                'V_aprox': v_aprox,
                'V_exacta': v_real,
                'Error_Abs': err_abs
            })

    ax.set_title(f'Gestión de Vulnerabilidades - Organización {org} ($k={k}$, $V_0=1000$)')
    ax.set_xlabel('Tiempo $t$ (días)')
    ax.set_ylabel('Equipos vulnerables $V(t)$')
    ax.grid(True, ls='--', alpha=0.6)
    ax.legend()

    guardar_figura(fig, f'act4_org_{org}.png')
    return resultados


def ejecutar_actividad_4():
    print('--- EJECUTANDO ACTIVIDAD 4 ---')

    organizacion_params = {'A': 0.1, 'B': 0.3, 'C': 0.7}
    resultados = []

    for org, k in organizacion_params.items():
        resultados.extend(graficar_organizacion(org, k))

    df_res = pd.DataFrame(resultados)
    print(df_res.to_string(index=False))
    return df_res


if __name__ == '__main__':
    ejecutar_actividad_4()
