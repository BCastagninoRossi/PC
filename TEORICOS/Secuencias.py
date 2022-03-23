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
- Se pueden sumar cadenas a cadenas, tuplas a tuplas o listas a listas

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
    
ID
    Es la identidad de la variable. La puedo obtener mediante la funcion ID
    Cuando modifico una tupla o una cadena, el ID cambia, cambia la variable.
    SIN EMBARGO cuando ya defini una lista, si la modifico si ID NO cambia
    Para evitar problemas, si yo sé que quiero una lista pero no voy a modificarla, debo usar TUPLAS. Es más eficiente y evita errores
    
    Formas de copiar una lista:
        - L = [1, 2, 3], L2 = L --> esto hace que L == L2 es true y *** L is L2 Tambien es True *** 
            el is nos dice que para python L y L2 SON LA MISMA LISTA, ENTONCES SI MODIFICO UNO SE MODIFICA EL OTRO!!!!!!
            L2 = L
            L2[1]= 100
            Ahora tanto L como L2 tendrán valor 100 en posicion 1 !!!! porque es como que hay 2 etiquetas (L y L2) para la MISMA VARIABLE
            
        - L3 = L [:] --> hace que L == L3 es true PERO L3 is L es False
        - L4 = L.copy() --> es otro modo de hacer lo mismo que el de arriba
    

SLICING
    Sirve para obtener más de un elemento de una lista/cadena/tupla
    Partiendo de cadenas obtengo cadenas, de listas obtengo listas y de tuplas, tuplas
    
    secuencia[int:int:int]
        |      |   |   |
        |      |   |   |
        *      |   |   |
    Puede ser una expresion
                |   |   |
                *   *   *
            desde hasta salto (pueden ser una expresion tambien)
            
    ej: def generar_lista(n:int) -> list:
        return list(range(n))
    
        expresion1 = generar_lista(100)[3, 100, 11]
        
    Otra forma es:
        lista [int1:int2] = L2
        Esto retorna L2 que es una nueva lista que incluye desde el indice int1 (incluyendolo) hasta el int2 (sin incluir)
        El SLICE nunca tira error. A lo sumo devuelve una lista vacía
        
DESEMPAQUETADO
    Puedo desempaquetar las secuencias, extrayendo sus valores
    ej:
        name = ('bruno', 'castagnino')
        nombre, apellido = name
        
    ej2:
        def minimax(secuencia):
            minimo = min(secuencia)
            maxino = max(secuencia)
            return minimo, maximo     *** esto por default devuelve una tupla pero si le agrego list.(minimo, maximo) o lo pongo entre [] devuelve una lista
    ej3 :
        def swap (a, b):
            temp = a
            a = b
            b = temp
            return a, b
    ej4 ITERACIONES:
        def probar_desempaquetado():
            meses = (('enero', 31), 
                 ('febrero', 28), 
                 ('diciembre', 31))
            for mes, dias in meses:
                print(mes, 'tiene ', dias, 'dias')
                
ENUMERADOS
    secuendia ---> enumerate() -----> secuencia(int, elemento, etc)
    ej:
        def probar_desempaquetado():
            docentes = ['pato', 'ernesto'] ---> VER POWER
            
            
FUNCIONES COMUNES

    largo: len()
    minimo y maximo: min(), max()
    contar ocurrencias: .count():
        "anana".count('a') -> 3
        [0, 0, 0, 1, 1, 0].count(0) -> 4
    
    *Conversion:
        - a cadenas: str()
        - a tuplas: tuple()
        - a listas: list()
        
    *Búsqueda:
        - .index()
        
FUNCIONES ESPECIFICAS A CIERTAS SECUENCIAS
    - Búsqueda en cadenas:
        .find() -> devuelve un int con el index de lo que quiero encontrar. SI NO LO ENCUENTRA DEVUELVE -1 (a diferencia de .index())
        
    - Casing en cadenas de texto:
        - .upper()
        - .lower()
        - .title() -> pone una mayuscula al inicio de cada palabra
        - .capitalize()
        - .casefold()
        - .swapcase()
        
        



























    
    
    
    