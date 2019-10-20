print("COMPARANDO NUMEROS")

def uncaso():    #funcion para comparar un par de numeros
	n1 = int(input("Ingrese el primer numero: "))   #se pide al usuario que ingrese el par de numeros
	n2 = int(input("Ingrese el segundo numero: "))

	if n1 > n2:    #en esta condicion se compara si los numeros imgresados son iguales, o uno es mayor o menor que le otro
		print(n1," es mayor que ",n2) 
	elif n1 < n2:
		print(n1," es menor que ",n2)
	elif n1 == n2:
		print(n1," es igual a ",n2)

def doscasos(): #funcion para comparar dos pares de numeros ingresados
	
		n1 = int(input("Ingrese el primer numero: "))
		n2 = int(input("Ingrese el segundo numero: "))
		m1 = int(input("Ingrese el primer numero: "))
		m2 = int(input("Ingrese el segundo numero: "))

		if n1 > n2:
			print(n1," es mayor que ",n2)
		elif n1 < n2:
			print(n1," es menor que ",n2)
		elif n1 == n2:
			print(n1," es igual a ",n2)		

		if m1 > m2:
			print(m1," es mayor que ",m2)
		elif m1 < m2:
			print(m1," es menor que ",m2)
		elif m1 == m2:
			print(m1," es igual a ",m2)

def trescasos(): #funcion para comparar tres pares de numeros ingresados
		n1 = int(input("Ingrese el primer numero: "))
		n2 = int(input("Ingrese el segundo numero: "))
		m1 = int(input("Ingrese el primer numero: "))
		m2 = int(input("Ingrese el segundo numero: "))
		p1 = int(input("Ingrese el primer numero: "))
		p2 = int(input("Ingrese el segundo numero: "))

		if n1 > n2:
			print(n1," es mayor que ",n2)
		elif n1 < n2:
			print(n1," es menor que ",n2)
		elif n1 == n2:
			print(n1," es igual a ",n2)		

		if m1 > m2:
			print(m1," es mayor que ",m2)
		elif m1 < m2:
			print(m1," es menor que ",m2)
		elif m1 == m2:
			print(m1," es igual a ",m2)

		if p1 > p2:
			print(p1," es mayor que ",p2)
		elif p1 < p2:
			print(p1," es menor que ",p2)
		elif p1 == p2:
			print(p1," es igual a ",p2)

a = int(input("Ingrese el numero de casos a evaluar (maximo 3) "))
while a >0:   #mientras el usuario solo elija maximo 3 pares de numeros  a comparar

	if a == 1:
		uncaso()  #llamamos a la funcion de un solo par de numeros si el usuario ingresa 1
		a = int(input("Ingrese el numero de casos a evaluar (maximo 3) "))
		
	elif a == 2:
		doscasos() #si ingresa dos, se llama a la funcion de dos pares de numeros a comparar
		a = int(input("Ingrese el numero de casos a evaluar (maximo 3) "))
		
	elif a == 3:
		trescasos() #y si es 3 la opcion, se llama a la funcion que compara 3 pares de numeros
		a = int(input("Ingrese el numero de casos a evaluar (maximo 3) "))
		
	elif a > 3:
		print("MAXIMO 3 CASOS!")
		a = int(input("Ingrese el numero de casos a evaluar (maximo 3) "))


