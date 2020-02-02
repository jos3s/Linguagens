#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <locale.h>
#include <math.h>

typedef struct no{
    int valor;
    struct no *prox;
}NO;

NO*inicio=NULL; //TOPO
int tam=0;

void adicionar(int valor){
    NO*novo=(NO*)malloc(sizeof(NO));
    novo->valor=valor;
    novo->prox=NULL;
    novo->prox=inicio;
    inicio=novo;
    tam++;
}

int remover(){
    NO*lixo=inicio;
    int retorno=inicio->valor;
    inicio=inicio->prox;
    free(lixo);
    tam--;
    return retorno;
}

void imprimir(){
    NO*aux=inicio;
    int i;
    for(i=0;i<tam;i++){
        printf("%d ", aux->valor);
        aux=aux->prox;
    }
    puts("");
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
    printf("O valor excluido foi: %d", lixo);
}

int main(){
    int i=0;
    while(i<3){
        inserir();
        i++;
    }
    imprimir();
    excluir();
return 0;
}