#include <iostream>
using namespace std;

int uncaso(){
	int n1, n2;
	cout<<"Ingrese el primer numero: ";cin>>n1;
	cout<<"Ingrese el segundo numero: ";cin>>n2;
	
	if(n1>n2){
		cout<<n1<<" es mayor que "<<n2<<endl;
	}
	else if(n1<n2){
		cout<<n1<<" es menor que "<<n2<<endl;
	}
	else if(n1==n2){
		cout<<n1<<" es igual a "<<n2<<endl;
	}	
}

int doscasos(){
	int n1, n2, m1, m2;
	cout<<"Ingrese el primer numero: ";cin>>n1;
	cout<<"Ingrese el segundo numero: ";cin>>n2;
	cout<<"Ingrese el primer numero: ";cin>>m1;
	cout<<"Ingrese el segundo numero: ";cin>>m2;
	
	if(n1>n2){
		cout<<n1<<" es mayor que "<<n2<<endl;
	}
	else if(n1<n2){
		cout<<n1<<" es menor que "<<n2<<endl;
	}
	else if(n1==n2){
		cout<<n1<<" es igual a "<<n2<<endl;
	}
	
	if(m1>m2){
		cout<<m1<<" es mayor que "<<m2<<endl;
	}
	else if(m1<m2){
		cout<<m1<<" es menor que "<<m2<<endl;
	}
	else if(m1==m2){
		cout<<m1<<" es igual a "<<m2<<endl;
	}		
	
}

int trescasos(){
	int n1, n2, m1, m2, p1, p2;
	cout<<"Ingrese el primer numero: ";cin>>n1;
	cout<<"Ingrese el segundo numero: ";cin>>n2;
	cout<<"Ingrese el primer numero: ";cin>>m1;
	cout<<"Ingrese el segundo numero: ";cin>>m2;
	cout<<"Ingrese el primer numero: ";cin>>p1;
	cout<<"Ingrese el segundo numero: ";cin>>p2;
	
	if(n1>n2){
		cout<<n1<<" es mayor que "<<n2<<endl;
	}
	else if(n1<n2){
		cout<<n1<<" es menor que "<<n2<<endl;
	}
	else if(n1==n2){
		cout<<n1<<" es igual a "<<n2<<endl;
	}
	
	if(m1>m2){
		cout<<m1<<" es mayor que "<<m2<<endl;
	}
	else if(m1<m2){
		cout<<m1<<" es menor que "<<m2<<endl;
	}
	else if(m1==m2){
		cout<<m1<<" es igual a "<<m2<<endl;
	}
	
	if(p1>p2){
		cout<<p1<<" es mayor que "<<p2<<endl;
	}
	else if(p1<p2){
		cout<<p1<<" es menor que "<<p2<<endl;
	}
	else if(p1==p2){
		cout<<p1<<" es igual a "<<p2<<endl;
	}				
}


int main(){
	int c;
	cout<<"COMPARANDO NUMEROS"<<endl;
	cout<<"Ingrese el numero de casos a evaluar (maximo 3): ";cin>>c;
	
	while(c>0){
		if(c==1){
			uncaso();
			cout<<"Ingrese el numero de casos a evaluar: ";cin>>c;
		}
		else if(c==2){
			doscasos();
			cout<<"Ingrese el numero de casos a evaluar: ";cin>>c;
		}
		else if(c==3){
			trescasos();
			cout<<"Ingrese el numero de casos a evaluar: ";cin>>c;
		}
		else if(c>3){
			cout<<"MAXIMO TRES CASOS"<<endl;
			cout<<"Ingrese el numero de casos a evaluar: ";cin>>c;
		}				
	}	
	return 0;
}
