a4 = 0
while a4 < 1:
    
    print("Introduzca la división")
    a1 = int(input("-> "))
    a2 = int(input("-> "))

    a4 = a1//a2
    a3 = a1 % a2

    print(a3)
    print(a4)

    print(" ")
    print("¿Desea reintroducir los valores?")
    print("SI = 0 | NO >= 1")
    a4 = int(input("-> "))
    print(" ")