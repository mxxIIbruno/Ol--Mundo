# Amigo Secreto
from random import choice
from random import randint

pessoas = list()
for i in range(int(input('\nQUANTAS PESSOAS? '))):
    pessoas.append(str(input(f'Pessoa {i+1}: ')))

amigos = list()
tamanho = int(len(pessoas) / 2)
chave = randint(1, tamanho - 1)

for i in range(2):
    lista = list()

    while len(lista) < tamanho:
        p = choice(pessoas)
        pessoas.remove(p)
        lista.append(p)

    amigos.append(lista[:])

for i in range(tamanho):
    print(f'{amigos[0][i]}\033[41mFoi\033[m{amigos[1][i]}')

parte_dois = False
cont = 0
copia_lista = amigos[:]

print('\nAmigos parte 2')
while not parte_dois:
    amigos.clear()

    for i in copia_lista[0]:
        indice = copia_lista[0].index(i)
        nova_ordem = copia_lista[0][(indice + chave) % tamanho]
        amigos.append(nova_ordem)
    
    for i in range(len(copia_lista[0])):
        if amigos[i] != copia_lista[0][i]:
            cont += 1
        else:
            cont = 0
        
    if cont == len(copia_lista[0]):
        parte_dois = True

for i in range(tamanho):
    print(f'{copia_lista[1][i]}\033[41mAmigo\033[m{amigos[i]}')
