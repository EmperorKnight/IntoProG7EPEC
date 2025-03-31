
import math
radio = 0
area = 0 
a4 = 0 

while a4<1:
    print(" ")
    print("Bienvenido")
    print("Introduzca el radio del circulo: ")
    radio = int(input())

    area= math.pi * (radio**2)

    print("El area del circulo es:",area)

    print(" ")
    print("¿Desea reintroducir el valor?")
    print("SI = 0 | NO = 1")
    a4 = int(input())
    print(" ")