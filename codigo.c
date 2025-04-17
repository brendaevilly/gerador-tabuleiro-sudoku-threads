#include <stdio.h>
#include <stdlib.h>

#define TAM 9

    void imprimirTabuleiro(int **tabuleiro) ;

    int main(){
        int **tabuleiro;
        tabuleiro = (int **)calloc(TAM, sizeof(int*));
        for(int i=0; i<TAM; i++){
            tabuleiro[i] = (int *)calloc(TAM, sizeof(int));
        }

        imprimirTabuleiro(tabuleiro);


        return 0;
    }

    //Funcao para imprimir o tabuleiro.
    void imprimirTabuleiro(int **tabuleiro){
        for(int i=0; i<TAM; i++) {
            if (i%3 == 0 && i!=0) printf("---------------------\n");

            for(int j=0; j<TAM; j++) {
                if (j%3 == 0 && j!=0) printf("| ");
                printf("%d ", tabuleiro[i][j]);
            }
            printf("\n");
        }
    }