# -*- coding: utf-8 -*-

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