def createMatrix(m,n,v):
    c=[]
    for i in range(m):
        c.append([])
        for j in range(n):
            c[i].append(v)
    
    return c

def getDimensions(a):
    return (len(a), len(a[0]))

def copyMatrix(b):
    m,n = getDimensions(b)
    a = createMatrix(m,n,0)
    for i in range(m):
        for j in range(n):
            a[i][j] = b[i][j]
    return a

def sumaMatrix(a,b):
    am, an = getDimensions(a)
    bm, bn = getDimensions(b)
    if am != bm or bn != bn:
        print("error prro")
        return []
    c = createMatrix(am,an,0)
    for i in range(am):
        for j in range(an):
            c[i][j] = a[i][j] + b[i][j]
    return c

def restaMatrix(a,b):
    am, an = getDimensions(a)
    bm, bn = getDimensions(b)
    if am != bm or bn != bn:
        print("error prro")
        return []
    c = createMatrix(am,an,0)
    for i in range(am):
        for j in range(an):
            c[i][j] = a[i][j] - b[i][j]
    return c

def multMatrix(a,b):
    am, an = getDimensions(a)
    bm, bn = getDimensions(b)
    if an != bm:
        print("error prro")
        return []
    c = createMatrix(am,bn,0)
    for i in range(am):
        for j in range(bn):
            for k in range(an):
                c[i][j] += a[i][k] * b[k][j]
            

    return c

def getAdyacente(a,r,c):
    am,an = getDimensions(a)
    c = createMatrix(am-1,an-1,0)
    
    for i in range(am):
        if i == r:
            continue
        for j in range(an):
            if j == c:
                continue
            ci = 0
            cj = 0
            if i < r:
                ci =i
            else:
                ci = i-1
            if j < r:
                cj = j
            else:
                cj = j-1
            c[i][j] = a[i][j]
    return c

a = createMatrix(3,3,1)
b = copyMatrix(a)
b[0][0] = 40
c = sumaMatrix(a,b)
d = multMatrix(a,a)
e = getAdyacente()
print(a)
print(b)
print(c)
print(d)
