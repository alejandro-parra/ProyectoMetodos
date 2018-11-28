# Punto Fijo

2x^2 -5x +3

despejar x

x1= (2x0^2 +3)/5

x1 - x0 = 0

El valor fijo es x0 que con suerte estará en el rango y se acerca a 0.

def xnew(xprev):
    return (2*xprev**2+3)/5

x0=0
iteraciones=1

for i in range(100):
    x1= xnew(x0)
    if abs(x1-x0) < 0.0000001:
        break
        
    x0=x1
    iteraciones+=1
    
    
print("La raiz es %.5f"%x1)
print("Con %d iteraciones"%iteraciones)




