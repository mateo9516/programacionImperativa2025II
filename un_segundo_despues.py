
hh = int(input("ingrese la hora: "))
mm = int(input("ingrese los minutos: "))
ss = int(input("ingrese los segundos: "))

if hh<24 and mm<60 and ss<60:
    ss = ss + 1
    if ss == 60:
        ss = 0
        mm = mm + 1
        if mm == 60:
            mm = 0
            hh = hh + 1
            if hh == 24:
                hh = 0
else:
    print("el formato de hora no es valido")

print(hh,":",mm,":",ss)