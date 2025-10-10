cadena = "mateo"

#for letra in cadena:
 #   print(letra)

#for i in range(len(cadena)):
 #   print(cadena[i])

respuesta = ""
for i in range(len(cadena)):
    if cadena[i] in "aeiou":
        respuesta = respuesta + "x"
    else:
        respuesta = respuesta + cadena[i]
print(respuesta)
