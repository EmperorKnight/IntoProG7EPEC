
a1 = 0
antecesor = 0
sucesor = 0
a4 = 0 

while a4<1:
    print(" ")
    print("Bienvenido")
    print("Introduzca un numero entero: ")
    a1 = int(input())

    antecesor = a1-1
    sucesor = a1 + 1

    print("El antecesor de",a1,"es",antecesor)
    print("El sucesor de",a1,"es",sucesor)

    print(" ")
    print("¿Desea reintroducir el valor?")
    print("SI = 0 | NO = 1")
    a4 = int(input())
    print(" ")
