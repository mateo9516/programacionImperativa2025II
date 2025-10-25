### split 

nombres = "mateo, carlos, liceth, sofia, ana, mario"
frutas = "manzana-pera-uva-banano-mora-fresa"

lista_nombres = nombres.split(", ")
lista_frutas = frutas.split("-")

print(lista_frutas)

for name in lista_nombres:
    print(name)
