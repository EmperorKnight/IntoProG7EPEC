
monto_final=0
cantidad_producto=0
precio_unitario=0
descuento=0.1
a6 = 0 

while a6<1:
    print(" ")
    print(" ")
    print("Bienvenido")
    print("Introduzca la cantidad de productos")
    cantidad_producto=int(input("- "))

    print("Precio unitario de los productos")
    precio_unitario = int(input("C$ "))

    a2 = precio_unitario
    a3 = 1

    while a3 < cantidad_producto:
        precio_unitario = int(input("C$ "))
        a2 = a2 + precio_unitario
        a3 = a3+1

    monto_final = a2 * descuento

    print(" ")
    print("Recibo")
    print("Total a pagar C$ ", a2)
    print("Descuento del 10% aplicado C$ ", monto_final)
    
    print(" ")
    print("¿Desea reintroducir los valores?")
    print("SI = 0 | NO = 1")
    a6 = int(input())
    print(" ")