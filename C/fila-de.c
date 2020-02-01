#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <locale.h>
#include <math.h>

typedef struct no{
    int valor;
    struct no* prox;
    struct no*ant;
}NO;

NO*inicio=NULL;
NO*fim=NULL;
int tam=0;

void adicionar(int valor){
    NO*novo=(NO*)malloc(sizeof(NO));
    novo->valor=valor;
    novo->prox=NULL;
    novo->ant=NULL;
    if(inicio==NULL){
        inicio=novo;
        fim=novo;
    }else{
        fim->prox=novo;
        novo->ant=fim;
        fim=novo;
    }
    tam++;
}

void imprimir(){
    int opcao;
    printf("Escolha uma das opções para impressão: \n1 Ordem direta \n2 Ordem inversa");
    scanf("%d", &opcao);
    int i;
    if(opcao==1){
        NO*aux=inicio;
        for(i=0;i<tam;i++){
        printf("%d ", aux->valor);
        aux=aux->prox;
        }
    }else{
        NO*aux=fim;
        for(i=0;i<tam;i++){
            printf("%d ", aux->valor);
            aux=aux->ant;
        }
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
    system("pause");
    return 0;
}