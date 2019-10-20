print("SUMA DE IMPARES EN UN RANGO DADO")

def rango1():      #funcion para el rango si en caso el usuario elije solo uno
	d1 = int(input("Inicio de rango: "))
	d2 = int(input("Fin de rango:    "))
	a = 0

	for i in range(d1,d2+1):
		if i%2 != 0:  #este if verifica si el numero en i en el rango, es par o impar, osea divisible o no entre 2
			a = a+i   #variable que va guardando cada numero impar del rango
	print("Suma de impares: ",a)  #se imprime la variable a, con el dato final osea la suma de todos los impares que fue guardando


def rango1y2():
	a = 0 #variable a que me ira guardando los impares del rango 1
	b = 0 #variable b que me ira guardando los impares del rango 2

	#AQUI SE PIDEN LOS RANGOS, DESDE EL PRIMER DATO AL ULTIMO DATO DE ESTOS SEGUN ELIJA EL USUARIO
	d1 = int(input("Inicio de rango 1: "))
	d2 = int(input("Fin de rango 1:    "))
	d3 = int(input("Inicio de rango 2: "))
	d4 = int(input("Fin de rango 2:    "))

	for i in range(d1,d2+1):  #for que verifica los datos del rango 1
		if i%2 != 0:
			a = a+i
	print("Caso 1: ",a) #aqui se imprime sa suma de los impares del rango 1

	for i in range(d3,d4+1): #for que verifica los datos del rango 2
		if i%2 != 0:
			b = b+i  
	print("Caso 2: ",b) #aqui se imprime la suma de los impares del rango 2


cp = int(input("Ingrese el numero de casos de prueba (Maximo 2) "))
while cp > 0:  #mientras la opcion sea mayor a 0 sino, el programa acabara

	if cp == 1:  
		rango1()  #si la opcion es 1 llamo a la funcion del rango 1
		cp = int(input("Ingrese el numero de casos de prueba (Maximo 2) "))
	
	elif cp == 2:
		rango1y2() # si es dos llamo a la funcion donde esta el rango 1 y 2 
		cp = int(input("Ingrese el numero de casos de prueba (Maximo 2) "))

	elif cp >2:
		print("MAXIMO 2 CASOS!")
		cp = int(input("Ingrese el numero de casos de prueba (Maximo 2) "))
	else:
		break

