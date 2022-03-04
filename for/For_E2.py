import sys
n=5
suma=0
baja= sys.maxsize 


for i in range(n):
    nota =int(input('ingrese nota' +str(i+1)+':'))
    suma += nota
    if nota< baja:
        baja=nota
        
print ("La calificacion mas baja es :",baja )
print("La media es:",suma/n)

#print(type("Hello world"))