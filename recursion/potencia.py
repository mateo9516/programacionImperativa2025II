
def potencia(a,b):
    if b == 0:
        return 1
    else:
        return a * potencia(a,b-1)

def inv_cadena(cadena):
    if len(cadena) == 1:
        return cadena
    else:
        return inv_cadena(cadena[1:]) + cadena[0]
    
#print(potencia(2,5))
print(inv_cadena("mateo"))


