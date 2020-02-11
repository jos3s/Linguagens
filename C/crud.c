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
    tam--;
    return lixo;
}

void imprimir(){
    NO*aux=inicio;
    int i;
    for(i=0;i<tam;i++){
        puts("");
        printf("%d ", aux->valor);
        aux=aux->prox;
    }
    puts("");
}

void inserir(){
    int valor;
    puts("");
    printf("Digite um valor:");
    scanf(" %d", &valor);

    adicionar(valor);
}

void excluir(){
    int lixo;
    lixo=remover();
    printf("\nO valor excluido foi: %d\n", lixo);
}

void editar(){
    if(tam!=0){
        int novo;
        puts("\nDigite o novo valor, para o inicio:");
        scanf("%d", &novo);
        inicio->valor=novo;
    }else{
        puts("\nNão é possível editar");
    }
}

void menu(){
    int op;
    while (1){
        puts("============================");
        printf("1-Adicionar\n2-Imprimir\n3-Excluir\n4-Editar\n5-Encerrar");
        printf("\nDigite a opção desejada: ");
        scanf(" %d", &op);
        printf("============================");
        if(op==1){
            inserir();
        }else if(op==2){
            printf("\nImprimindo:");
            imprimir();
        }else if (op==3){
            excluir();
        }else if(op==4){
            editar();
        }else{
            break;
        }
    }

}

int main(){
    setlocale(LC_ALL, "Portuguese");
    menu();
    puts("");
    system("pause");
    return 0;
}
