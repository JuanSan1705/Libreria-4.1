def suma(a, b):
    return (a[0]+b[0], a[1]+b[1])

def multiplicacion(c1,c2):
    """Recibo 2 complejos y los multiplica -> complejo
    """
    a1,b1,a2,b2=c1[0],c1[1],c2[0],c2[1]
    return (a1*a2-b1*b2,a1*b2+a2*b1)

def multiplicacionMatrizVector(m1,m2):
    """Recibo 2 matrices complejas y hallo la multiplicacion de matrices -> matriz compleja
       se debe cumplr a:m*n, b:n*p
    """
    if (len(m1[0])!=len(m2)):
        return "Imposible"
    else:
        m3 = [[0] for x in m2]
        for j in range(len(m1)):
            for k in range(len(m2[0])):
                #print(len(m2[0]))
                resultado=(0,0)
                for h in range(len(m2)):
                    resultado=suma(multiplicacion(m1[j][h],m2[h][k]),resultado)
                m3[j][k]=resultado
        return m3

def multiplicacionMatrizMatriz(m1,m2):
    """Recibo 2 matrices complejas y hallo la multiplicacion de matrices -> matriz compleja
       se debe cumplr a:m*n, b:n*p
    """
    if (len(m1[0])!=len(m2)):
        return "Imposible"
    else:
        m3=[[(0,0) for x in m2[0]] for x in m1]
        for j in range(len(m1)):
            for k in range(len(m2[0])):
                resultado=(0,0)
                for h in range(len(m2)):
                    resultado=suma(multiplicacion(m1[j][h],m2[h][k]),resultado)
                m3[j][k]=resultado
        return m3

def Tuplex(c1):
    Ma = []
    for i in range (len(c1)):
        Ma.append(c1[i][0])
    h = []
    for j in range (len(Ma)):
        A = modulo(Ma[j])
        h.append(A)
    return h

def modulo(c1):
    return c1[0]**2 + c1[1]**2

def conjugado(c1):
    return (c1[0], -c1[1])

def Division(C1, R):
    return (C1[0]/R, C1[1]/R)
