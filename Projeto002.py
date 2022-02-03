# Minha Autoria
from time import sleep

class JogoDaVelha:
    def __init__(self, jogo):
        self.jogo = jogo

    def letra(self, mensagem):
        for i in str(mensagem):
            sleep(0.1)
            print(i, end='', flush=True)

    def lin(self, matriz):
        for linha in matriz:
            for elemento in linha:
                lista.append(elemento)

    def tela(self, matriz):
        for linha in matriz:
            for elemento in linha:
                print(elemento, end=' ')
            print()

jogo = JogoDaVelha('3x3')

print(' '*20, end='')
jogo.letra('Jogo da Velha')

matriz = [[7,8,9],[4,5,6],[1,2,3]]
lista = []

jogo.letra('\nEscolha as Posições:\n')
game_over = vez = False

while True:
    posição = int(input('Sair = [0]>> '))

    if 7 <= posição <= 9:
        indice = matriz[0].index(posição)
        if vez == False:
            matriz[0][indice] = 'X'
            vez = True
            jogo.tela(matriz)
        else:
            matriz[0][indice] = 'O'
            vez = False
            jogo.tela(matriz)
    elif 4 <= posição <= 6:
        indice = matriz[1].index(posição)
        if vez == False:
            matriz[1][indice] = 'X'
            vez = True
            jogo.tela(matriz)
        else:
            matriz[1][indice] = 'O'
            vez = False
            jogo.tela(matriz)
    elif 1 <= posição <= 3:
        indice = matriz[2].index(posição)
        if vez == False:
            matriz[2][indice] = 'X'
            vez = True
            jogo.tela(matriz)
        else:
            matriz[2][indice] = 'O'
            vez = False
            jogo.tela(matriz)
    else:
        if posição == 0:
            break
        jogo.tela(matriz)
        print('Escolha pelo teclado númerico.')

    for linha in matriz:
        if linha.count('X') == 3:
            game_over = True
            print('Vitoria do X')
        if linha.count('O') == 3:
            game_over = True
            print('Vitoria do O')
    
    if game_over == True:
        break
    
    cont_X = cont_O = 0

    for vezes in range(len(matriz)):
        jogo.lin(matriz)
        for coluna in range(vezes, len(lista), 3):
            if 'X' in str(lista[coluna]):
                cont_X += 1
                if cont_X == 3:
                    game_over = True
                    print('Vitoria do X')
            if 'O' in str(lista[coluna]):
                cont_O += 1
                if cont_O == 3:
                    game_over = True
                    print('Vitoria do O')
        
        lista.clear()
        cont_X = cont_O = 0
    
    if game_over == True:
        break

    jogo.lin(matriz)
    for diagonal_principal in range(0, len(lista), 4):
        if 'X' in str(lista[diagonal_principal]):
            cont_X += 1
            if cont_X == 3:
                game_over = True
                print('Vitoria do X')
        if 'O' in str(lista[diagonal_principal]):
            cont_O += 1
            if cont_O == 3:
                game_over = True
                print('Vitoria do O')
    
    lista.clear()
    cont_X = cont_O = 0

    if game_over == True:
        break

    jogo.lin(matriz)
    for diagonal_segundaria in range(2, 7, 2):
        if 'X' in str(lista[diagonal_segundaria]):
            cont_X += 1
            if cont_X == 3:
                game_over = True
                print('Vitoria do X')
        if 'O' in str(lista[diagonal_segundaria]):
            cont_O += 1
            if cont_O == 3:
                game_over = True
                print('Vitoria do O')
    
    lista.clear()
    cont_X = cont_O = 0

    if game_over == True:
        break

jogo.letra('\nGAME OVER\n')