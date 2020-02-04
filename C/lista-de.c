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

NO*inicio=NULL;
NO*fim=NULL;
int tam;

void adicionar(int valor, int pos){
    if(pos>=0 && pos<=tam){
        NO*novo=(NO*)malloc(sizeof(NO));
        novo->valor=valor;
        novo->prox=NULL;
        novo->ant=NULL;
        if(inicio==NULL){
            inicio=novo;
            fim=novo;
        }else if(pos==0){
            novo->prox=inicio;
            inicio->ant=novo;
            inicio=novo;
        }else if(pos==tam){
            fim->prox=novo;
            novo->ant=fim;
            fim=novo;
        }else{
            NO*aux=inicio;
            int i;
            for(i=0;i<pos;i++){
                aux=aux->prox;
            }
            novo->prox=aux;
            novo->ant=aux->ant;
            aux->ant->prox=novo;
            aux->ant=novo;
        }
        tam++;
    }
}

int remover(int pos){
    if(pos>=0 && pos<=tam){
        NO*lixo;
        NO*aux=inicio;
        int retorno=-1;
        int i;
        if(tam==1){
            lixo=inicio;
            retorno=lixo->valor;
            inicio=NULL;
            fim=NULL;
        }else if(pos==0){
            lixo=inicio;
            retorno=lixo->valor;
            inicio=inicio->prox;
            inicio->ant=NULL;
        }else if(pos==tam-1){
            lixo=fim;
            retorno=lixo->valor;
            fim->ant->prox=NULL;
            fim=fim->ant;
        }else{
            int i;
            for(i=0;i<pos;i++)
                aux=aux->prox;
            lixo=aux;
            retorno=lixo->valor;
            aux->ant->prox=aux->prox;
            aux->prox->ant=aux->ant;
        }
        free(lixo);
        tam--;
        return retorno;
    }
}

void imprimir(){
    int opcao;
    printf("\nEscolha uma opção:\n1 - Ordem direta \n2 - Ordem indireta\n");
    scanf("%d", &opcao);
    if(opcao==1){
        NO*aux=inicio;
        int i;
        for(i=0;i<tam;i++){
            printf("%d ", aux->valor);
            aux=aux->prox;
        }
    }else{
        NO*aux=fim;
        int i;
        for(i=0;i<tam;i++){
            printf("%d ", aux->valor);
            aux=aux->ant;
        }
    }
} 

void inserir(){
    int valor,pos;
    printf("Digite um valor e a posção:");
    scanf("%d %d", &valor, &pos);
    adicionar(valor,pos);
}

void excluir(){
    int pos, lixo;
    printf("Digite uma posição para remover:");
    scanf("%d", &pos);
    lixo=remover(pos);
    printf("O valor excluido foi: %d\n", lixo);
    
}

int main(){
    int i=0;
    while(i<3){
        inserir();
        i++;
    }    
    imprimir();
    puts("\n");
    excluir();
    imprimir();
  

return 0;
}
