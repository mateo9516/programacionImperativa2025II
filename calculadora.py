import math

continuar = "" 
while continuar!="salir":
    a = int(input("Digite el valor de A "))
    b = int(input("Digite el valor de B "))
    ## Aqui imprimo las opciones

    print("1. raiz cuadrada de la suma de a + b")
    print("2. A/B")
    print("3. (A*B)/2.5")
    opcion = int(input("por favor digite la opcion "))
    resultado = 0
    if opcion == 1:
        resultado = math.sqrt(a+b)
        #resultado = (a+b)**0,5
    elif opcion == 2:
        if b != 0:
            resultado = a/b
        else:
            print("Error")
    elif opcion == 3:
        resultado = (a*b)/2.5
    else:
        print("Opcion no valida")

    print(resultado)

    continuar=input("si desea salir digite salir ")