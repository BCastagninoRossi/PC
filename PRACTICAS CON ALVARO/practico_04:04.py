# -*- coding: utf-8 -*-

'''
Write a function that takes a list and returns the list in reverse order
'''


def reverse_list (lista: list)->list:
    new_list=[]
    for i in range(len(lista)-1, -1, -1):
       new_list.append(lista[i])
    return new_list


def reverse_optimized(one_list: list)-> list:
    '''Misma funcion pero estoy optimizando memoria, al mantener una sola lista y no 2 listas enteras con valores invertidos'''
    left = 0
    right = len(one_list)-1
    while left < right:
        aux = one_list[right]
        one_list[right] = one_list[left]
        one_list[left] = aux
        left += 1
        right-=1
    return one_list

# def rps(player1: str, player2: str)-> str:
#     '''plays rock, paper, scissors and returns winner or draw'''
#     possibilities = ['rock', 'paper', 'scissors']
#     rounds = 3
#     while True: etc
        
        
            

def main():
    pass


if __name__=='__main__':
    main()