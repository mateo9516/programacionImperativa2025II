numeros = [3,7,2,9,5]

## forma 1
for n in numeros:
    print(n)

## forma 2 ---> la mayoria
for i in range(len(numeros)):
    print(numeros[i])

### completar codigo
m = 10
while m>0 :
    print(m)
    m = m - 1

florecitas = [1,0,0,0,0,1]
n = 2
salida = False


for i in range(1,len(florecitas)):
    if florecitas[i-1] == 0 and florecitas[i] == 0 and florecitas[i+1] == 0:
        florecitas[i] = 1
        n = n-1
    if florecitas[0] == 0 and florecitas[1] == 0:
        florecitas[0] = 1
        n = n-1
    if florecitas[-1] == 0 and florecitas[-2] == 0:
        florecitas[-1] = 1
        n = n-1

if(n == 0):
    salida = True

print(salida)


j1 = [3,5,7,6]
j2 = [8,10,10,2]
puntos1=0
puntos2=0

for i in range(len(j1)):
    if(i>0):
        if(j1[i-1]==10):
            puntos1 = puntos1 + j1[i]*2
        else:
            puntos1 = puntos1 + j1[i]
    elif(i>1):
        if(j1[i-2] == 10):
            puntos1 = puntos1 + j1[i]*2
        else:
            puntos1 = puntos1 + j1[i]
    else:
        puntos1 = puntos1 + j1[i]

for i in range(len(j2)):
    if(i>0):
        if(j2[i-1]==10):
            puntos2 = puntos2 + j2[i]*2
        else:
            puntos2 = puntos2 + j2[i]
    elif(i>1):
        if(j2[i-2] == 10):
            puntos2 = puntos2 + j2[i]*2
        else:
            puntos2 = puntos2 + j2[i]
    else:
        puntos2 = puntos2 + j2[i]

if puntos1>puntos2:
    print("1")
else:
    print("2")


#### tercera

n = 10
p = 0
for i in range(1,n+1):
    p = p + i

print(p/n)
    