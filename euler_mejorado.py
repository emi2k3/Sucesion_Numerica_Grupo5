import os
import matplotlib.pyplot as plt
from euler import euler, f_decreciente, solucion_referencia
from error_euler import errores

os.makedirs("figuras", exist_ok=True)


def euler_mejorado(f, x0, t0, tf, h):
    if h <= 0:
        raise ValueError("h debe ser mayor a 0")
    if tf < t0:
        raise ValueError("tf debe ser mayor o igual a t0")

    t = t0
    x = x0
    n = 0
    valoresx = [x]
    tiempos = [t]
    while t < tf - 1e-12:
        h_actual = min(h, tf - t)
        k1 = f(t, x)
        x_pred = x + h_actual * k1          # prediccion
        k2 = f(t + h_actual, x_pred)        # pendiente predicha
        x = x + h_actual / 2 * (k1 + k2)    # promedio de pendientes
        t = t + h_actual
        if abs(t - tf) < 1e-12:
            t = tf
        n += 1
        tiempos.append(t)
        valoresx.append(x)
    return n, valoresx, tiempos


def actividad3():
    print(f"{'Método':<16} {'h':>5} {'Valor final':>14} "
          f"{'Error final':>14} {'Error máx':>12} {'Pasos':>6}")
    for nombre, metodo in [("Euler", euler), ("Euler mejorado", euler_mejorado)]:
        for h in [1, 0.5, 0.1]:
            n, x, t = metodo(f_decreciente, 1, 0, 10, h)
            E = errores(t, x)
            print(f"{nombre:<16} {h:>5} {x[-1]:>14.6e} "
                  f"{E[-1]:>14.4e} {max(E):>12.4e} {n:>6}")

    # Gráfica comparativa del error con h = 0.1
    fig, ax = plt.subplots(figsize=(8, 5))
    for nombre, metodo in [("Euler", euler), ("Euler mejorado", euler_mejorado)]:
        n, x, t = metodo(f_decreciente, 1, 0, 10, 0.1)
        ax.plot(t, errores(t, x), label=nombre)
    ax.set_xlabel("Tiempo t")
    ax.set_ylabel("Error absoluto")
    ax.set_title("Euler vs Euler mejorado (h = 0.1)")
    ax.legend()
    ax.grid(True)
    plt.tight_layout()
    fig.savefig("figuras/actividad3_comparacion.png")
    plt.close(fig)


if __name__ == "__main__":
    actividad3()