## funciones en arreglos
l = [1,3,5,2,1,5,7,2,4,8]
s = [6,2,5,2,2]
r = [4,6,6,5,5]

def media(a):
    suma = 0
    for i in a:
        suma = suma + i
    
    return suma/len(a)

print(media(l))
print(media(s))
print(media(r))