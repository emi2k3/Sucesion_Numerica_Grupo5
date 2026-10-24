import matplotlib.pyplot as plt
import math

def graficar_resultados(resultado, nombre_archivo: str,crecimiento):
    figura, ejes = plt.subplots(figsize=(8, 5))
    
    for h,pasos,valoresx,tiempos in resultado:
        ejes.plot(
            tiempos,
            valoresx,
            marker="o",
            label=f"h={h} ({pasos} pasos)"
        )
    plt.tight_layout()
    if (crecimiento):
        ejes.plot(
        [0, 10],
        [0, 10],
        linestyle="--",
        label="Solución exacta: x(t) = t"
        )
    else:
        tiempos_referencia = [i / 10 for i in range(101)]
        valores_referencia = [
        solucion_referencia(t) for t in tiempos_referencia
        ]
        plt.plot(
        tiempos_referencia,
        valores_referencia,
        linestyle="--",
        label="Solución exacta"
        )

    ejes.set_xlabel("Tiempo t")
    ejes.set_ylabel("Valor de x(t)")
    ejes.set_title("Método de Euler")
    ejes.legend()
    ejes.grid(True)
    plt.tight_layout()
    figura.savefig(f'figuras/{nombre_archivo}.png')
    plt.close(figura)


def euler(f,x0,t0,tf,h):
    """
        Recibe: funcion f(t,x)
        \nx0:Condicion inicial
        \nt0:Tiempo inicial
        \ntf:Tiempo final
        \ntamaño del paso h
        \nRetorna: 
        \nValores del tiempo
        \nValores aproximados de x 
        \nCantidad de pasos realizados
    """
    t=t0
    x=x0
    n=0
    valoresx=[x]
    tiempos=[t]  
 
    if(h<=0):
        raise ValueError("h debe ser mayor a 0")
    if(tf<t):
        raise ValueError("tf debe ser mayor o igual t")
    while t < tf - 1e-12:
        h_actual = min(h, tf - t)
        x = x + h_actual * f(t, x)
        t = t + h_actual

        if abs(t - tf) < 1e-12:
            t = tf
        n += 1
        tiempos.append(t)
        valoresx.append(x)
    return n, valoresx, tiempos
    

def f_creciente(t,x):
    return 1

def f_decreciente(t,x):
    return -x

def solucion_referencia(t):
    return math.e**(-t)


def Crece():
    test=[1,0.5,0.1]
    resultado=[]
    for h in test:
        pasos,valoresx,tiempos=euler(f_creciente,0,0,10,h)
        resultado.append((h,pasos,valoresx,tiempos))
    graficar_resultados(resultado,"crecimiento_lineal",True)

def Decrece():
    test=[1,0.5,0.1,0.01]
    resultado=[]
    for h in test:
        pasos,valoresx,tiempos=euler(f_decreciente,1,0,10,h)
        resultado.append((h,pasos,valoresx,tiempos))
    graficar_resultados(resultado,"decrecimiento_exponencial",False)

if __name__ == "__main__":
    Crece()
    Decrece()