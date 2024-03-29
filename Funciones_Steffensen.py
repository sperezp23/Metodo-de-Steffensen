# Funciones Steffensen 

# %% Librerías
import math

# %% Funciones a evaluar
def f(p):
    f = p + math.cos(p)
    return f

def g(p):
    g = -math.cos(p)
    return g

# %% Errores
def Errores(tipErr,p,z):
    if tipErr == 1:
        E = abs(p-z)
    elif tipErr == 2:
        E = abs((p-z)/(p))
    elif tipErr == 3:
        E = abs((p-z)/(p))*100.0
    return E