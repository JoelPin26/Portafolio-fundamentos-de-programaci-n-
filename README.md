# Portafolio-fundamentos-de-programación-
# Qué es Python?
Python es un lenguaje de programación interpretado cuya filosofía hace hincapié en una sintaxis que favorezca un código legible. Y define este como un lenguaje multiparadigma, debido a que soporta orientación a objetos, programación imperativa y en menor medida programación funcional. Es interpretado de tipado dinámico y multiplataforma.
# Qué es una variable?
Una variable es un espacio reservado de memoria que te permite almacenar diferentes tipos de valores. Y este valor puede ser un número, una cadena de texto, decimales, valores entre verdadero y falso.
## Nombrando una variable
La creación de variables se realiza a través de la asignación de un valor a la misma. El operador de asignación en Python es el “=“

- x = 100
De derecha a izquierda
"correcto"
- 100 = x
De izquierda a derecha
"incorrecto"
## Asignando valores a una variable

- Asignación en la misma línea:
  - x = 5; y = 9; z = 12
- Asignación múltiple:
  - day, month, year = “miércoles”,”mayo”, 2016
- Asignación del mismo valor:
  - largo = ancho = 4
- Asignación de intercambio:
  - base = 15; altura = 30
  - base, altura = altura, base
		
## Operadores básicos
- suma (+)
- resta (-)
- multiplicacion (*)
- division (/)
- division euclidiana (cociente)(//)
- módulo (%)
- potencia (** )
### Ingreso y salida 
input:Esta función permite obtener el texto escrito por el usuario, el cual se asignará a un espacio de memoria con el nombre que el programador vea conveniente.

```python      
#Entrada 
num=int(input("ingrese un numero:"))
```
### Suma
La suma se realiza uniendo el valor de 2 o más numeros (+)
```python
#Aqui ya se le asigna valor a las variables
 num1=7
 num2=5
 sum1=num1+num2
 print(num1,'+',num2,'=',sum1)
```
```python
#Aqui se debe ingresar valor a los numeros por consola
 num1=int(input("ingrese un numero:"))
 num2=int(input("ingrese un numero:"))
 sum1=num1+num2
 print(num1,'+',num2,'=',sum1)
```
### Resta
La resta se realiza quitando valores entre 2 o mas numeros(-)
```python
#Aqui ya se le asigna valor a las variables
num1=10
num2=9
resta=num1-num2
print(num1,'-',num2,'=',resta)
```
```python 
#Aqui se debe ingresar valor a los numeros por consola
num1=int(input("ingrese un numero:"))
num2=int(input("ingrese un numero:"))
resta=num1-num2
print(num1,'-',num2,'=',resta)
```
### Multiplicación
Operación aritmética que consiste en calcular el resultado (producto) de sumar un mismo número (multiplicando) tantas veces como indica otro número (multiplicador); se representa con los signos · o ×.
```python
#Aqui ya se le asigna valor a las variables
num1=4
num2=6
mult=num1*num2
print(num1,'*',num2,'=',mult)
```
```python
#Aqui se debe ingresar valor a los numeros por consola
num1=int(input("ingrese un numero:"))
num2=int(input("ingrese un numero:"))
mult=num1*num2
print(num1,'*',num2,'=',mult)
```
### División
La división es aquella operación matemática mediante la cual se trata de descomponer un número,en tantas partes como así lo indique otro número
```python
#Aqui ya se le asigna valor a las variables
num1=10
num2=7
divi=num1/num2
print(num1,'/',num2,'=',divi)
```
```python
#Aqui se debe ingresar valor a los numeros por consola
num1=int(input("ingrese un numero:"))
num2=int(input("ingrese un numero:"))
divi=num1/num2
print(num1,'/',num2,'=',divi)
```
### Módulo
El operador módulo da como resultado el resto de la división entera
```python
#Aqui ya se le asigna valor a las variables
num1=10
num2=7
modulo=num1%num2
print(num1,'%',num2,'=',modulo)
```
```python
#Aqui se debe ingresar valor a los numeros por consola
num1=int(input("ingrese un numero:"))
num2=int(input("ingrese un numero:"))
modulo=num1%num2
print(num1,'%',num2,'=',modulo)
```
# Tipos de datos en Python
Los tipos de datos serían:
- Numeros enteros
- Numeros de punto flotante
- Texto (cadenas de caracteres)
- Booleanos (Verdadero y falso)
## Integer
int= un numero entero como 21,7,8, etc. Ademas en este caso ya les asigne valor a la varibale dia
```python
dia=17
print(type(dia)) #imprimirá que tipo de dato es.
```
## Float
float= un numero decimal como 21.5;15.6;8.5, etc. Ya aqui le asigne valor
```python
dia=21.5
print(type(dia)) #imprimirá que tipo de dato es.
```
## String
string= Caracteres
```python
dia="lunes"
print(type(dia)) #imprimirá que tipo de dato es.
```
## Casting en Python
El casting es la tecnica que sirve para convertir un dato de un tipo a un tipo de dato diferente
```python
 int a str: str(45)
 str a int: int ("123")
 float a int: int (3.5)
```
## List
Una lista es una estructura de datos en Python que es una secuencia de elementos ordenados mutables o cambiables. Cada elemento o valor que está dentro de una lista se denomina elemento. Así como las cadenas se definen como caracteres entre comillas, las listas se definen con valores entre corchetes [ ]
```python
list = [ 1,6,9,["uno",seis","nueve"]]
print(list)
```
## Tuple
Una tupla es una colección de objetos de Python separados por comas. De alguna manera, una tupla es similar a una lista en términos de indexación, objetos anidados y repetición, pero una tupla es inmutable a diferencia de las listas que son mutables.
```python
()
(1,2,4,5,6,7,8,9)
("Hola", "me", "llamo","Joel")
```
## Dictionary
Un Diccionario es una estructura de datos y un tipo de dato en Python con características especiales que nos permite almacenar cualquier tipo de valor como enteros, cadenas, listas e incluso otras funciones. Estos diccionarios nos permiten además identificar cada elemento por una clave (Key).
```python
d= {'clave1': [1,2,3]
    'clave2': {true}
print[]
```
# Tomando decisiones
- Las palabras clave if,elif,else permieten dirigir el camino por el que va a avanzar el programa dependiendo de una o varias condiciones
- Luego de los dos puntos(:), dejamos 4 espacios de sangria en la siguiente linea o una tabulación
## Sentencia if
Es una forma común de controlar el flujo de un programa, lo que te permite ejecutar bloques de código específicos según el valor de algunos datos. Si la condición que sigue a la palabra clave if se evalúa como verdadera, el bloque de código se ejecutará.
```python
#Escribir un programa que solicite un valor entero al usuario
#determine si es par o impar
num=int(input("ingrese numero:"))


if (num%2==0):
    print("El numero es par",)
    print(num,"es par")
else:
    print("El numero es impar")  
```
## Ciclo For
El bucle for se utiliza para recorrer los elementos de un objeto iterable (lista, tupla, conjunto, diccionario, …) y ejecutar un bloque de código. En cada paso de la iteración se tiene en cuenta a un único elemento del objeto iterable, sobre el cuál se pueden aplicar una serie de operaciones.
```python
# Calcular la suma y la media aritmetica de Nnumeros reales. 
# solicitar el valor de n al usuario y cada uno de los N números reales.

n = int(input("Ingrese los números que desee: "))
suma= 0
for i in range(n):
    nota =int(input('Ingrese el número' + str (i+1) +  ':'))
    suma += nota
    
promedio = suma/n 
print("promedio:", promedio)
```
## Ciclo While
El bucle while evalúa una condición y luego ejecuta un bloque de código si la condición es verdadera. El bloque de código se ejecuta repetidamente hasta que la condición llega ser o es falsa.
```python
#10-20

num=11

while num<10 or num >20 or num%2!=0:
    num=int(input("ingrese numero:"))

print("se fue")
```
## Break
La instrucción break le proporciona la oportunidad de cerrar un bucle cuando se activa una condición externa.
```python
j=0
for i in range (10):
    j+=2
    print ("i;",i,"j:",j)
    if j==10:
        break
```
## Continue
La instrucción continue da la opción de omitir la parte de un bucle en la que se activa una condición externa, pero continuar para completar el resto del bucle.
```python
contador=0
for i in range (10):
    for j in range (10):
        contador +=1
        print ("i:",i,"j:",j)
        if contador >50:
            continue
print ("contador:",contador)
```
