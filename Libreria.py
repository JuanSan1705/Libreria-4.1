import Operaciones as Op
import math


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
    
def CalculoMedia(Matriz, Ket):
    if Op.matrizHermitian(Matriz) == True:
        M = Op.multiplicacionMatrizVector(Matriz, Ket)
        M1 = []
        for h in range (len(M)):
            M1.append(M[h][0])
        kResult = []
        for Cam in range(len(M1)):
            kResult.append(Op.conjugado(M1[Cam]))
        ket1 = []
        for x in range(len(Ket)):
            ket1.append(Ket[x][0])
        Sum = (0, 0)
        k = []
        for i in range (len(Ket)):
            Mult = Op.multiplicacion(kResult[i], ket1[i])
            k.append(Mult)
        for j in range(len(k)):
            Sum = Op.suma(Sum, k[j])


        Delta = Op.multiplicacionEscalarMatriz(Op.matrizIdentidad(len(Matriz)), Sum)
        n = Matriz
        for p in range(len(Matriz)):
            for r in range(len(Matriz)):
                n[p][r] = Op.resta(Matriz[p][r], Delta[p][r])
        return n
    else:
        return 'Matriz no Hermitiana'

def Variance(Matriz, Ket):
    m = Op.multiplicacionMatrizMatriz(CalculoMedia(Matriz, Ket), CalculoMedia(Matriz, Ket))
    return m
