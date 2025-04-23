# 3 threads

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

def validarLinhas(tabuleiro, resultado):
    for i in range(9):
        if sorted(tabuleiro[i]) != list(range(1, 10)):
            resultado[0] = False
            return
    resultado[0] = True

def validarColunas(tabuleiro, resultado):
    for i in range(9):
        coluna = [tabuleiro[j][i] for j in range(9)]
        if sorted(coluna) != list(range(1, 10)):
            resultado[1] = False
            return
    resultado[1] = True

def validarBlocos(tabuleiro, resultado):
    for blocoLinha in range(0, 9, 3):
        for blocoColuna in range(0, 9, 3):
            numeros = []
            for i in range(3):
                for j in range(3):
                    numeros.append(tabuleiro[blocoLinha + i][blocoColuna + j])
            if sorted(numeros) != list(range(1, 10)):
                resultado[2] = False
                return
    resultado[2] = True

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

resultado = [True, True, True]

t1 = threading.Thread(target=validarLinhas, args=(tabuleiro, resultado))
t2 = threading.Thread(target=validarColunas, args=(tabuleiro, resultado))
t3 = threading.Thread(target=validarBlocos, args=(tabuleiro, resultado))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("---- VALIDAÇÃO ----")
print(f"Linhas válidas: {resultado[0]}")
print(f"Colunas válidas: {resultado[1]}")
print(f"Blocos 3x3 válidos: {resultado[2]}")

if all(resultado):
    print("# SUDOKU VÁLIDO")
else:
    print("# SUDOKU INVÁLIDO")

print(f"\nSudoku resolvido com sucesso em {fim - inicio:.4f} segundos")
