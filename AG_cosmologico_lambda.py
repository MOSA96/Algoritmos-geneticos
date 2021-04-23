import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Definimos ecuaciones 

#Calculamos valores de H para cada valor z para cada parámetros
def h_square(z,list_cdm):
    h_dict = {}
    
    for i in list_cdm:
        h_dict[i] = list(np.sqrt((H0**2)*(i*(1+z)**3+ (1-i) )))
        
    return h_dict

#Calculamos 

def chi_square(z, H_dat, cdm, sigma):
    #Calculamos H para cada Omega
    H_th  = h_square(z,cdm)
    lista2 = []
    
    for i in H_th:
        resultado = 0
        lista = H_th[i]
        for j in range(len(lista)):
            resultado += (lista[j]-H_dat[j])**2 / sigma[j]
            
        lista2.append(resultado)
    
def _obtener_fitness(z, H_dat, padres, sigma):
    _fitness = chi_square(z, H_dat, padres, sigma)
    Pfitness = list(zip(padres,_fitness))
    Pfitness.sort(key = lambda x: x[1], reverse=False)
    mejor_padre, mejor_fitness = Pfitness[0]
    return round(mejor_padre,6), round(mejor_fitness, 6)


def mutacion(z, H_dat, padres, sigma):
    
    n = int(len(H_dat))
    puntajes = chi_square(z, H_dat, padres, sigma)
    padres = np.array(padres)
    hijos = np.random.choice(padres, size=n, p = puntajes / sum(puntajes))
    hijos = hijos.tolist()
    inferior = min(hijos)
    superior = max(hijos)
    hijos = hijos + np.random.uniform(0, 1-superior, size = n)
    
    return hijos.tolist()


def AG_simple(z, H_dat, padres, sigma, max_iter):
    Historial=[]
    Mejores_padres = []
    
    mejor_padre, mejor_fitness = _obtener_fitness(z, H_dat, padres, sigma)
    
    for i in range(1, max_iter):
        padre = mutacion(z, H_dat, padres, sigma)
        padre_actual, fitness_actual = _obtener_fitness(z, H_dat, padre, sigma)
        
        if fitness_actual < mejor_fitness:
            mejor_padre = padre_actual
            mejor_fitness = fitness_actual    
            
        Historial.append((i, np.min(chi_square(z, H_dat, padre, sigma))))
               
    return mejor_padre, mejor_fitness,Historial



