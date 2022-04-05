# -*- coding: utf-8 -*-
### PROGRAMACION DEFENSIVA
    
Escribir especificaciones
Validar condiciones
Modularizar programas
'No es que el códico no falla, si no que se degrada con gracia...cae con estilo'

Es distinta que la programacion *segura* que se relaciona con la seguridad informática

Cuando fallan lo hacen de manera segura (Realiza una limpieza antes de cerrarse - ej cerrar la sesion del homebanking cuando crashea un navegador web -)
Fallan de forma clara: explican claramente cual fue el error (Ya sea para el desarrollador o para el usuario)

##TESTING Y VALIDACION
TESTING

*Anticipación - preparar todo para hacer test y debug 

Disenar código en módulos que se puedan probar individualmente
Documentar restricciones en cada módulo (que se espera de cada entrada, qe se espera de cada salida)
Documentar suposiciones realizadas al Disenar el código

*Disenar Pruebas
Cuando se disenan primero las pruebas y luego el software que puede pasarlas se denomina Test Driven Development
Muchas veces primero se disena la solucion y luego las pruebas
En cualquier caso, se define un conjunto de **resultados esperados**
    Típicamente pensamos un conjunto de entradas y cada ubna de ellas debe tener una salida

*Cuándo hacemos pruebas?
-Tenemos el conjunto de resultados esperados

*Tipos de pruebas
    -Tests unitarios:
        Validan cada pieza del programa
        Prueban cada funcion de manera indepoendiente
        Pueden haber multiples test unitarios para cada funicion
    -Tests Regresivos
    
*Aproximacion al diseno de pruebas
-Intuicion
-Pruebas aleatorias - cuando no hay particion evidente
-Black box testing - probar todos los caminos/formas mirando las especificaciones
-Glass box testing - probar todos los caminos/formas mirando el codigo fuente

En el black box testing alcanza con leer las especificaciones de una funcion o propgrama con las entradas y salidas esperadas. 
Las pruebas se disenan sin mirar el código
Mejor si las hace alguien que no haya escrito el codigo
Las pruebas se pueden reutilizar en caso de que el codigo cambie
Avanza por los caminos de la particion


En el glass box testing miramos el código para disenar las pruebas
se dice que es de camino completo (path-complete) si recorre todas las posibles ramas del código
Test/Code Coverage es la idea de cuantas líneas del total ejecuta la prueba. Si las cubre todas es Coverage 100% o PATH-complete
Contras:
    Puede pasar por ciclos cualquier cantidad de veces
    Un coverage del 100% puede no encontrar un bug
    
        

##DEBUGGING
Se buscan eliminar todos los bugs del programa
    Nunca sabemos 
    
Distintas herramientas
-python debugger (el de spyder)
-python tutor
-meter print, print, print

Requiere ser sistemático y pensar mucho donde buscar

##Pasos en el debugging
ver ppt
Meter print s en todos lados ES la manera de probar hipótesis
Cuando ponemos el print?
Antes de ingresar a una funcion (lo que le pasamos)
Al ingresar a una funicon (lo que recibe)
Al terminar de ejecutar una funcion (lo que retorna)
Al salir de la funcion(lo que recibimos)
Si no tenemos idea de la ubicacion de un bug: usar biseccion (poner print en la mitad del código y ejecutar, repetir en funcion de los valores impresos)
    Hay una funcion de github que permite esto automaticamente

###Errores
XxxxxError(los faciles):
    IndexError
    TypeError
    etc

Errores de lógica(los dificiles):
    mejor evitarlos que solucionarlos
    Pensar mucho antes de escribir código
    Trata de explicarle el diseno a otra persona, a un patito de goma
    *The pragmatic programmer* libro interesante
    
Donny Don't!
    NO escribir todo el programa sin parar
    NO probar tooodo el programa
    NO hacer debugging todo junto
    
MELD: app que sirve para comparar 2 archivos (versiones distintas) uno al lado del otro, comparar y cambiar entre ellos

###EXEPCIONES








