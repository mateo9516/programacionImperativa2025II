
diccionario = {
    "1860098": "Mateo Echeverry", 
    "1556098": "Mateo Echeverry Correa",
    "2569066": "Juan Jose Cardona",
    "2569203": "Matias Henao"
}

### Buscar un elemento
print(diccionario["2569066"])

### Agrego
diccionario["2569151"] = "Joan Arcila"
print(diccionario["2569151"])

### eliminar 
diccionario.pop("1556098")
#print(diccionario["1556098"]) ### da error porque ya no existe

## Recorrer un diccionario
for codigo, nombre in diccionario.items():
    if nombre == "Joan Arcila":
        print("lo encontré, ", codigo)

