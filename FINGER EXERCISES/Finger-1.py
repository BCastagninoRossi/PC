# -*- coding: utf-8 -*-

### Finger 1 --- Se pide construir una función que calcule la duración del partido medida en segundos. La función tomará
### como parámetros la cantidad de horas, minutos y segundos.

def match_duration(hours, minutes, seconds):
    hour_seconds = hours * 3600
    minute_seconds = minutes * 60
    total_seconds = hour_seconds + minute_seconds + seconds
    return total_seconds

print("El partido de tenis tuvo una duración de ", match_duration(11, 6, 23), " segundos")