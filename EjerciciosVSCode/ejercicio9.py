
a1 = 0
a2 = 0 
a3 = 0
a4 = 0 
a5 = 0
promedio_total = 0
a6 = 0 

while a6<1:
    print(" ")
    print("Bienvenido")
    print("Introduzca el promedio de 5 asignaturas del estudiante: ")
    a1 = int(input("1) "))
    a2 = int(input("2) "))
    a3 = int(input("3) "))
    a4 = int(input("4) "))
    a5 = int(input("5) "))

    promedio_total = int((a1+a2+a3+a4+a5)/5)

    print("El promedio total del estudiante es:",promedio_total)

    print(" ")
    print("¿Desea reintroducir los valores?")
    print("SI = 0 | NO = 1")
    a6 = int(input())
    print(" ")