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

def preencherTabuleiro(tabuleiro):
    for linha in range(9):
        for coluna in range(9):
            if tabuleiro[linha][coluna] == 0:
                #cria uma lista com numero de 1 a 9
                numeros = list(range(1,9))
                #embaralha a ordem 
                random.shuffle(numeros)
              
            for num in numeros:
                if validarNumero(tabuleiro, linha, coluna, num):
                    tabuleiro[linha][coluna]= num
                if preencherTabuleiro(tabuleiro):
                    return True
                tabuleiro[linha][coluna] = 0
                return False
    return True

resultado_linhas = False
resultado_colunas = False
resultado_blocos = False
                 
def validarLinha(tabuleiro):
    global resultado_linhas
    for linha in tabuleiro:
        if sorted(linha) != list (range(1,9)):
            resultado_linhas = False 
            return
        resultado_linhas = True

def validarColuna(tabuleiro):
    global resultado_colunas
    for i in range(9):
        coluna = [tabuleiro[j][i] for j in range(9)]
        if sorted(coluna) != list(range(1,10)):
            resultado_colunas = False
            return
    resultado_colunas = True

tabuleiro = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0]]

preencherTabuleiro(tabuleiro)
print("Tabuleiro preenchido com sucesso!")

print(" Sudoku:")
imprimeTabuleiro(tabuleiro)


t1 = threading.Thread(target=validarLinha, args=(tabuleiro,))
t2 = threading.Thread(target=validarColuna, args=(tabuleiro,))


t1.start()
t2.start()


#espera as threads terminaren
t1.join()
t2.join()

