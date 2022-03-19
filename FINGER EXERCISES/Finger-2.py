# -*- coding: utf-8 -*-

### Finger exercise 2 - Hace unos meses compramos un volumen de 12095.2 items a 0.86 GRO la unidad, pidiendo prestado para la
# compra. Hoy, esos items valen 1.28 GRO la unidad.
# Escribir una función que indique mi ganancia neta si vendo todos mis items (el valor debe ser devuelto, no
# impreso). Necesito comprar un libro que cuesta 2831.97 GRO. Implementar una función que determine cuál
# es el volumen de items que debo vender para comprar el libro y a su vez devolver los GRO que me
# prestaron para comprar esa cantidad. Dicho de otro modo, cada item comprado me da una ganancia neta
# de 1.28 GRO - 0.86 GRO ¿cuántos items debo vender para poder comprar el libro a partir de las ganancias?

def total_gain(volume: float, initial_price: float, final_price: float, target_gain: float)->float:
    '''
    Funcion que calcula ganancias netas pueden ser obtenidas luego de compra y venta de un stock de items, asi como tambien cuántos items deben ser comprados y vendidos para conseguir una ganancia neta específica
    
    PARAMETROS:
        -volume: es el número de items que tengo actalmente en stock
        -initial_price: es el precio inicial que fue pagado por cada uno de los items en stock
        -final_price: es el precio de venta de cada uno de los items en stock
        -target_gain: es la ganancia objetivo que deseo obtener mediante la compraventa de un determinado stock de los items previaamente mencionados
        
    RETURN:
        ganancia_neta (la ganancia neta obtenida de la venta de todo mi stock actual), needed_volume (el n;umero de items que deberia compravender para llegar a target_gain)
    '''
    item_margin = final_price - initial_price
    ganancia_neta = item_margin * volume
    needed_volume = target_gain / item_margin
    return (ganancia_neta, needed_volume)


print(total_gain(12095.2, 0.86, 1.28, 2831.97))

 



