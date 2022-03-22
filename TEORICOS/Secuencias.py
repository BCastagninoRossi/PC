# -*- coding: utf-8 -*-

TUPLAS

Como las cadenas (strings) son secuencias ordenadas de elementos que son INMUTABLES

Diferencias con cadenas:
    - No es necesario que cada elemento sea un caracter
    - Cada elemento puede ser de cualquier tipo (int, float, str, etc)
    - No es necesario que todos los elementos sean del mismo tipo
    
Hay que encerrar entre paréntesis una lista de elementos separados con comas (hasta si es un solo elemento le tengo que poner una coma)
ex:
    tupla1 = (0, "hola", false, list, etc)

LISTAS

Mismo concepto que las tuplas pero son MUTABLES (Puedo acceder y obtener un elemento pero TAMBIEN MODIFICARLO)
- Se definen entre corchetes []

SECUENCIAS
son las CADENAS, TUPLAS y LISTAS

- Soportan operaciones comunes
- Se puede ITERAR SOBRE ELLAS
- Se pueden obtener los elementos directamente

ejemplos:
    
    Cadenas: s = 'hola'
    type(s) -> str
    s+ str -> str
    s * int -> str
    
    def contar_letras (cadena: str, letra: str)->int:
        '''cuenta la cantidad de letras específicas en la cadena
        
        Argumentos:
            cadena (str) -- cadena sobre la que contar
            letra(str) -- letra que quiro contar
        '''
        cuenta = 0
        for caracter in cadena:
            if caracter == letra:
                cuenta +=1
                
        return cuenta
    
    def contar_elementos(lista: list, ele)-> int:
        '''cuenta la cantidad de un elemento específico que hay en una lista
        
        Arguentos:
            lista (list) -- la lista
            ele -- elemento a contar
        '''
        cuenta = 0
        for e in lista:
            if e == ele:
                cuenta +=1
        return cuenta
    
    
INDEXING
    Obtiene un elemento de una posicion dada por un int
    - para cadenas obtiene cadenas
    - para tuplas y listas, obtiene el tipo de elemento accedido
    
        ex: string[int], tupla[int], list[int]
        
        - 'secuencia' es el nombre del string, list o tupla
        - [int] voy a poner la posicion del elemento que desee acceder, CONTANDO DESDE EL 0, puede ser POSITIVO o NEGATIVO
        - ejemplo:
            
            
    - En una lista, esto me permite modificar un elemento, por ejemplo list[1]= 'hola'
    estoy modificando el elemento 1 de la lista por 'hola'
    

SLICING
            
    
    
    
    
    
    