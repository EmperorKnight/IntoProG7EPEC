Algoritmo ejercicio_10
	Definir a1, a3, a2, monto_final, cantidad_producto, precio_unitario, descuento Como Real
	
	descuento = 0.1
	
	Escribir 'Introduzca la cantidad de producto: '
	Leer cantidad_producto
	
	Escribir 'Precio unitario de los productos: '
	Leer precio_unitario
	
	a3=1
	a2=precio_unitario
	
	Repetir
		Leer precio_unitario
		a2 <- a2+precio_unitario
		a3 <- a3+1
	Hasta Que a3=cantidad_producto
	
	monto_final = a2 * descuento
	
	escribir "************************************************************************"
	escribir "Recibo"
	escribir "Total a pagar:" a2
	escribir "Descuento del 10% aplicado: C$" monto_final
	escribir "************************************************************************"
	
FinAlgoritmo
