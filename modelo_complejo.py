import os
import matplotlib.pyplot as plt
from euler import euler

os.makedirs("figuras", exist_ok=True)

# Parámetros de la Actividad 6
V0 = 1000
K = 0.3
LAMBDAS = [0, 50, 100, 200]
T0, TF = 0, 20
H = 0.1
TIEMPOS_CONTROL = [5, 10, 15, 20]


def f_aparicion(lam, k):
    """Devuelve f(t, V) = lambda - k*V para el modelo con aparición de vulnerabilidades."""
    def f(t, V):
        return lam - k * V
    return f


def valor_en(tiempos, valores, t_buscado):
    """Valor aproximado en el instante de la malla más cercano a t_buscado."""
    i = min(range(len(tiempos)), key=lambda j: abs(tiempos[j] - t_buscado))
    return valores[i]


def tendencia(V0, V_eq):
    if abs(V0 - V_eq) < 1e-9:
        return "se mantiene estable"
    return "disminuye y se estabiliza" if V0 > V_eq else "crece y se estabiliza"


def actividad6():
    encabezado = f"{'lambda':>7} {'V* = lambda/k':>14}"
    for tc in TIEMPOS_CONTROL:
        encabezado += f" {'V(' + str(tc) + ')':>10}"
    encabezado += f"  {'Tendencia'}"
    print(encabezado)

    fig, ax = plt.subplots(figsize=(8, 5))
    for lam in LAMBDAS:
        n, V, t = euler(f_aparicion(lam, K), V0, T0, TF, H)
        V_eq = lam / K      # equilibrio: V'(t) = 0  =>  V = lambda / k

        fila = f"{lam:>7} {V_eq:>14.2f}"
        for tc in TIEMPOS_CONTROL:
            fila += f" {valor_en(t, V, tc):>10.2f}"
        fila += f"  {tendencia(V0, V_eq)}"
        print(fila)

        linea, = ax.plot(t, V, label=f"λ = {lam}")
        ax.axhline(V_eq, linestyle="--", linewidth=0.8, color=linea.get_color())

    ax.set_xlabel("Tiempo t")
    ax.set_ylabel("Equipos vulnerables V(t)")
    ax.set_title(f"V' = λ − kV  (V0 = {V0}, k = {K}, Euler h = {H})")
    ax.legend()
    ax.grid(True)
    plt.tight_layout()
    fig.savefig("figuras/actividad6_modelo_complejo.png")
    plt.close(fig)


if __name__ == "__main__":
    actividad6()
