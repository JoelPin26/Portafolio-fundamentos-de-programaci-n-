contandor=0
for i in range(10):
    for j in range(10):
        contandor += 1
        print(i,j)
        break
#Nunca se realiza más de una iteración
#El break no afecta a este for
print("contandor:",contandor)
