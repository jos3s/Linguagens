#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <locale.h>
#include <math.h>

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

int remover(){
    NO*aux=inicio;
    int lixo=inicio->valor;
    inicio=inicio->prox;
    free(aux);
    return lixo;
}

void imprimir(){
    NO*aux=inicio;
    int i;
    for(i=0;i<tam;i++){
        printf("%d ", aux->valor);
        aux=aux->prox;
    }

}

void inserir(){
    int valor;

    printf("Digite um valor:");
    scanf(" %d", &valor);

    adicionar(valor);
}

int main(){

    int i=0;
    while(i<5){
        inserir();
        i++;
    }
    imprimir();
    puts("\n");
    remover();
    imprimir();

    return 0;
}