from math import sqrt
var_pri = int(input("Ingrese Cateto Primero"))
var_seg = int(input("Ingrese Cateto Segundo"))
#ver_hipo = (((var_pri**2)+(var_seg**2))**0.5)
ver_hipo = sqrt((var_pri**2)+(var_seg**2))
print ("La hipotenusa buscada da",ver_hipo)
edad = int(input)
if (edad>=18):
    Print("Mayor de edad)")
else:
    print("Menor de Edad")