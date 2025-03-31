
dolares = 0
cordobas = 0 
a4 = 0 

while a4<1:
    print(" ")
    print("Bienvenido")
    print("Introduzca la cantidad de dolares a convertir: ")
    dolares = int(input("$ "))

    cordobas = dolares * 36.75

    print("Conversion completa C$",cordobas)

    print(" ")
    print("¿Desea reintroducir el valor?")
    print("SI = 0 | NO = 1")
    a4 = int(input())
    print(" ")