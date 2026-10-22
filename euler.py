def euler(f,x0,t0,tf,h):
    t=t0
    x=x0
    n=0
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
    try:
        if(h<=0):
                err=ValueError("h debe ser mayor a 0")
        for i in range(tf):
            t+=h
            n+=1
            x=x+h*f(t,x)
        print(f"""Valores de tiempo: 
        \nTiempo inicial:{x}
        \nPasos realizados:{n}      
""")
    except(err):
        print(err)
    

def f(t,x):
    return t +x
euler(f,0,0,3,1)