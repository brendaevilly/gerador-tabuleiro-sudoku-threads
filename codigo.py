#Módulo para usar threads.
import threading 
#Random é usado para embaralhar números aleatoriamente.
import random


#Função para imprimir o tabuleiro sudoku.
def imprimeTabuleiro(tabuleiro):
    #linha é um lista do vetor, uma linha do tabuleiro sudoku.
    for linha in tabuleiro:
        #str(num) coverte o número da lista linha percorrida em uma string.
        #.join() junta todos os numeros da lista linha em uma string só. 
        print(" ".join(str(num) for num in linha))


def validarNumero(tabuleiro, linha, coluna, num):
    #Verifica se um número já existe na linha ou na coluna.
    for i in range(0, 9):
        if tabuleiro[linha][i] == num or tabuleiro[i][linha] == num:
            return False
        
    #Identifica o bloco 3x3 dentro do tabuleiro 9x9 que o número vai ou não ser inserido.
    blocoLinha = (linha//3)*3
    blocoColuna = (coluna//3)*3

    #Percorre o bloco para saber se já existe algum número igual ao que está sendo validado.
    for i in range(0, 3):
        for j in range(0, 3):
            if tabuleiro[blocoLinha+i][blocoColuna+j] == num:
                return False
    
    #Se o número não existe na linha, na coluna e no bloco 3x3 dentro do tabuleiro, a função retorna True.
    return True

tabuleiro = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0]]

imprimeTabuleiro(tabuleiro)

