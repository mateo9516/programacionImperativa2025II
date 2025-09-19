#### Creando una lista

lista = [1,3,4,6,7]
print(lista)
## añadir un elemento
lista.append(10)
print(lista)

## añadir un elemento en una posicion indicada
lista.insert(1,2) ### (posicion, elemento)
print(lista)

### Eliminar un elemento
lista.pop() ## eliminar el ultimo
print(lista)

lista.pop(3) ### elimino la posicion indicada
print(lista)

lista.remove(6) ### elimina el elemento indicado
print(lista)

lista2 = [10,20,40,50]

lista.extend(lista2)

print(lista)
lista3 = [10,1,3,40]
lista.extend(lista3)
print(lista)

### conocer el tamaño de la lista

print(len(lista))
