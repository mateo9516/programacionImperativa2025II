
tarifa = int(input("ingrese el valor de la hora "))
cantidad_horas = int(input("ingrese las horas trabajadas "))
nombre = input("ingrese el nombre del julano")
salario_neto = 0

if cantidad_horas > 35:
    ## Las horas extra se pagan a 1,5 
    salario_neto = tarifa*35 + (cantidad_horas - 35 ) *1.5*tarifa 
else:
    salario_neto = tarifa*cantidad_horas

if salario_neto > 2000 and salario_neto <= 2220:
    salario_neto = salario_neto -(salario_neto * 0.2) ## 20porciento sobre todo el sueldo
elif salario_neto > 2220:
    salario_neto = salario_neto -(salario_neto * 0.3) ##30 porciento sobre todo el sueldo

print(salario_neto)