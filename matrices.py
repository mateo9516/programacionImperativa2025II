matriz = [[1,2,3],[3,4,5],[6,7,8]]

matricita = [
    [10,11,12],
    [13,14,15],
    [16,17,18]
    ]
#### forma 1 
def recorrido1(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j])

#### forma 2
def recorrido2(matriz):
    for fila in matriz:
        for elemento in fila:
            print(elemento)

def sumaFilas(matriz):
    salida = []
    for fila in matriz:
        suma = 0
        for elemento in fila:
            suma = suma + elemento
        salida.append(suma)
    return salida

print(sumaFilas(matricita))