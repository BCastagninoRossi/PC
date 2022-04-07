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

###EXEPCIONES-> son errores en la ejecucion

Es lo queocurre cuando la ejecucion llega a una CONDICION INESPERADA
-IndexError: intentamos acceder a una secuencia mas alla de sus elementos
-VER POWER QUE FALTAN VARIOSS

Que hacemos con las exepciones?
-Fallar silenciosamente(en realidad se puede con cualquier error, no solo exepciones):
    *Remplazar los valores que fallaron por valores por omision o simplemente continuar
    *No esta bueno! porque el usuario no se entera y los errores NUNCA DEBERIAN PASAR silenciosamente
-Retornar un valor que indique ERROR:
    *Qué valor elegimos? -1? a veces retornar -1 permitiria continuar el programa...
    *No es una mala manera de operar pero hay que pensar mucho en el valor...
-Parar la ejecucion y Senalar la condicion que fallo:
    *LANZAR EXEPCIONES para controlar el flujo de la ejecucion
    *No se retornan valores especiales
    *Se lanza una exepcion cuando no podemos producir un resultado consistente con la especificacion de la funcion:
        raise nombredelaexepcion('descripcion')
    *Ej: def sqrt(x, eps):
            if x<0:
                raise ValueError('x no puede ser menor a 0')
    
    *Python nos permite 'atrapar' las exepciones:
        try: 
            <instrucciones>
        except:
            <instrucciones>
            
        Exepciones que saltan del try son atrapadas por el exept
        Ej: print('Vamos a dividir x por y')
            try: 
                x = int(input('Ingrese el valor de x:'))
                y = int(input('Ingrese el valor de y: '))
                print (x/y)
            except:
                print('Algo no salio bien, revise los inputs')
                
        
        

- Manejo de EXEPCIONES ESPECIFICAS:
    *Ej:print('Vamos a dividir x por y')
        try: 
            x = int(input('Ingrese el valor de x:'))
            y = int(input('Ingrese el valor de y: '))
            print (x/y)
        except ValueError:
            print('La entrada no se pudo convertir a entero')
        except ZeroDivisionError:
            print('No se puede dividir por cero')
        except:
            print('No se que pasó')
        
- Manejo de exepciones - COMPLETA:
    try:
        <Body> aca tienen que estar las cosas que puedan tirar error, hay que tratar de mantenerlo lo mas reducido posible
    except ValueError as <nombre>:
        <excepcion>
    except KeyboardInterrupt as <nombre>:
        <excepcion>
        tipo:
            raise exepcion('lo que sea la excepcion')
    else:
        Esto solo se ejecuta si el try se ejecuta correctamente sin excepciones
    finally:
        Se ejecuta SIEMPRE, aunque el try haya fallado, incluso si se ejecuto un break, continue o return
    
ES IMPORTANTE SABER que aquello que quede escrito fuera de las excepciones se va a ejecutar igual!!! (o a intentar ejecutar)
Por esto la idea es tener todos los bloques dentro de try y except s
o.....

Como los try y except tienen alto costo de procesamiento

###VALIDACIONES

-Validar precondiciones - nada, falla
* Ver PPT

- ASSERTIONS:
    buen ejemplo de programacion defensiva
    puede simplificar encontrar bugs apenas ingresados
    es como lanzar una exepcion y que el usuario ingrese datos incorrectos
    Se usan para:
        comprobar tipos de argumentos o valores
        comprobar que los invariantes de los datos se cumplan
        comprobar restricciones de valores de retorno
        coprobar que no se violen requerimientos de las funciones o programas
    el assert CORTA la ejecucion de lo que sigue
    
    ej:
        def average (grades):
            assert len(grades) != 0, 'NO GRADES DATA'
            return sum(grades) / len(grades)
        
        
    Se pueden usar durante el DESARROLLO del codigo pero a la hora de meterlo en produccion SE PUEDE DESACTIVAR para mejorar el desempeño

-Validar entradas de usuario - ver PPT

            
        




