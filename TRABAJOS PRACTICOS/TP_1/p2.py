# -*- coding: utf-8 -*-


def p2()->str:
    '''Pide al usuario que ingrese el nombre del segundo jugador. 
    De no ingresar un término solicita al usuario que intente nuevamente
    Return: -player2(str)
    '''
    player2 = input('Ingrese el nombre del segundo jugador: ')
    while not player2:
        player2 = input('Ha ingresado un término inválido, ingrese el nombre nuevamente:\n')
    return player2