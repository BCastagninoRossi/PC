# =============================================================================
# # -*- coding: utf-8 -*-
# =============================================================================


def virtuamatch (a: str, b: str)->str:
    '''Keeps score of a virtual tennis match game according to who wins the point
    
    inputs:
        - a : player1
        - b : player2
    
    print: a string containing the score or who won the game
    '''
    p1 = a.lower()
    p2 = b.lower()
    score1 = 0
    score2 = 0
    wingame = 'ha ganado el game'
    print(f'Score: \n-{a}: {score1} \n-{b}: {score2}')
    
    while score1 != 40 or score2 != 40:
        win = input('Quién ganó el punto?: ').lower()
        if win == p1:
            
            if score1 == 40:
                print(a, wingame)
                break
            
            elif score1 == 30:
                score1 = 40
                
            else:
                score1 += 15
                
        elif win == p2:
            
            if score2 == 40:
                print(b, wingame)
                break
            
            elif score2 == 30:
                score2 = 40
                
            else:
                score2 += 15
                
        else:
            print ('Nombre de jugador inválido')
            continue
        
        print(f'Score: \n-{a}: {score1} \n-{b}: {score2}')
    
    while score1 == 40 and score2 == 40:
        
        win = input('Quién ganó el punto?: ').lower()
        
        if win == p1:
            score1 = 'AD'
            
        elif win == p2:
            score2 = 'AD'
            
        else:
            print ('Nombre de jugador inválido')
            continue
            
        print(f'Score: \n-{a}: {score1} \n-{b}: {score2}')
        
    while score1 == 'AD' or score2 == 'AD':
        
        win = input('Quién ganó el punto?: ').lower()
    
        if win == p1 or win == p2:
            if score1 == 'AD' and win == p1:
                print(a, wingame)
                break
            
            elif score2 == 'AD' and win == p2:
                print (b, wingame)
                break
            
            else:
                score1 = 40
                score2 = 40
        else:
             print ('Nombre de jugador inválido')
             continue

            
        



def main():
    
    print(' %%% VIRTUA TENNIS GAMMA %%% ' )
    mode = input("Ingrese MANUAL o AUTOMATICO según el modo en que desea utilizar el programa:\n").lower()
    player1 = input('Ingrese el nombre del primer jugador: ')
    player2 = input('Ingrese el nombre del segundo jugador: ')
    virtuamatch(player1, player2)
   
   
    
if __name__=='__main__':
    main()
