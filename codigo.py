
#Função para imprimir o tabuleiro sudoku.
def imprimeTabuleiro(tabuleiro):
    #linha é um lista do vetor, uma linha do tabuleiro sudoku.
    for linha in tabuleiro:
        #str(num) coverte o número da lista linha percorrida em uma string.
        #.join() junta todos os numeros da lista linha em uma string só. 
        print(" ".join(str(num) for num in linha))

#Tamanho das linhas e colunas da "matriz" que será o tabuleiro de sudoku.
size = 9

#A "matriz" tabuleiro será um vetor de listas, cada lista é uma linha.
# [0 for col in range(size)] gera uma lista de tamanho size preenchida com 0s.
# for lin in range(size) gera size listas de 0s no vetor.
tabuleiro = [[0 for col in range(size)] for lin in range(size)]

imprimeTabuleiro(tabuleiro)

