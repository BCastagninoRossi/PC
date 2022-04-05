# # -*- coding: utf-8 -*-

# ##Funciones .join, reverse(), .split

# cadena = '2022-02-01'
# '/'.join(reversed(cadena))

# ####

# cadena = '''Esta es la docuumentacion
# de una funciín
# que tiene muchas lineas'''

# cadena.split('\n')

#### FUNCIONES DE LISTAS

#.append()
#.split()
#.remove()
#.index()
#.pop()
#.insert()


users = 'pato felipe juan pedro bruno'
users_split = users.split() # Por default usa los espacios como puntos para splitear y genera una lista
print (users_split)

users_split.remove('bruno') # elimina el elemento
print (users)

print(users_split.pop(0))

users_split.append('bruno2')
print(users_split)

##### IMPORT y OTRAS (Clave, llegue mediahora tarde)
##### ALGORITMOS DE BUSQUEDA (SE ME CAGO EL CARGADOR)
