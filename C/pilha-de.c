#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <locale.h>
#include <math.h>

typedef struct no{
    int valor;
    struct no *prox;
    struct no *ant;
}NO;

NO*inicio=NULL; //TOPO
NO*fim=NULL;
int tam=0;

void adicionar(int valor){
    NO*novo=(NO*)malloc(sizeof(NO));
    novo->valor=valor;
    novo->prox=NULL;
    novo->ant=NULL;
    if(inicio==NULL){
        novo->prox=inicio;
        inicio=novo;
        fim=novo;
    }else{
        novo->prox=inicio;
        inicio->ant=novo;
        inicio=novo;
    }
    tam++;
}

int remover(){
    int retorno=-1;
    NO*lixo=inicio;
    if(tam==1){
        retorno=lixo->valor;
        inicio=NULL;
        fim=NULL;
    }else{
        retorno=lixo->valor;
        inicio=inicio->prox;
        inicio->ant=NULL;
    }
    tam--;
    free(lixo);
    return retorno;
}

void imprimir(){
    int opcao;
    printf("\nEscolha uma das opções para impressão: \n1 Ordem direta \n2 Ordem inversa\n");
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
    scanf("%d", &valor);
    adicionar(valor);
}

void excluir(){
    int lixo;
    lixo=remover();
    printf("\nO valor excluido foi: %d", lixo);
}

int main(){
    int i=0;
    while(i<3){
        inserir();
        i++;
    }
    imprimir();
    excluir();
    imprimir();
return 0;
}