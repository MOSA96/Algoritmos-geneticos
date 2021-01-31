#Definimos funciones a optimizar

def _fitness(x):
    if x > -20 and x < 20:
        y = (x**2+x)*np.cos(2*x) + x**2
        return round(y, 6)
    else:
        return 0
    
def _polynomial(x):
    y =  - x**6/60 - x**5/50 + x**4/2 + 2*x**3/3 - 3.2*x**2 - 6.4*x
    
    return y


def _trigonometric(x):
    y =  np.sin(3*x + 45)**2 + 0.9*np.sin(9*x)**3 - np.sin(15*x + 50)*np.cos(2*x - 30)
    return y
