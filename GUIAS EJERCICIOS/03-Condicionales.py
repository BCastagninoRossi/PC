# -*- coding: utf-8 -*-

# 1)

state = True
print(not state)

# 2)
cake = True
if cake == True:
 print("cake es True")
else:
 print("The cake is a lie")
 
 # 3)
 def is_even(number: int) -> bool:
     if number % 2 == 0:
         return True
     else:
         return False
     
# 4)
def cmp_number(a: float, b: float) -> float:
    if a == b:
        return 0
    elif a < b:
        return -1
    else:
        return 1

# 5)
def multdiv ()->float:
    '''computes x*y and x/y'''
    try:
        x = input('Ingrese el primer número:\t')
        y = input('Ingrese el segundo número:\t')
        x = float(x)
        y = float(y)
    except:
        print('Ha ingresado al menos un término no numérico')
    assert y != 0, 'No es posible dividir por 0'
    print(f'El resultado de la multiplicación es {x} * {y} = {x*y}')
    print(f'El resultado de la división es {x}/{y} = {x/y}')
    
    
# 6)
def boolean(a:bool, b:bool, c:bool)->bool:
    if (a == True and b==False and c == False) or (a == True and b == True and c == False) or(a == True and b == True and c == True):
        x = True
    else:
        x = False
    print('| a | b | c | x |\n|---|---|---|---|\n| 0 | 0 | 0 | 0 |\n| 0 | 0 | 1 | 0 |\n| 0 | 0 | 1 | 0 |\n| 0 | 1 | 0 | 0 |\n| 0 | 1 | 1 | 0 |\n| 1 | 0 | 0 | 1 |\n| 1 | 0 | 1 | 0 |\n| 1 | 1 | 0 | 1 |\n| 1 | 1 | 1 | 1 |')
    return x
            
            
            
# 7)
import math

def resolvente(a: float, b: float, c: float)-> str:
    '''calculates roots of cuadratic function
    args:
        -a(float): multiplies x**2
        -b(float): multiplies x
        -c(float): independent term
    return:
        x1, x2(float): roots of the equation
    '''
    if (b**2-4*a*c) < 0:
        return 'La ecuación no tiene raices reales'
    elif (b**2-4*a*c) == 0:
        return f'La ecuación tiene una raíz doble que es {-b/(2*a)}'
    else:
        root = math.sqrt(b**2-4*a*c)
        x1 = (-b + root)/(2*a)
        x2 = (-b - root)/(2*a)
        return f'X1 es {x1:.3f}\nX2 es {x2:.3f}'
    
#8)
def dia (day_num: int)-> str:
    assert day_num > 0 and day_num <= 366, "Debe ingresar un número del 1 al 366" 
    if day_num % 7 == 0:
        return 'domingo'
    elif day_num % 7 == 1:
        return 'lunes'
    elif day_num % 7 == 2:
        return 'martes'
    elif day_num % 7 == 3:
        return 'miercoles'
    elif day_num % 7 == 4:
        return 'jueves'
    elif day_num % 7 == 5:
        return 'viernes'
    else:
        return 'sábado' 
    
# 9)
def intersection (a1: float, b1: float, a2: float, b2: float)-> float:
    if a1 == a2 and b1 == b2:
        return 'Las rectas son coincidentes' 
    elif a1 == a2:
        return 'Las rectas son paralelas, no se intersecan en ningún punto' 
    else:
        cross = (b1-b2)/(a2-a1)
        return f'La abscisa donde se intersecan es X= {cross}' 
    
    
# 10)
# a)
def bisiesto (year: int)->bool:
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False 
    
# b)
def daymonth (year: int, month: int)-> int:
    if month != 2:
        if month < 8:
            if month % 2 == 0:
                return 30
            else:
                return 31
        else:
            if month % 2 == 0:
                return 31 
            else:
                return 30
    else:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            return 29
        else:
            return 28 
    
#c) 
def valid_date (d: int, m: int, a: int)->bool:
    days = daymonth(a, m)
    if d <= days:
        return True
    else:
        return False
    
# d)
def pending_month (d: int, m: int, a: int)-> int:
    assert valid_date(d, m, a) == True, 'Ha ingresado una fecha inválida'
    days = daymonth(a, m)
    pending = days - d
    return pending

#e)
def pending_year(d: int, m: int, a: int)-> int:
    assert valid_date(d, m, a) == True, 'Ha ingresado una fecha inválida'
    current = pending_month(d, m, a)
    d = 0
    while m < 12:
        m+=1
        d+= daymonth(a, m)
    return current + d
        
#f)
def days_gone_by(d: int, m: int, a: int)->int:
    assert valid_date(d, m, a) == True, 'Ha ingresado una fecha inválida'
    dm=0
    while m > 1:
        m -= 1
        dm+=daymonth(a, m)
    return d + dm

# g)
def days_appart (d1: int, m1: int, a1: int, d2: int, m2: int, a2: int)->int:
    assert valid_date(d1, m1, a1) == True and valid_date(d2, m2, a2) == True , 'Ha ingresado una fecha inválida'
    ydays = 0
    ydays1 = days_gone_by(d1, m1, a1)
    ydays2 = days_gone_by(d2, m2, a2)
    ydiff = abs(a2-a1)
    while ydiff >= 1:
        ydiff-=1
        if a1>a2:
            if bisiesto(a2)== False:
                ydays += 365
                a2+=1
            else:
                ydays += 366
                a2+=1
        else:
            if bisiesto(a1)== False:
                ydays += 365
                a1+=1
            else:
                ydays += 366
                a1+=1
    return abs(ydays1-ydays2) + ydays       
            
# ahora funciona pero nom me gusta                





























 