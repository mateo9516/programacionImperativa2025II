### ejemplo del ciclo while

palabra = ""

while palabra != "salir":
    palabra = input("ingrese una palabra")

    if palabra == "merequetengue":
        #print("xD")
        continue

    if palabra == "terminar":
        print("terminado")
        break

    print("hola, repito ",palabra)


