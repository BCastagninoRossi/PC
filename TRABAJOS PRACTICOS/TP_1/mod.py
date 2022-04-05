# -*- coding: utf-8 -*-

def mod()->str:
    '''Pide al usuario que ingrese el modo de ejecucion que desea, 1 o 2. 
    De ingresar un término inválido solicita al usuario que intente nuevamente
    Return: -mode(str)
    '''
    mode = input("Ingrese el modo de ejecución que desea:\n1. MANUAL\n2. SIMULACION\n").lower()
    while mode != '1' and mode != '2':
        mode = input('Ha ingresado un modo inválido, ingrese el modo de ejecución nuevamente:\n')
    return mode