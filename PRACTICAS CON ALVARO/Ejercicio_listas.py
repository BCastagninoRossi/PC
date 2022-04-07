#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 12:39:28 2022

@author: brunocr
"""


'''Define a function that removes from a given array of 
integers all the values contained in a second array'''

def popper (father_array: list, popper: list)->list:
    res=[]
    for i, c in enumerate(father_array): #Tengo i y c porque enumerate devuelve una lista de tuplas con el index (i) y el value(c)
        if c not in popper:
            res.append(father_array[i])
    return res


def popper2 (father_array: list, popper: list)->list:
    res=[]
    for value in father_array:
        if value not in popper:
            res.append(value)
    return res

def popper3 (father_array: list, popper: list)->list:
    res=father_array[:] #clave esta forma de copiar la lista para que no se piren los IDs
    for value in father_array:
        for plop in popper:
            if value == plop:
                res.remove(value)
    return res