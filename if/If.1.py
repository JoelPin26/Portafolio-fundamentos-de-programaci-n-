#Dada la fecha de hoy
#Calcular la fecha del dia siguiente
#Suponer que el año no es bisiesto

print ("Ingrese fecha")
año=int(input("Introduzca el año:"))
mes=int(input("Introduzca el mes:"))
dia=int(input("Introduzca el dia:"))
#def fecha_dia_siguiente(año,mes,dia):
    
if año%4==0 and  año%100!=0 or año%400==0:
    bisciesto= True   
else:
    bisciesto= False

if mes in(1,3,5,7,8,10,12):
    dias_mes=31
elif mes==2:
    if bisciesto:
        dias_mes=29
    else:
        dias_mes=28
else:
    dias_mes=30

if dia<dias_mes:
    dia+=1
else:
    dia=1
    if mes==12:
        mes=1
        año+=1
    else:
        mes+=1
    
##return(año,mes,dia)
#print (fecha_dia_siguiente(2020,1,15))
print(año,mes,dia)

#vida