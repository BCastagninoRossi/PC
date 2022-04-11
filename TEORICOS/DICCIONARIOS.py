# -*- coding: utf-8 -*-
Hasta ahora teniamos info tipo

names = ('aardonyx', 'triceratops')
diet = ('hervivorous', 'carnivorous')

problemas:
    necesitamos listas con mismos numeros de indices, ordenadas, etc
    la info se deberia rescatar con funciones del tipo:
        def get_diet(dinosaur, names, diet, species):
            i = names.index(dinosaur)
            return diets[i]
        
Todo tiene que estar ordenado, cuando se actualiza una lista hay que actualizar todas, desprolijo, etc
Cuando necesitamos muchas secuencias de informacion vinculada:
    DICCIONARIOS
    
***** Diccionarios *****:
    
    Conjunto de pares (clave:valor)
    En una secuencia teniamos (index:Value)
    Acá tenemos una clave ÚNICA vinculada a un valor
    No estan ordenados
    
    ***Se definen con {}
    o se pueden transformar otras cosas en diccionarios con dict()
    
    Ejemplo:
        
        dinosaurs{
            "aardonyx" : ('Herviborous', 'celestae')
            "abelisaurus" : ("Carnivorous", "comahuensis") 
            }
        
        ACCEDO MEDIANTE:
        dictionary[key]
        Ej:
        dinosaurs['aardonyx']
        Acceder a un elemento en un diccionario conlleva una complejidad de O=1
        
        Entonces podría buscar la dieta con
        def get_diet(dinosaur, dinosaurs):
            return dinosaurs[dinosaur][0]

    También podriamos guardar la informacion en diccionarios en diccionarios:
        dinosaurs = {
            "aardonyx" : {"diet": "herviborous", "species": "celestae"}
            "abelisaurur" : {"diet": "carnivorous", "species": "comahuensis"}
            }
        Es mas facil de llamar ahora
        dinosaurs["aardonyx"]["diet"]
        
        
        
    PARA AGREGAR un elemento al diccionario:
        dinosaurs['nuevodino'] = {"diet": "herviborous", "species": "celestae"}
    
    PARA BORRAR una clave:
        del(dinosaurs["key"])
    
    OPERACIONES:
        Para obtener claves y valores:
            
            - dictionary.keys(): sobre esto puedo iterar o printear o generar una lista de keys
            - dictionary.values()
            - dictionary.items()
            - dictionary.get() --> permite tomar un valor que no esta en el diccionario si la clave no existe:
                Ej:
                    contadores = {
                        'dino1': 'trex'
                        }
                    contadores.get('velociraptor', 'no hay ese dino')
                    ESTO Va a devolver que no hay ese dino
        
            
        
        
        
        