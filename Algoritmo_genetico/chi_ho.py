#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np


# In[4]:


#Definimos ecuaciones 


#Calculamos los parámetros
def omega(cdm):
    return 1-cdm


# In[5]:


#Calculamos valores de H para cada valor z para cada parámetros Omega
def h_square(z,list_cdm, list_h):
    h_dict = {}
    
    
    for i in list_h:
        cdm_dict = {}
        for j in list_cdm:
            cdm_dict[j] = list(np.sqrt((i**2)*(j*(1+z)**3+ (1-j) )))
            h_dict[i] = cdm_dict

    return h_dict


# In[6]:


def chi_square(z, H_dat, cdm, sigma,h):
    #Calculamos H para cada Omega
    H_th  = h_square(z,cdm,h)
    lista2 = []
    
    for i in H_th:
        diccionario = H_th[i]
        for j in diccionario:
            resultado = 0
            lista = diccionario[j]
            for w in range(len(lista)):
                resultado += (lista[w]-H_dat[w])**2 / sigma[w]
                
            lista2.append(resultado)
    
    return lista2


# In[7]:


#Datos
datos = pd.read_csv('Hz_all.dat', delim_whitespace=True)


H_dat = datos["Hz"]
z = datos["z"]
error = datos["errHz"]

cdm = np.random.uniform(low=0,high=1,size=26)
h = np.random.randint(low=0,high=100,size=26)


# In[8]:


def _obtener_fitness(z, H_dat, padres, sigma, h):
    _fitness = chi_square(z, H_dat, padres, sigma, h)
    Pfitness = list(zip(padres,h,_fitness))
    Pfitness.sort(key = lambda x: x[2], reverse=False)
    mejor_padre, mejor_h, mejor_fitness = Pfitness[0]
    return round(mejor_padre,6), round(mejor_h,6) ,round(mejor_fitness, 6)


# In[11]:


def mutacion(z, H_dat, padres, sigma, h):
    
    n = int(len(H_dat))
    puntajes = chi_square(z, H_dat, padres, sigma, h)
    padres_cdm = np.array(padres)
    padres_h = np.array(h)
    hijos_cdm = np.random.choice(padres_cdm, size=n, p = puntajes/sum(puntajes))
    #hijos = hijos.tolist()
    #inferior = min(hijos)
    #superior = max(hijos)
    #hijos = hijos + np.random.uniform(0, 1-superior, size = n)
    
    #return hijos.tolist()
    return hijos_cdm


# In[17]:


def combinaciones(x,y):
    x = np.asarray(x)
    y = np.asarray(y)
    combinaciones = []
    for i in x:
        elemento = zip(i,y)
        combinaciones.append(elemento)
        
    return elemento
        
        


# In[18]:


combinaciones(cdm,h)


# In[13]:


_obtener_fitness(z, H_dat, cdm, error, h)


# In[100]:


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


# In[ ]:




