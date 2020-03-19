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

def resta(c1,c2):
    """Recibo 2 complejos y los resta -> complejo
    """
    a1, b1, a2, b2= c1[0], c1[1], c2[0], c2[1]
    return (a1-a2, b1-b2)

def transpuesta(m1):
    """Recibo una matriz compleja y determino su transpuesta -> matriz compleja
    """
    m2=[[(0,0) for x in m1] for x in m1[0]]
    for j in range(len(m1[0])):
        for k in range(len(m1)):
            m2[j][k]=m1[k][j]
    return m2

def matrizConjugada(m1):
    """Recibo una matriz compleja y determino la matriz conjugada -> matriz compleja
    """
    for j in range(len(m1)):
        for k in range(len(m1[0])):
            m1[j][k]=conjugado(m1[j][k])
    return m1

def matrizAdjunta(m1):
    """Recibo una matriz compleja y determino matriz adjunta -> matriz compleja
    """
    return matrizConjugada(transpuesta(m1))

def matrizHermitian(m1):
    """ Determino si una matriz es hermitian -> boolean
    """
    if (len(m1)!=len(m1[0])):
        return "Imposible"
    else:
        esHermitian = True
        m2 = matrizAdjunta(m1)
        for j in range(len(m1)):
            for k in range(len(m1)):
                if (resta(m1[j][k],m2[j][k])!=(0,0)):
                    esHermitian = False
                    break
        return esHermitian

def matrizIdentidad(n):
    """ Recibo un entero y determino la matriz identidad n*n -> matriz
    """
    ident=[[(0,0) for x in range(n)] for x in range(n)]
    for j in range(n):
        ident[j][j]=(1,0)
    return ident

def multiplicacionEscalarVector(v1,c):
    """Recibo 1 vector complejo y un escalar y hago la multiplicacion escalar de vector -> vector complejo
    """
    for j in range(len(v1)):
        v1[j]=multiplicacion(v1[j],c)
    return v1

def multiplicacionEscalarMatriz(m1,c):
    """Recibo una matriz compleja y un escalar y hago la multiplicacion escalar de matriz -> matriz compleja
    """
    for j in range(len(m1)):
        m1[j]=multiplicacionEscalarVector(m1[j],c)
    return m1
