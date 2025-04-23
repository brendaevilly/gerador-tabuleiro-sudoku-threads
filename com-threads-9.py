# 9 threads

import threading
import random
import time

random.seed(42)

def imprimeTabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" ".join(str(num) for num in linha))

def validarNumero(tabuleiro, linha, coluna, num):
    for i in range(9):
        if tabuleiro[linha][i] == num or tabuleiro[i][coluna] == num:
            return False
    blocoLinha = (linha // 3) * 3
    blocoColuna = (coluna // 3) * 3
    for i in range(3):
        for j in range(3):
            if tabuleiro[blocoLinha + i][blocoColuna + j] == num:
                return False
    return True

def preencherTabuleiro(tabuleiro):
    for linha in range(9):
        for coluna in range(9):
            if tabuleiro[linha][coluna] == 0:
                numeros = list(range(1, 10))
                random.shuffle(numeros)
                for num in numeros:
                    if validarNumero(tabuleiro, linha, coluna, num):
                        tabuleiro[linha][coluna] = num
                        if preencherTabuleiro(tabuleiro):
                            return True
                        tabuleiro[linha][coluna] = 0
                return False
    return True

def validarTudo(tabuleiro, index, resultado_linhas, resultado_colunas, resultado_blocos):
    if sorted(tabuleiro[index]) != list(range(1, 10)):
        resultado_linhas[index] = False

    coluna = [tabuleiro[i][index] for i in range(9)]
    if sorted(coluna) != list(range(1, 10)):
        resultado_colunas[index] = False

    blocoLinha = (index // 3) * 3
    blocoColuna = (index % 3) * 3
    numeros = []
    for i in range(3):
        for j in range(3):
            numeros.append(tabuleiro[blocoLinha + i][blocoColuna + j])
    if sorted(numeros) != list(range(1, 10)):
        resultado_blocos[index] = False

tabuleiro = [
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

'''
tabuleiro = [[0]*9 for _ in range(9)]
'''

inicio = time.time()
preencherTabuleiro(tabuleiro)
fim = time.time()

print("Tabuleiro preenchido com sucesso!")
print("---- SUDOKU ----")
imprimeTabuleiro(tabuleiro)

resultado_linhas = [True] * 9
resultado_colunas = [True] * 9
resultado_blocos = [True] * 9

threads = []

for i in range(9):
    t = threading.Thread(target=validarTudo, args=(tabuleiro, i, resultado_linhas, resultado_colunas, resultado_blocos))
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

print("---- VALIDAÇÃO ----")
print(f"Linhas válidas: {all(resultado_linhas)}")
print(f"Colunas válidas: {all(resultado_colunas)}")
print(f"Blocos 3x3 válidos: {all(resultado_blocos)}")

if all(resultado_linhas) and all(resultado_colunas) and all(resultado_blocos):
    print("# SUDOKU VÁLIDO")
else:
    print("# SUDOKU INVÁLIDO")

print(f"\nSudoku resolvido com sucesso em {fim - inicio:.4f} segundos")
