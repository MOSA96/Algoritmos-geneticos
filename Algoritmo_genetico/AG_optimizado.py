def AG_simple(padres, funcion_fitness, inicio, fin, max_iter=100):
    mejor_padre, mejor_fitness = _obtener_fitness(padres, funcion_fitness)
       
    for i in range (1, max_iter):
        #Seleccionamos a los mejores padres, mutamos y creamos generacion hija
        padres = mutacion(padres, funcion_fitness= funcion_fitness)
        padre_actual, fitness_actual = _obtener_fitness(padres, funcion_fitness=funcion_fitness)
        
        #Actualizamos valores de mejor padre y fitness
        
        if fitness_actual > mejor_padre:
            mejor_padre = padre_actual
            mejor_fitness = fitness_actual
            
        padre_actual, fitness_actual = _obtener_fitness(padres, funcion_fitness)

               
    return mejor_padre, mejor_fitness

