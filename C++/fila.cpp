#include <iostream>
#include <cstdlib>
using namespace std;

typedef struct no{
    int valor;
    struct no*prox;
}NO;

NO*inicio=NULL;
NO*fim=NULL;
int tam=0;

void adicionar(int valor){
    NO*novo=(NO*)malloc(sizeof(NO));
    novo->valor=valor;
    novo->prox=NULL;
    if(inicio==NULL){
        inicio=novo;
        fim=novo;
    }else if(tam==1){
        inicio->prox=novo;
        fim=novo;
    }else{
        fim->prox=novo;
        fim=novo;
    }
    tam++;
}

void imprimir(){
    NO*aux=inicio;
    for(int i=0;i<tam;i++){
        if(i<tam-1){
            cout<<aux->valor<<" -> ";
        }else{
            cout<<aux->valor;
        }
        aux=aux->prox;
    }
    cout<<endl;
}

void inserir(){
    int valor;
    cout<<"Digite um valor:"<<endl;
    cin>>valor;
    adicionar(valor);
    
}

int remover(){
    NO*aux=inicio;
    int lixo=inicio->valor;
    inicio=inicio->prox;
    free(aux);
    return lixo;
}

int main(){
    int i=0;
    while(i<5){
        inserir();
        i++;
    }
    imprimir();
    system("pause");
    return 0;
}