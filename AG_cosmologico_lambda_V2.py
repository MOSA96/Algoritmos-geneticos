import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
        
    return lista2   
  
def _obtener_fitness(z, H_dat, padres, sigma):
    _fitness = chi_square(z, H_dat, padres, sigma)
    Pfitness = list(zip(padres,_fitness))
    Pfitness.sort(key = lambda x: x[1], reverse=False)
    mejor_padre, mejor_fitness = Pfitness[0]
    return round(mejor_padre,6), round(mejor_fitness, 6), Pfitness



def mutacion(z, H_dat, padres, sigma, factor_mutacion):
    
    n = int(len(H_dat))
    padre, fitness, poblacion = _obtener_fitness(z, H_dat, padres, sigma)
    hijos = np.random.normal(padre, factor_mutacion, size=17)
    
    return hijos


def AG_simple(z, H_dat, padres, sigma, max_iter):
    
    Poblacion = {}
    Historial=[]
    f_mutacion = 0.2
    
    mejor_padre, mejor_fitness, poblacion = _obtener_fitness(z, H_dat, padres, sigma)
    padre = mutacion(z, H_dat, padres, sigma, f_mutacion)  
    
    for i in range(1, max_iter):
        
        padre = mutacion(z, H_dat, padre, sigma, f_mutacion)
        padre_actual, fitness_actual, poblacion = _obtener_fitness(z, H_dat, padre, sigma)
        
        Poblacion[i] = poblacion
        
        if fitness_actual < mejor_fitness:
            mejor_padre = padre_actual
            mejor_fitness = fitness_actual    
            
        Historial.append((i, fitness_actual))
        
        f_mutacion = f_mutacion/2 
        
    return mejor_padre, mejor_fitness, Historial, Poblacion
