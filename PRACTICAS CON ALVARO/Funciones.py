# -*- coding: utf-8 -*-

# print("Bienvenido, Bruno")

# miles = float(input("Ingrese las millas a convertir "))

# def convert_miles_to_km (miles:float)->float:
#     '''
#     Convierte millas a km
#     '''
#     kilometers = miles / 0.621
#     print("La conversion resulta: ", kilometers, "km")
    
# print(convert_miles_to_km(miles))
    
###

# Una buena práctica es definir una función main al principio de nuestro archivo de código. Simplemente iniciar a codear con 
# def main():
#     Y meter toooooodo el código acá adentro.
#     y al final de todo siempre hay que poner al final de toooodo:

# if __name__=='__main__':
#     main()


###
# Además convertir a pesos ARS y francos suizos CHF. Y elegír entre Scw y el resto y ver a que se Convierte

# def main():
    
#     dollars = float(input("Ingrese USD: "))
#     coin = input("Ingrese moneda a la que desea realizar la conversión (CHF, ARS, CNY): ")
    
#     def usd_to_coin (dollars, coin):
#         lower_coin = coin.lower()
#         if (lower_coin == 'ars'):
#             conversion = dollars * 200
#             print(f"{conversion:.2f} ARS")
#             if (lower_coin == 'chf'):
#                 conversion = dollars * 0.94
#                 print(f"{conversion:.2f} CHF")
    
#         if (lower_coin == 'cny'):
#             conversion = dollars * 6.75
#             print(f"{conversion:.2f} CNY")

#     usd_to_coin(dollars, coin)
        
# if __name__=='__main__':
#     main()

### 

# def main ():
    
#     month = int(input('Ingrese el més del año cuyo cuarto desea conocer '))
#     def quarter_of_year(month):
#         if (1 <= month <= 3):
#             print(f'El mes {month} pertenece al primer cuarto del año' )
#         elif (4 <= month <= 6):
#              print(f'El mes {month} pertenece al segundo cuarto del año' )
#         elif (7 <= month <= 9):
#              print(f'El mes {month} pertenece al tercer cuarto del año' )
#         elif (10 <= month <= 12):
#              print(f'El mes {month} pertenece al cuarto cuarto del año' )
#         else:
#             print(" Ingresó un número de mes inválido")
                  
#     quarter_of_year(month)
    
# if __name__=='__main__':
#     main()

### CICLOS CON FOR

def generateRange(min: int, max: int, step: int) ->None:
    minimum = int (min)
    maximum = int (max)
    escalon = int(step)
    for i in range (minimum, maximum+1, escalon):
        print (i)

### CICLOS CON WHILE
        
def generateRange_While(min: int, max: int, step: int) ->None:
    minimum = int (min)
    maximum = int (max)
    escalon = int (step)
    while minimum <= maximum:
        print (minimum)
        minimum += escalon
    

def main():
    
    generateRange_While(1, 35, 1)
    
if __name__=='__main__':
    main()

