import Operaciones as Op


def SumModulos(VectorKet, Posicion):
    if Posicion >= len(VectorKet):
        return 'No es posible calcular'
    else:
        suma = []
        for i in range(len(VectorKet)):
            A = Op.modulo(VectorKet[i])
            suma.append(A)
        Sum1 = 0
        for j in range(len(suma)):
            Sum1 += suma[j]
        Mod = Op.modulo(VectorKet[Posicion])
        Result = Mod / Sum1
        return Result

def NormalizarVector(VectorKet):
    b = []
    for i in range(len(VectorKet)):
        a = Op.modulo(VectorKet[i])
        b.append(a)
    sum = 0
    for j in range(len(b)):
        sum += b[j]
    Vec = []
    for x in range(len(VectorKet)):
        S = Op.Division(VectorKet[x], sum)
        Vec.append(S)
    return Vec

def AmplitudTrans(VectorKet, VectorKet2):
    A = NormalizarVector(VectorKet)
    B = NormalizarVector(VectorKet2)
    if len(A) != len(B):
        return 'No se puede hacer la operacion'
    else:
        Mat = []
        for i in range (len(B)):
            X = Op.conjugado(B[i])
            Mat.append(X)

        Result = []
        for j in range(len(B)):
            w = Op.multiplicacion(Mat[j], A[j])
            Result.append((w))
        sum = (0, 0)
        for x in range (len(Result)):
            sum = Op.suma(sum, Result[x])
        return  sum

