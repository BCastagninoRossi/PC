# -*- coding: utf-8 -*-

##### Secuencias
Tupla = (1, 2, 3)
List = [1, 2, 3]
String = '1, 2, 3' # Los strings, como las tuplas son inmutables

## INDEXING - Buscar la posición de un valor en una secuencia
a = List[2]
b = Tupla[2]
c = String[2]

## Acceder al ultimo elemento de list
List[2] = List[len(List)-1] = List[-1]

## SLICING
other_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sliced_list = other_list[:5]
sliced_list_2 = other_list[1:8:2] # Esto me slicea del index 1 al 8 sin inclujir a este último y con un step de 2

## METHODS - Son funciones asociadas al tipo de dato (list, str, etc)
para strings: .split