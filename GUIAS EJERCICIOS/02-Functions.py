# -*- coding: utf-8 -*-

### 2. ★☆☆ Escriba una función que devuelva el cuadrado de un número (sin utilizar el operador de potencia
# del lenguaje de programación).

# def power_2 (n):
#     return n * n

# print (power_2(4)

### 3. ★☆☆ Escriba una función llamada sumador que recibe dos argumentos y devuelva su suma. Luego,
# ejecute pruebas con distintos tipos de datos (dos strings, dos en punto flotante, un int y un str, etc.)

# def sumador (a, b):
#     '''suma a + b'''
#     r = a + b
#     return r

# # print (sumador(2, 3))
# # print (sumador(2.0, 3.5))
# # print (sumador("hola", "mundo"))
# # print (sumador(2, 'mundo'))

### 4. ★☆☆ Corrija la siguiente función defectuosa para que devuelva la multiplicación entre dos números:
# def multiply(a, b):
#     answer = a * b
#     return answer

# print(multiply(2, 5))

### 5. ★☆☆ Implemente una función que solicite un número por la consola, que represente el radio de una
# circunferencia, y muestre en pantalla el perímetro de dicha circunferencia. En la consola se debe ver lo
# siguiente:
#Ingrese un valor que representa el radio de una circunferencia: [ENTRADA]
#El perímetro resultante es [RESULTADO]

# def perimeter ():
#     '''solicita un radio y devuelve el perimetro de la circunferencia'''
#     r = float(input("Ingrese un valor que representa el radio de una circunferencia: "))
#     print (f"El perímetro resultante es {(2 * 3.141592653589793 * r):.2f}")
    
# perimeter()

### 6. ★★☆ Para la función definida en el siguiente código, encuentre una implementación alternativa que
# permita implementar la misma función pero reduciendo las 7 líneas del cuerpo de su definición a un cuerpo
# de sólo 2 líneas.

# def some_function(first_word, second_word, third_word, fourth_word):
#     print(f' Name: {first_word + " " + second_word} \n Age: {third_word} years\n Profession: {fourth_word}')

# some_function('Bruno', 'Castagnino', 28, 'Médico')

### 7. ★★☆ Escriba una función que redondee un número de tipo flotante al entero más cercano y devuelva
# este número entero.
# Escriba un programa que pida al usuario el número y muestre en la consola interactiva el resultado
# de ejecutar la función desarrollada.

# def round (n: float)-> int:
#     if n - int(n) >= 0.5:
#         res = int(n)+1
#     else:
#         res = int(n)
#     return res

# n = float(input("Ingrese el numero a redondear: "))
# print ('El número entero más cercano es ', round(n))

### 8. ver enunciado en guia

# def simple_capital (initial_capital: float, annual_interest: float, periods: float)->float:
#     '''calculates total capital after a number of years of pericieving an annual simple interest
    
#     inputs:
#         - initial_capital
#         - interest_per_period
#         - periods
        
#     output: total_capital
#     '''
#     total_capital = initial_capital * (1 + periods * annual_interest)
#     return total_capital

# initial_capital = float(input('Ingrese el capital inicial en $: '))
# annual_interest = float(input('Ingrese el interés anual en porcentaje: ')) / 100
# periods = float(input('Ingrese cantidad de años transcurridos: '))
# print(f"El capital total luego de {periods} años es de ${simple_capital(initial_capital, annual_interest, periods)}")

### 9. ver enunciado en guia

# def compound_capital (initial_capital: float, annual_interest: float, periods: float)->float:
#     '''calculates total capital after a number of years of pericieving an annual compound interest
    
#     inputs:
#         - initial_capital
#         - interest_per_period
#         - periods
        
#     output: total_capital
#     '''
#     total_capital = initial_capital * (1 + annual_interest) ** periods
#     return total_capital

# initial_capital = float(input('Ingrese el capital inicial en $: '))
# annual_interest = float(input('Ingrese el interés anual en porcentaje: ')) / 100
# periods = float(input('Ingrese cantidad de años transcurridos: '))
# print(f"El capital total luego de {periods} años es de ${compound_capital(initial_capital, annual_interest, periods)}")

### 10. ver enunciado en guia

# def effective_interest (nominal_interest: float, period_length: float)->float:
#     '''calculates annual effective iterest rate after n month cycles
    
#     inputs:
#         - nominal_interest
#         - periods
        
#     output: effective_interest
#     '''
#     cycles = 12 / period_length
#     effective_interest = 100 * ((1 + nominal_interest / cycles) ** cycles - 1)
#     return effective_interest

# nominal_interest = float(input('Ingrese el interés nominal anual en porcentaje: ')) / 100
# period_length = float(input('Ingrese la duración en meses de cada ciclo: '))
# print(f"La tasa efectiva anual para ciclos de {period_length} meses es de %{(effective_interest(nominal_interest, period_length)):.3f}")

### 11. ver enunciado en guia

# def future_capital (period_capital: float, period_interest: float, periods: float)->float:
#     '''calculates future capital after a number of periods of pericieving an interest over each's period investment
    
#     inputs:
#         - period_capital
#         - period_interest
#         - periods
        
#     output: 
#         - total_capital
#     '''
#     total_capital = (period_capital * ((1 + period_interest) ** periods - 1)) / period_interest
#     return total_capital

# period_capital = float(input('Ingrese el capital a invertir en cada ciclo en $: '))
# period_interest = float(input('Ingrese el interés nominal por cada período en porcentaje: ')) / 100
# periods = float(input('Ingrese cantidad de períodos a calcular: '))
# print(f"El capital total luego de {periods} períodos es de ${(future_capital(period_capital, period_interest, periods)):.2f}")


## 12. ★★☆ Escriba una función que dadas la hora, minutos y segundos devuelva el tiempo en segundos.
# Escriba un programa que pida la hora al usuario y muestre el tiempo en segundos.

# def timeinseconds (h: int, m: int, s: int)-> int:
#     ''' recieves a time in hour, minute, seconds format and returns said time in seconds
    
#     Inputs:
#         -h : hours
#         -m : minutes
#         -s : seconds
#     Returns:
#         total_seconds
#     '''
#     total_seconds = h * 360 + m * 60 + s
#     return total_seconds

# h = int(input("ingrese las horas: "))
# m = int(input('ingrese los minutos: '))
# s = int(input('ingrese los segundos: '))
# print (f'la hora en segundos es {timeinseconds(h, m, s)}')

### 13. ★★★ Escriba una función que dado un número devuelva el primer número múltiplo de 10 inferior o
# igual a él. Por ejemplo, para 153 debe devolver 150.

# def multipleten (n: float) -> int:
#     '''Retorna el múltiplo de 10 inferior más cercano a un número n'''
#     if n % 10 == 0:
#         multiple = n
#     else:
#         multiple = n - n%10
#     return multiple

# n = float(input('Ingrese un número: '))
# print (f'El primer número múltiplo de 10 inferior o igual al número ingresado es {multipleten(n)}')

### 14. 14. ★★★ Escriba una función que dado un tiempo en segundos, retorne el tiempo en horas, minutos y
# segundos (similar al ejercicio 12). 

# def secondstotime (s: int)-> str:
#     '''convierte una hora ingresada en segundos en formato XXh:XXm:XXs
#     '''
    
#     hours = int (s / 3600)
#     minutes = int ((s % 360)/ 60)
#     seconds = (s % 360) % 60 
#     return f"La hora es {hours}h {minutes}m {seconds}s"

# s = int (input('Ingrese el tiempo en segundos: '))
# print(secondstotime(s))




















