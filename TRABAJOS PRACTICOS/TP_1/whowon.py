# -*- coding: utf-8 -*-


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
    while ganador.lower() != player1.lower() and ganador.lower() != player2.lower():
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
