#include <iostream>
using namespace std;

int rango(){
	int inicio, final, a;
	a = 0;
	cout<<"Inicio del rango: ";cin>>inicio;
	cout<<"Final del rango: ";cin>>final;
	
	for(int i=inicio; i<=final; i++){
		if(i%2!=0){
			a += i;		
		}		
	}
	cout<<"Suma de impares en el rango ingresado: "<<a<<endl;		
}

int dosrangos(){
	int in1, fin1, in2, fin2, a, b;
	a = 0;
	b = 0;
	cout<<"Inicio del rango 1: ";cin>>in1;
	cout<<"Final del rango 1: ";cin>>fin1;
	cout<<"Inicio del rango 2: ";cin>>in2;
	cout<<"Final del rango 2: ";cin>>fin2;
	
	for(int i=in1; i<=fin1; i++){
		if(i%2!=0){
			a += i;		
		}		
	}
	cout<<"Caso 1: "<<a<<endl;
	
	for(int i=in2; i<=fin2; i++){
		if(i%2!=0){
			b += i;		
		}		
	}
	cout<<"Caso 2: "<<b<<endl;	
	
}

int main(){
	int r;
	cout<<"SUMA DE IMPARES EN UN RANGO INGRESADO"<<endl;
	cout<<"Ingrese el numero de rangos a evaluar (maximo 2): ";cin>>r;
	while (r>0){
		
		if(r==1){
			rango();
			cout<<"Ingrese el numero de rangos a evaluar (maximo 2): ";cin>>r;
		}
		else if(r==2){
			dosrangos();
			cout<<"Ingrese el numero de rangos a evaluar (maximo 2): ";cin>>r;
		}
		else if (r>2){
			cout<<"MAXIMO 2 RANGOS"<<endl;
			cout<<"Ingrese el numero de rangos a evaluar (maximo 2): ";cin>>r;
		}
		else{
			break;
		}			    		
	}				
	return 0;
}
