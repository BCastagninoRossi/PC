# -*- coding: utf-8 -*-

# SCOPE

# ver como funciona el main() y como llamar funciones

#ejercicios

# def weridage (father, son):
#     '''
#     Calcula la cantidad de años hacia adelante o hacia atras que el padre debe tener para tener el doble de edad que el hijo actualmente
#     '''
#     return -(father - 2 *son)

# print(weridage(53, 25))

# def area_or_perimeter(x,y):
#     '''
#     Calcula el area si el cuadrilatero es un cuadrado y el perimetro si es un rectangulo
#     '''
#     if x == y:
#         return x*y
#     return 2*x + 2*y
    

def poinperator (operation: str)->str:
    dot1 = 0
    dot2 = 0
    op = None
    for character in operation:
        if character == '.' and op is None:
            dot1 += 1
        if character != " " and character !='.':
            op = character
        if character == '.' and op is not None:
            dot2 += 1
    if op == '+':
        return (dot1+dot2) * '.'
    elif op == '-':
        return (dot1-dot2) * '.'
    elif op == '/':
        return (dot1/dot2) * '.'
    elif op == '*':
        return (dot1 * dot2)* '.'
    
        
    
    
poinperator('........... + ..')