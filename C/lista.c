#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <locale.h>
#include <math.h>

typedef struct no{
    int valor;
    struct no *prox;
}NO;

NO*inicio=NULL;
NO*fim=NULL;
int tam;

void adicionar(int valor, int pos){
    if(pos>=0 && pos<=tam){
        NO*novo=(NO*)malloc(sizeof(NO));
        novo->valor=valor;
        novo->prox=NULL;
        if(inicio==NULL){
            inicio=novo;
            fim=novo;
        }else if(pos==0){
            novo->prox=inicio;
            inicio=novo;
        }else if(pos==tam){
            fim->prox=novo;
            fim=novo;
        }else{
            NO*aux=inicio;
            int i;
            for(i=0;i<pos-1;i++){
                aux=aux->prox;
            }
            novo->prox=aux->prox;
            aux->prox=novo;
        }
        tam++;
    }
}

int remover(int pos){
    int retorno;
    if(pos>=0 && pos<=tam){
        NO*lixo;
        NO*aux=inicio;
        int i;
        if(pos==0){
            lixo=inicio;
            retorno=lixo->valor;
            inicio=inicio->prox;
        }else if(pos==tam-1){
            for(i=0;i<tam-2;i++)
                aux=aux->prox;
            lixo=fim;
            retorno=lixo->valor;
            aux->prox=NULL;
            fim=aux;
        }else{
            for(i=0;i<pos-1;i++)
                aux=aux->prox;
            lixo=aux->prox;
            retorno=lixo->valor;
            aux->prox=aux->prox->prox;
        }
        tam--;
        free(lixo);
        return retorno;
    }
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
    int valor,pos;
    printf("Digite um valor e a posição:");
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