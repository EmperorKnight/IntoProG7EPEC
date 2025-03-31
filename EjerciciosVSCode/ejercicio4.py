
a1 = 0
a2 = 0
a3 = 0
a4 = 0 

while a4<1:
    print(" ")
    print("Bienvenido")
    print("Introduzca un numero entero: ")
    a1 = int(input("- "))

    print("Introduzca otro numero entero: ")
    a2 = int(input("- "))

    a3 = a1/a2

    print("El resultado de la suma es:", a3)

    print(" ")
    print("¿Desea reintroducir los valores?")
    print("SI = 0 | NO = 1")
    a4 = int(input())
    print(" ")