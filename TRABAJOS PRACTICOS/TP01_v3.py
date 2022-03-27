#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 18:19:06 2022

@author: brunocr
"""

def showscore (player: str, s: int)->str:
    
    """ Transforma el puntaje en int de 0 al 5 de cada jugador en puntaje equivalente según reglamento de tenis.
    También muestra en la consola el puntaje del jugador y si este ha ganado

    Args:
        -player(str): el jugador de quien se calcula el puntaje
        -s(int): el puntaje en int de dicho jugador
        
    Print:
        Imprime en la consola el nombre del jugador y su puntaje según reglamento de tenis
        Si el jugador ha ganado el game, esto es impreso en la consola sin el puntaje

    """    
    result = 0
    if s == 1:
        result = 15
    elif s == 2:
        result = 30
    elif s == 3:
        result = 40
    elif s == 4:
        result = "AD"
    elif s == 5:
        print(f'\n{player} ha ganado el game!')
        return
    print(f'\n-{player}: {result}')

def whowon (player1: str, player2: str, score1: int, score2: int, winner:str)->int:
    
    """ Recibe los nombres de los jugadores, sus puntajes y quén ha ganado el último punto.
        Calcula el puntaje de ambos del 0 al 5 y retorna los nuevos puntajes. 

    Args:
        -player1(str): Nombre del jugador1
        -player2(str): Nombre del jugador2
        -score1(int): Puntaje del jugador1
        -score2(int): Puntaje del jugador2
        -winner(str): Nombre del jugador que ha ganado el último punto
    Return:
        -score1, score2(int): puntajes actualizados según quien ha ganado el último punto
    """
    
    ganador = winner
    while ganador == False or (ganador.lower() != player1.lower() and ganador.lower() != player2.lower()):
        ganador = input("Ha ingresado un término invalido, ingrese qué jugador ha ganado el punto: ")
    if ganador.lower() == player1.lower():
        if score1 == 3 and score2 < 3:
            score1 = 5 
        else:
            score1 += 1
    elif ganador.lower() == player2.lower():
        if score2 == 3 and score1 < 3:
            score2 = 5   
        else:
            score2 += 1
    if score1 == 4 and score2 == 4:
        score1 = 3
        score2 = 3
    return score1, score2

def game (mode: str, player1: str, player2: str, score1: int, score2: int):
    
    """ Analiza la modalidad de ejecución seleccionada y permite 
    contabilizar un game de tenis ya sea ingresando al ganador de manera manual 
    o corriendo una simulación.

    Args:
        -player1(str): Nombre del jugador1
        -player2(str): Nombre del jugador2
        -score1(int): Puntaje del jugador1
        -score2(int): Puntaje del jugador2
        -mode(int): modo de ejecucion del programa
    """
    if mode == '2':
        submode = input("Ingrese la modalidad de simulación:\n1. DESGLOSE COMPLETO\n2. SOLO MOSTRAR GANADOR\n")
        while not submode or (submode != '1' and submode != '2'):
            submode = input('Ha ingresado un modo inválido, intente nuevamente: ')
        import random 
        player_tuple = (player1, player2)
        while score1 != 5 and score2 != 5 :
            if submode == '1':
                    showscore(player1, score1)
                    showscore(player2, score2)
                    randomplayer = random.choice(player_tuple)
                    print(f'\nQuién ha ganado el punto? {randomplayer}')
                    score1, score2 = (whowon(player1, player2, score1, score2, randomplayer))
            else:
                randomplayer = random.choice(player_tuple)
                score1, score2 = (whowon(player1, player2, score1, score2, randomplayer))
        if score1 == 5:
            showscore(player1, score1)
        else:
            showscore(player2, score2)
    else:
        while score1 != 5 and score2 != 5 :
            showscore(player1, score1)
            showscore(player2, score2)
            score1, score2 = (whowon(player1, player2, score1, score2, input('Quién ha ganado el punto? ')))
        if score1 == 5:
            showscore(player1, score1)
        else:
            showscore(player2, score2)

def mod()->str:
    '''Pide al usuario que ingrese el modo de ejecucion que desea, 1 o 2. 
    De ingresar un término inválido solicita al usuario que intente nuevamente
    Return: -mode(str)
    '''
    mode = input("Ingrese el modo de ejecución que desea:\n1. MANUAL\n2. SIMULACION\n").lower()
    while not mode or (mode != '1' and mode != '2'):
        mode = input('Ha ingresado un modo inválido, ingrese el modo de ejecución nuevamente:\n')
    return mode

def p1()->str:
    '''Pide al usuario que ingrese el nombre del primer jugador. 
    De no ingresar un término solicita al usuario que intente nuevamente
    Return: -player1(str)
    '''
    player1 = input('Ingrese el nombre del primer jugador: ')
    while not player1:
        player1 = input('Ha ingresado un término inválido, ingrese el nombre nuevamente:\n')
    return player1

def p2()->str:
    '''Pide al usuario que ingrese el nombre del segundo jugador. 
    De no ingresar un término solicita al usuario que intente nuevamente
    Return: -player2(str)
    '''
    player2 = input('Ingrese el nombre del segundo jugador: ')
    while not player2:
        player2 = input('Ha ingresado un término inválido, ingrese el nombre nuevamente:\n')
    return player2

   
def main():
    print(' %%% VIRTUA TENNIS GAMMA %%% ' )
    game(mod(), p1(), p2(), 0, 0)
if __name__=='__main__':
    main()
              