from time import sleep
from random import randint
from random import choice


def letra(msm):
    for i in msm:
        sleep(0.15)
        print(i, end='', flush=True)


pais = ['Brasil', 'Argentina', 'Alemanha', 'França', 'Espanha',
        'Inglaterra', 'Italia', 'Uruguai', 'Holanda', 'Belgica']

print(' '*40, end='')
letra('Campeonato das Seleções\n')

for i in range(len(pais)):
    print(f'[{i}]{pais[i]}', end=' ')

letra('\n\nEscolha um Pais:')

while True:
    jogador = int(input('\n>> '))

    if 0 <= jogador <= 9:
        jogador = pais[jogador]
        pais.remove(jogador)

        print(f'Muito bem... Você escolheu {jogador}')
        break

    else:
        print('Ops... Ocorreu um erro!\nEscolha de acordo com o Indice, por favor!')

vitoria = derrota = empate = 0

while True:
    letra('\nPROCESSANDO...\n')

    if len(pais) == 0:
        break
    bot = choice(pais)
    pais.remove(bot)
    sleep(1)

    print(f'{jogador} vs {bot}')

    tempo = gp = gs = 0

    while tempo < 10:
        tempo += 1.25

        if randint(0, 5) % 3 == 0:
            if randint(0, 5) % 2 == 0:
                gp += 1
            else:
                gs += 1

            sleep(2)
            print(f'{jogador[:3].upper()}| {gp}\n{bot[:3].upper()}| {gs}')
            print('-=-'*8)

    if gp == gs:
        empate += 1
        print('Fim de jogo >> Empate.')
    elif gp > gs:
        vitoria += 1
        print('Fim de Jogo >> VITORIA.')
    else:
        derrota += 1
        print('Fim de Jogo >>  Derrota.')

if vitoria > derrota and vitoria > empate:
    print(f'Excelente Dezempenho...\n{jogador} fechou com...')
    sleep(1), print(f'{vitoria} Vitorias')
    sleep(1), print(f'{empate} Empate(s)')
    sleep(1), print(f'{derrota} Derrota(s)')
elif empate > vitoria and empate > derrota:
    print(f'{jogador} fechou com...')
    sleep(1), print(f'{empate} Empates')
    sleep(1), print(f'{vitoria} Vitoria(s)')
    sleep(1), print(f'{derrota} Derrota(s)')
else:
    print(f'Que pena... mais sorte na proxima...\n{jogador} fechou com...')
    sleep(1), print(f'{derrota} Derrotas')
    sleep(1), print(f'{vitoria} Vitoria(s)')
    sleep(1), print(f'{empate} Empate(s)')

letra('\nFIM...\n')