### Calculadora con funciones

def sumar(a,b):
    return a + b

def restar(a,b):
    return a - b

def multiplicar(a,b):
    return a * b

def dividir(a,b):
    return a/b

def saludar():
    return "Holi"

def recibirDatos(cadena):
    v1 = 0
    v2 = 0
    signo = ""
    pivote = 0
    for i in range(len(cadena)):
        if cadena[i] == '+' or cadena[i] == '*' or cadena[i] == '-' or cadena[i] == '/':
            signo = cadena[i]
            pivote = i
            v1 = int(cadena[:pivote])
            v2 = int(cadena[pivote+1:])

    #### logica para separar la cadena 3+3
    return v1, v2, signo

signo = ""

while signo != "salir":
    expresion = input("ingrese la expresion")
    valor1, valor2, signo = recibirDatos(expresion)
    print(saludar())
    if signo == "+":
        print(sumar(valor1, valor2))
    elif signo == "-":
        print(restar(valor1,valor2))
    elif signo == "*":
        print(multiplicar(valor1, valor2))
    elif signo == "/":
        print(dividir(valor1, valor2))
    else:
        if signo == "":
            continue
        print("signo no valida")