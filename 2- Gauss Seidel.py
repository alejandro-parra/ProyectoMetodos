def getx1(x2,x3):
    return (210 - 20*x2 - 5*x3)/15

def getx2(x1,x3):
    return 2*x3

def getx3(x1,x2):
    return 2*x1


#Valores iniciales
x1 = 1
x2 = 1
x3 = 1
error = 0.01
x1a = 0.00001
x2a = 0.00001
x3a = 0.00001

for i in range(100):
    x1 = getx1(x2,x3)
    x2 = getx2(x1,x3)
    x3 = getx3(x1,x2)
    print("itera %d"%i,x1,x2,x3)
    #Calculo de errores
    ex1 = abs((x1a - x1)/x1a)
    ex2 = abs((x2a - x2)/x2a)
    ex3 = abs((x3a - x3)/x3a)
    
    if ex1 < error and ex2 < error and ex3 < error:
        break
    
    x1a = x1
    x2a = x2
    x3a = x3
    
print("Los valores son",x1,x2,x3)
        
