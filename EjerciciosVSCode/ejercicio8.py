
dolares = 0
cordobas = 0 
a4 = 0 

while a4<1:
    print(" ")
    print("Bienvenido")
    print("Introduzca la cantidad de cordobas a convertir: ")
    cordobas = int(input("C$ "))

    dolares = cordobas / 36.75

    print("La cantidad de cordobas es C$",dolares)

    print(" ")
    print("¿Desea reintroducir el valor?")
    print("SI = 0 | NO = 1")
    a4 = int(input())
    print(" ")