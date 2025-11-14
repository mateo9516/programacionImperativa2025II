### una pequeña agenda con funciones

### numero de celular : [nombre, direccion, relacion]
agenda = {}

def agregar(nombre, direccion, numero, relacion):
    registro = [nombre, direccion, relacion]
    agenda[numero] = registro

def actualizarNombre(numero, nombre):
    agenda[numero][0] = nombre


#############################################
#### Poner el menu en una funcion
print("Bienvenido a la agenda")
while True:
    print("Escoja una opcion para continuar")
    print("1. Crear un contacto")
    print("2. Actualizar un contacto") ### Actualizar direccion, relacion o nombre
    print("3. Buscar un contacto, por nombre") ### Si hay 2 retorna el primero
    print("4. Eliminar un contacto")
    print("5. mostrar cuantas personas hay de la misma relacion") ### es decir si hay 4 amigos, mostrar los nombres
    print("6. cambiar el numero de un contacto") ### misma informacion diferente numero sin solicitar la informacion de nuevo
    print("7. mostrar en orden alfabetico las personas guardadas en la agenda y su relacion")
    print("8. Ver Agenda")
    print("0. salir")

    opcion = int(input("Digite la opcion que desea"))
    if opcion == 1:
        nombre = input("ingrese el nombre de la persona ")
        numero = input("ingrese el numero de la persona ")
        direccion = input("ingrese la direccion de la persona ")
        relacion = input("ingrese su relacion con la persona")

        agregar(nombre, direccion, numero, relacion)
    elif opcion == 2:
        numero = input("ingrese el numero de la persona a modificar")
        nuevo_nombre = input("ingrese el nombre nuevo")
        actualizarNombre(numero, nuevo_nombre)
    elif opcion == 5:
        for numero, datos in agenda.items():
            print(numero, "info: ", datos)
    elif opcion == 0:
        break