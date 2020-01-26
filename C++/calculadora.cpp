#include <iostream>
#include <stdlib.h>
#include <locale>
using namespace std;

int main(){

    float valor1, valor2;
    char op;
    cout<<"Digite um valor:";
    cin>>valor1;
    cout<<"Digite outro valor:";
    cin>>valor2;
    cout<<"Digite a operação:"<<endl;
    cout<<"+ Adição\n- Subtração \n* Multiplicação \n/ Divisão"<<endl;
    cin>>op;

    switch (op){
        case '+':
            cout<<"O resultado da soma é: "<< valor1+valor2<<endl;
            break;
        case '-':
            cout<<"O resultado da soma é: "<< valor1-valor2<<endl;
            break;
        case '*':
            cout<<"O resultado da soma é: "<< valor1*valor2<<endl;
            break;
        case '/':
            if(valor1>valor2){
                cout<<"O resultado da soma é: "<< valor1/valor2<<endl;
            }else{
                cout<<"O resultado da soma é: "<< valor2/valor1<<endl;
            } 
            break;
        default:
            cout<<"A operação digitada é inválida.";
            break;
    }

    system("pause");
    return 0;
}