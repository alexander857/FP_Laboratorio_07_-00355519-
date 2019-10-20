#include <iostream>
using namespace std;

int main(){
	int inicio, final, num;
	bool primo;
	cout<<"NUMEROS PRIMOS EN UN RANGO DADO"<<endl;
	cout<<"Ingrese el inicio del rango: ";cin>>inicio;
	cout<<"Ingrese el final del rango: ";cin>>final;
	cout<<"LOS NUMEROS PRIMOS EN ESE RANGO SON LOS SIGUIENTES: "<<endl;
	
	for(int i=2;i<=final;i++){
		num=2;
		primo = true;
		
		while(primo==true && num < i){
			if (i%num==0){
				primo= false;
			}
			else{
				num += 1;
			}
			
		}
		if (primo==true){
			cout<<i<<endl;
		}
	}
	
	
	
	return 0;
}
