### Operadores de comparacion# -Expresiones que dan como resultado un valor Booleano# -Se pueden convertir tipos de valores #     ej int a float al hacer 1.0 + 1 ==2 **** (este caso se llama conversion IMPLICITA)#     casos de conversion EXPLICITA serian float(0) que pasa a ser 0.0, etc    # -Más conversion explicita: bool (0), (""), (0.0) son ejemplos de FALSE# - bool (1), ("x"), (0.01) son TRUE### Ejemplo de problema# def is_positive(number: float):#     answer = FALSE#     if (number > 0):#         answer = TRUE#     return answer# #Alternativa mas corta# def short_is_positive(number: float):#     return number > 0### Operadores lógicos de Python# and# or# not# ### Paradigmas de la programacion# -Fail fast, return early# Implica hacer múltiples pruebas al principio antes de ejecutar el código posta# ej: if not (condicion que quiero):#         return# Es bastante la posta# -Single entry, single exit# Implica una forma de programar con un unico punto de entrada y un único punto de salida (un solo return)# Es muy restrictivo# Genera mucha identacion# Prueba muchos errores encadenados# Es fácil determinar dónde sale la funcion    