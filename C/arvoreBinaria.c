#include <stdio.h>
#include <stdlib.h>

typedef struct no{
    int chave;
    int valorpai;
    struct no*esq;
    struct no*dir;
}NO;

NO*raiz=NULL;

NO* buscar(int x, NO* pt){
    if(pt==NULL)
        return NULL;
    else if(x==pt->chave)
        return pt;
    else if(x<pt->chave){
        if(pt->esq==NULL)
            return pt;
        else
            return buscar(x,pt->esq);
    }else{
        if(pt->dir==NULL)
            return pt;
        else
            return buscar(x,pt->dir);
    }

}

int buscareal(int x){
    NO*pt=buscar(x,raiz);
    if(pt->chave==x)
        return pt->chave;
    else
        return -1;
}

void adicionar(int x){
    NO*pt=buscar(x,raiz);
    if(pt==NULL || pt->chave!=NULL){
        NO*pt1=malloc(sizeof(NO));
        pt1->chave=x;
        pt1->dir=NULL;
        pt1->esq=NULL;
        pt1->valorpai=-1;
        if(pt==NULL){
            raiz=pt1;
        }else{
            if(x<pt->chave){
                pt->esq=pt1;
                pt1->valorpai=pt->chave;
            }else{
                pt->dir=pt1;
                pt1->valorpai=pt->chave;
            }
        }
    }else{
        puts("Inserção invalida");
    }
}

void imprimirPos(NO*pt){
    if(pt->esq!=NULL)
        imprimirPos(pt->esq);
    if(pt->dir!=NULL)
        imprimirPos(pt->dir);
    printf("%d ", pt->chave);
}

void imprimirPre(NO*pt){
    printf("%d ", pt->chave);
    if(pt->esq!=NULL)
        imprimirPre(pt->esq);
    if(pt->dir!=NULL)
        imprimirPre(pt->dir);
}

void imprimirIn(NO*pt){
    if(pt->esq!=NULL)
        imprimirIn(pt->esq);
    printf("%d ", pt->chave);
    if(pt->dir!=NULL)
        imprimirIn(pt->dir);
}

void imprimirvpai(NO*pt){
    if(pt->esq!=NULL)
        imprimirvpai(pt->esq);
    printf("O no %d tem como pai %d ",pt->chave, pt->valorpai);
    puts("");
    if(pt->dir!=NULL)
        imprimirvpai(pt->dir);
}

NO* remover(NO*pt,int x){
    if(pt==NULL)
        return NULL;
    else if(x<pt->chave)
        pt->esq=remover(pt->esq,x);
    else if(x>pt->chave)
        pt->dir=remover(pt->dir,x);
    else{
        if(pt->esq==NULL && pt->dir==NULL){
            free(pt);
            return NULL;
        }else if(pt->esq==NULL){
            NO*aux=pt;
            pt=pt->dir;
            free(aux);
        }else if(pt->dir==NULL){
            NO*aux=pt;
            pt=pt->esq;
            free(aux);
        }else{
            NO*aux=pt->esq;
            while(aux->dir!=NULL)
                aux=aux->dir;
            pt->chave=aux->chave;
            aux->chave=x;
            pt->esq=remover(aux->esq,x);
        }

    }
    return pt;
}

void inserir(){
    int valor;
    printf("Qual valor você quer adicionar:");
    scanf("%d",&valor);
    adicionar(valor);
}

int main(){
   
    char op;
    do{
        inserir();
        printf("Quer continuar adicionando? [s/n]:");
        scanf("%s",&op);
    }while(op!='n');
    puts("\nIn-ordem");
    imprimirIn(raiz);
    puts("");
    imprimirvpai(raiz);
return 0;
}