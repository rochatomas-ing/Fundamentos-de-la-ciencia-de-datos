import math

def calcular_area_circulo(radio):
    return math.pi * (radio**2)

myradio = float(input("Ingrese el radio de su circulo: "))
print(calcular_area_circulo(myradio))