print("INGRESA EL RANGO DESEADO")
inicio = int(input("Ingresa el numero inicial de tu rango: ")) #se piden los limites del rango de donde se mostraran los primos
final = int(input("Ingresa el numerofinal de tu rango: "))
print("LOS PRIMOS EN EL RANGO INGRESADO SON LOS SIGUIENTES: ")
for i in range (2, final+1): #el rango en i empieza desde dos ya si se empieza de 1, el programa dira que el 1 es primo lo cual no lo es.
	num = 2 #se crea una variable la cual va ir tomando los valores de i, desde donde empieza el rango hasta donde termina, empezando por el 2, luego el 3 y 
	         #asi hasta que llegue al ultimo valor de i, ya que cada valor de i se va ir dividiendo entre el valor de num para comprobar si el numero de i es
	         #primo o no. Ejemplo 2 (que es el primer valor de i)/2(que es el primer valor de num) y luego 2/3, 2/4 etc hasta llegar al ultimo valor del rango
	primo = True #esta variable se inicializa en True de que todos los numeros son primos, hasta que se muestre que alguno no lo sea

	while primo and num < i: #este ciclo while se seguira ejecutando miestras los numeros del rango sean primos, y la variable num sea menor al ultimo valor
	                         #que toma i
		if i % num == 0:  #condicion donde se verifica si el numero es primo o no
			primo = False  #si el cociente de i/num es exacta significa que el numero no es primo entonce la variable primo cambia su estado a False
		else:           
			num += 1    #si no se haya ninguna division exacta, la varibale num va a crecer en 1 y va comenzar nuevamente el bucle a verificar si el 
			            #siguiente numero es primo o no y si en caso tampoco hay una division exacta num seguira creciendo en 1 hasta llegar a ser igual al 
			             #ultimo valor del rango

	if primo:   
		print(i)  #si el rango termina, los numeros de los cuales no se encontro division exacta se imprimiran en pantalla, que seran los numeros primos
		          #en el rango ingresado ya que solo tienen division exacta entre ellos mismos y la unidad