import os
import matplotlib.pyplot as plt
from euler import euler, f_decreciente, solucion_referencia

os.makedirs("figuras", exist_ok=True)


def errores(tiempos, valoresx):
    return [abs(solucion_referencia(t) - x) for t, x in zip(tiempos, valoresx)]


def actividad2():
    hs = [1, 0.5, 0.1, 0.05, 0.01]
    print(f"{'h':>6} {'Pasos':>6} {'Error final':>14} {'Error máximo':>14}")

    fig, ax = plt.subplots(figsize=(8, 5))
    for h in hs:
        n, x, t = euler(f_decreciente, 1, 0, 10, h)
        E = errores(t, x)
        print(f"{h:>6} {n:>6} {E[-1]:>14.4e} {max(E):>14.4e}")
        ax.plot(t, E, label=f"h={h}")

    ax.set_xlabel("Tiempo t")
    ax.set_ylabel("Error absoluto $E_n$")
    ax.set_title("Error de Euler para x' = -x")
    ax.legend()
    ax.grid(True)
    plt.tight_layout()
    fig.savefig("figuras/actividad2_error.png")
    plt.close(fig)


if __name__ == "__main__":
    actividad2()