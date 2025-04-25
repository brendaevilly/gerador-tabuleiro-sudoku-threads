# Sem threads

import random as ran
import time

ran.seed(42)

def jogada_valida(sudoku, linha, coluna, numero):
    for i in range(9):
        if sudoku[linha][i] == numero:
            return False
    for i in range(9):
        if sudoku[i][coluna] == numero:
            return False
        
    linha_canto = linha - linha % 3 
    coluna_canto = coluna - coluna % 3

    for i in range(3):
        for j in range(3):
            if sudoku[linha_canto + i][coluna_canto + j] == numero:
                return False 
    return True 

def preencher_tabuleiro(sudoku):
    for l in range(9):
        for c in range(9):
            if sudoku[l][c] == 0:
                numeros = list(range(1, 10))
                ran.shuffle(numeros)
                for num in numeros: 
                    if jogada_valida(sudoku, l, c, num):
                        sudoku[l][c] = num
                        if preencher_tabuleiro(sudoku): 
                            return True
                        sudoku[l][c] = 0
                return False
    return True

def eh_sudoku_valido(sudoku):
 
    for linha in sudoku:
        numeros = [num for num in linha if num != 0]
        if len(numeros) != len(set(numeros)):
            return False

    for c in range(9):
        coluna = [sudoku[l][c] for l in range(9) if sudoku[l][c] != 0]
        if len(coluna) != len(set(coluna)):
            return False

    for bloco_linha in range(0, 9, 3):
        for bloco_coluna in range(0, 9, 3):
            bloco = []
            for i in range(3):
                for j in range(3):
                    num = sudoku[bloco_linha + i][bloco_coluna + j]
                    if num != 0:
                        bloco.append(num)
            if len(bloco) != len(set(bloco)):
                return False

    return True

sudoku = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

'''sudoku = [[0]*9 for _ in range(9)]'''

inicio = time.time()

if preencher_tabuleiro(sudoku):
    print("--------- SUDOKU COMPLETO ---------")
    for linha in sudoku:
        print(linha)
else:
    print("Não foi possível preencher o tabuleiro.")

if eh_sudoku_valido(sudoku):
    print("\nO tabuleiro é válido!")
else:
    print("\nO tabuleiro é inválido.")

fim = time.time()

print(f"Tempo de execução: {fim - inicio:.4f} segundos")