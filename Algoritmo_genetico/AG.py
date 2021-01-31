import numpy as np #Herramiento de computo científico
import matplotlib.pyplot as plt #Herramientas para gráficar 
from scipy.optimize import minimize #Encontrar máximos y mínimos
import time #Tiempos de ejecución


#Definimos la función mutación

def mutacion(padres, funcion_fitness):
    n = int(len(padres))
    puntajes = funcion_fitness(padres)
    #Tomamos valores mayores que cero
    idx = puntajes > 0
    puntajes = puntajes[idx]
    padres = np.array(padres)[idx]
    #Creamos generacion hija
    hijos = np.random.choice(padres, size=n, p = puntajes / puntajes.sum())
    hijos = hijos + np.random.uniform(-0.51, 0.51, size = n)

    return hijos.tolist()

#Creamos listas vacías para guardar tiempo de ejecución
def _obtener_fitness(padres, funcion_fitness):
        _fitness = fitness(padres)
        PFitness = list(zip(padres, _fitness))
        PFitness.sort(key = lambda x: x[1], reverse=True)
        mejor_padre, mejor_fitness = PFitness[0]
        return round(mejor_padre,4), round(mejor_fitness, 4)
    
    
    def AG(padres, funcion_fitness, inicio, fin, max_iter=100):
    #Lista para guardar datos
    Historial=[]
    Mejores_padres = []
    #Datos generación cero
    mejor_padre, mejor_fitness = _obtener_fitness(padres, funcion_fitness)
    
    print('generacion {}| mejor fitness{}| fitness actual {} | padre_actual {}'.format(0, mejor_fitness, mejor_fitness, mejor_padre))
    
    #Graficamos
    x = np.linspace(start=inicio, stop=fin, num=1000)
    plt.plot(x, funcion_fitness(x))
    plt.scatter(padres, funcion_fitness(padres), marker='o')
    
    for i in range (1, max_iter):
        #Seleccionamos a los mejores padres, mutamos y creamos generacion hija
        padres = mutacion(padres, funcion_fitness= funcion_fitness)
        padre_actual, fitness_actual = _obtener_fitness(padres, funcion_fitness=funcion_fitness)
        
        #Actualizamos valores de mejor padre y fitness
        
        if fitness_actual > mejor_padre:
            mejor_padre = padre_actual
            mejor_fitness = fitness_actual
            
        padre_actual, fitness_actual = _obtener_fitness(padres, funcion_fitness)
        
        if i % 10 == 0:
            print('generacion {}| mejor fitness {}| fitness actual {} | padre actual {}'.format(i, mejor_fitness, fitness_actual, padre_actual))
            
        Historial.append((i, np.max(funcion_fitness(padres)))) 
        Mejores_padres.append(mejor_padre)
        
    plt.scatter(padres, funcion_fitness(padres))
    plt.scatter(mejor_padre, funcion_fitness(mejor_padre), marker = '.', c = 'b', s = 100)
    plt.ioff()    
        
    print('generacion {}| mejor_padre {}| mejor_fitness {}'.format(i,  mejor_padre, mejor_fitness))
               
    return mejor_padre, mejor_fitness, Historial, Mejores_padres

