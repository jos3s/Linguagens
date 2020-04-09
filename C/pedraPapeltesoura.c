#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <locale.h>
#include <math.h>

int main(){
    setlocale(LC_ALL, "Portuguese");
    int jog=0, comp=0;
    char jogadas[3][10]={"Papel","Tesoura","Pedra"};
    srand(time(NULL));
    comp=rand()%3;
    do{
        printf("0-Papel\n1-Tesoura\n2-Pedra\n");
        printf("Qual sua escolha: ");
        scanf("%d", &jog);
    }while(jog<0 || jog>2);
    printf("O jogador escolheu : %s\nO computador escolheu: %s\n", jogadas[jog], jogadas[comp]);
    if (jog==0){
        if (comp==0){
            printf("Deu empate");
        }else if(comp==1){
            printf("Computador ganhou");
        }else{
            printf("Você ganhou");
        }
    }else if(jog==1){
        if (comp==0){
            printf("Você ganhou");
        }else if(comp==1){
            printf("Deu empate");
        }else{
            printf("Computador ganhou");
        }
    }else{
        if (comp==0){
            printf("Computador ganhou");
        }else if(comp==1){
            printf("Você ganhou");
        }else{
            printf("Deu empate");
        }
    }  
    return 0;
}