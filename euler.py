import matplotlib.pyplot as plt

def graficar_resultados(resultado, nombre_archivo: str):
    figura, ejes = plt.subplots(figsize=(8, 5))
    
    for h,pasos,valoresx,tiempos in resultado:
        ejes.plot(
            tiempos,
            valoresx,
            marker="o",
            label=f"h={h} ({pasos} pasos)"
        )
    plt.tight_layout()
    ejes.plot(
    [0, 10],
    [0, 10],
    linestyle="--",
    label="Solución exacta: x(t) = t"
    )
    ejes.set_xlabel("Tiempo t")
    ejes.set_ylabel("Valor de x(t)")
    ejes.set_title("Método de Euler")
    ejes.legend()
    ejes.grid(True)
    plt.tight_layout()
    plt.show()
    plt.close(figura)
    figura.savefig(f'figuras/{nombre_archivo}')


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
 
    try:
        if(h<=0):
            raise ValueError("h debe ser mayor a 0")
        if(tf<t):
            raise ValueError("tf debe ser mayor a t")
        while t<tf:
            x=x+h*f(t,x)
            t+=h
            n+=1
            tiempos.append(t)
            valoresx.append(x)
        return n,valoresx,tiempos
    except:
        print(ValueError)
    

def f(t,x):
    return 1
euler(f,0,0,10,1)

test=[1,0.5,0.1]
resultado=[]
for h in test:
    pasos,valoresx,tiempos=euler(f,0,0,10,h)
    print(valoresx)
    print(tiempos)
    resultado.append((h,pasos,valoresx,tiempos))
graficar_resultados(resultado,"crecimiento_lineal")
