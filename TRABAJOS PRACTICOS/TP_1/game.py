# -*- coding: utf-8 -*-

from showscore import showscore
from whowon import whowon

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
        while submode != '1' and submode != '2':
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