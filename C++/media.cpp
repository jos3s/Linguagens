#include <iostream>
#include <string>
#include <stdlib.h>
using namespace std;

typedef struct aluno{
    char nome[20];
    float nota[3];
    float media;
}ALUNO;

void pegardados(ALUNO & alu){
    cout<<"Digite o nome: ";
    cin>>alu.nome;
    cout<<"Digite a notas: ";
    cin>>alu.nota[0]>>alu.nota[1]>>alu.nota[2];
    alu.media=(alu.nota[0]+alu.nota[1]+alu.nota[2])/3.0;
}

void imprimir(ALUNO & aluno){
    cout<<"\nNome: "<<aluno.nome<<endl;
    cout<<"Nota 1:"<< aluno.nota[0]<<endl;
    cout<<"Nota 2:"<< aluno.nota[1]<<endl;
    cout<<"Nota 3:"<< aluno.nota[2]<<endl;
    cout<<"Média: "<<aluno.media<<endl;
}

int main(){

    ALUNO alunos[2];
    int i=0;
    int a=0;
    while(i<2){
        pegardados(alunos[i]);
        i++;
    }
    while(a<2){
        imprimir(alunos[a]);
        a++;
    }
    system("pause");
    return 0;
}