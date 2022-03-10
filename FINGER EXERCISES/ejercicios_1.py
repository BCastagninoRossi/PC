# -*- coding: utf-8 -*-

### Ejercicio 3

# 2 * var - seg = 150

#1 = True No se puede asignar valor a True

# a = b = "la puerta azul está abierta" 

# x = 5
# y = 10

# suma = 30

### Ejercicio 4

# x, y, z = 0.1, 25, 'azúl'   

### Ejercicio 5

# num1, num2 = 2, 2
# answer = num1 + num2 #La mayúscula de Answer generaba una variable distinta de answer
# print(answer)

### Ejercicio 6

# num1, num2 = 6, 3
# answer = num1 / num2 # % devuelve el resto de la division, habia que cambiarlo a /
# print(answer)

### Ejercicio 7

# num1, num2 = 2, 2
# answer = num1 ** num2 # La sintaxis correcta de la potenciacion es **
# print(answer)

### Ejercicio 8

# x = '5'
# respuesta = 'el resultado es ' + x

### Ejercicio 9

# peras = 5
# manzanas = 7
# frutas = peras + manzanas
# print('Hay', frutas, 'frutas en total.')

### Ejercicio 10

##Parte a)
# a, b = 4, 5

# print ( a * b)

##Parte b)
# a = float(input('Ingrese el primer número a multiplicar'))
# b = float(input('Ingrese el segundo número a multiplicar'))
# print('El resultado es ', a * b )

### Ejercicio 11
 
# def greet():
#     name = input("Cuál es su nombre?") 
#     msg = "Hola, " 
#     return msg + name

# print(greet())


# def greet_msg(name):
#     return 'Hola, ' + name

# print(greet_msg('Brunelo'))

### Ejercicio 12

#  Un grupo de 5 amigos se va a juntar a comer en la casa de uno de ellos. El anfitrión dice que él y
# su pareja van a comprar las pizzas y han estimado que se comerán, en promedio, 4 porciones por cabeza. El
# resto del grupo se ofreció a traer bebidas, picada y postre. Uno de ellos no puede traer nada y los otros dos
# decidieron que uno llevará las bebidas y la picada ($410), y el otro el postre ($800). En la pizzería favorita
# del anfitrión, una pizza mediana (6 porciones) cuesta $1020, y una grande (8 porciones) $1380,
# independientemente del sabor.
# Implementar una función llamada main() que imprima por pantalla:
# El costo total de la juntada.
# La cantidad de dinero que gastó cada uno antes de ir a la cena.
# Cuánto dinero debe aportar cada uno.
# Quién le debe dinero a quién, y cuánto es el monto.

def main():
    anfitrion = float(input('Cuánto dinero gastó el anfitrión?'))
    pareja = float(input('Cuánto dinero gastó la pareja del anfitrión?'))
    invitado1 = float(input('Cuánto dinero gastó el primer invitado?'))
    invitado2 = float(input('Cuánto dinero gastó el segundo invitado?'))
    invitado3 = float(input('Cuánto dinero gastó el tercer invitado?'))
    
    total = anfitrion + pareja + invitado1 + invitado2 + invitado3
    
    personal = total/5
    

print(main())
    
    


