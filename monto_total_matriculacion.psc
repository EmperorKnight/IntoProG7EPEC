Algoritmo monto_total_matriculacion
	Definir monto_total, matricula, pre_matricula, valor_semestre, a1, a2, a3, a4 Como Real
	Escribir 'Introduzca la cantidad a pagar por la prematrícula'
	Leer pre_matricula
	Escribir 'Introduzca la cantidad a pagar por la matrícula'
	Leer matricula
	Escribir '¿Conoce la cantidad total a pagar por todo el semestre?'
	Escribir 'SI = 1 | NO = 0'
	Leer a1
	Si a1=1 Entonces
		Escribir 'Introduzca la cantidad a pagar'
		Leer valor_semestre
		monto_total <- (pre_matricula+matricula)+(valor_semestre*0.25)
		Escribir 'El monto total a pagar para poder matricularse en una universidad es de: C$', monto_total
	SiNo
		Escribir 'Introduzca la cantidad a pagar por un mes del semestre'
		Leer a2
		Escribir 'Introduzca la cantidad de meses que conforman el semestre'
		Leer a3
		a4 <- a2*a3
		monto_total <- (pre_matricula+matricula)+(a4*0.25)
		Escribir 'El monto total a pagar para matricularse en la universidad es de: C$', monto_total
	FinSi
FinAlgoritmo
