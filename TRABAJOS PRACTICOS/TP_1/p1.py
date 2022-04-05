# -*- coding: utf-8 -*-

def p1()->str:
    '''Pide al usuario que ingrese el nombre del primer jugador. 
    De no ingresar un término solicita al usuario que intente nuevamente
    Return: -player1(str)
    '''
    player1 = input('Ingrese el nombre del primer jugador: ')
    while not player1:
        player1 = input('Ha ingresado un término inválido, ingrese el nombre nuevamente:\n')
    return player1
