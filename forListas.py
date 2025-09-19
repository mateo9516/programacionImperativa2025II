
### listar numeros desde 10 hasta 38 de 3 en 3 

numeros = []

for i in range(10,39,3):
    numeros.append(i)
print(numeros)

### generar una lista con los multiplos de 4 y eliminarlos de la original

multiplos4 = []

for i in range(len(numeros)):
    if numeros[i]%4 == 0:
        multiplos4.append(numeros[i])

print(multiplos4)

for i in range(len(multiplos4)):
    numeros.remove(multiplos4[i])

print(numeros)