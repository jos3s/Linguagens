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

int remover(){
    int retorno=-1;
    NO*lixo=inicio;
    inicio=inicio->prox;
    retorno=lixo->valor;
    tam--;
    return retorno;
}

void imprimir(){
    int opcao;
    printf("Escolha uma das opções para impressão: \n1 Ordem direta \n2 Ordem inversa\n");
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

void excluir(){
    int lixo;
    lixo=remover();
    printf("\nO valor excluido foi: %d\n", lixo);
}

int main(){
    int i=0;
    while(i<5){
        inserir();
        i++;
    }
    imprimir();
    excluir();
    imprimir();
    system("pause");
    return 0;
}