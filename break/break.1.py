#Crear un programa que cuando encuentre la letra "g", pare.
cadena = 'programacion'
for letra in cadena:
    if letra == 'g':
        print("Se encontró la g")
        break
    print(letra)