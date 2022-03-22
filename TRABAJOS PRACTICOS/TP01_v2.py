#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 13:29:56 2022

@author: brunocr
"""

def showscore (player: str, s: int)->str:
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
        print(f'{player} ha ganado el game!')
        return
    
    print(f'-{player}: {result} \n')

def whowon (player1: str, player2: str, score1: int, score2: int, winner:str)->str:
    ganador = winner
    while ganador == False or (ganador.lower() != player1.lower() and ganador.lower() != player2.lower()):
        ganador = input("Ha ingresado un término invalido, ingrese qué jugador ha ganado el punto ")
        
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

def manualgame (player1, player2, score1, score2):
    
    while score1 != 5 and score2 != 5 :
        showscore(player1, score1)
        showscore(player2, score2)
        score1, score2 = (whowon(player1, player2, score1, score2, input('Quien ha ganado el punto? ')))
    
    if score1 == 5:
        showscore(player1, score1)
    
    else:
        showscore(player2, score2)

def autogame(player1, player2, score1, score2, fullmatch):
    
    import random 
    player_tuple = (player1, player2)
   
    if fullmatch == 'completo':
        
        while score1 != 5 and score2 != 5 :
            showscore(player1, score1)
            showscore(player2, score2)
            randomplayer = random.choice(player_tuple)
            print(f'Quien ha ganado el punto? {randomplayer}')
            score1, score2 = (whowon(player1, player2, score1, score2, randomplayer))
        
        if score1 == 5:
            showscore(player1, score1)
        
        else:
            showscore(player2, score2)
    
    else:
        while score1 != 5 and score2 != 5 :
            randomplayer = random.choice(player_tuple)
            score1, score2 = (whowon(player1, player2, score1, score2, randomplayer))
        
        if score1 == 5:
            showscore(player1, score1)
        
        else:
            showscore(player2, score2)



def main():
    
    print(' %%% VIRTUA TENNIS GAMMA %%% ' )
    mode = input("Ingrese MANUAL o SIMULACION según el modo en que desea utilizar el programa:\n").lower()

    while not mode or (mode.lower() != 'manual' and mode.lower() != 'simulacion'):
        mode = input('Ha ingresado un modo inválido, ingrese el modo de ejecución nuevamente ')
        continue
    
    player1 = input('Ingrese el nombre del primer jugador: ')
    while not player1:
        player1 = input('Ha ingresado un término inválido, ingrese el nombre nuevamente: ')
        
    player2 = input('Ingrese el nombre del segundo jugador: ')
    
    while not player2:
        player2 = input('Ha ingresado un término inválido, ingrese el nombre nuevamente: ')
    
    score1 = 0
    score2 = 0
    
    if mode.lower() == 'manual':
        manualgame(player1, player2, score1, score2)
        return
        
    else:
        fullmatch = input('Ingrese COMPLETO para ver el desglose del game o RESULTADO para ver solamente el ganador ')
        while not fullmatch or (fullmatch.lower() != 'completo' and fullmatch.lower() != 'resultado'):
            fullmatch = input('Ha ingresado un modo inválido, intente nuevamente: ')
            continue
        autogame(player1, player2, score1, score2, fullmatch)
        return
    
    
if __name__=='__main__':
    main()
              
            
        
                  
                  
            
                  
            
            
        
            
            
            
            
            
            
            
            
            
                 