from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('Suas opções:')
print(f'-=' * 20)
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')
jogador = int(input('Qual é a sua opção?'))
print(f'-=' * 20)

print(f'Você escolheu {itens[jogador]}!!')
print(f'O computador escolheu {itens[computador]}!!')
print(f'-=' * 20)

if computador == 0: #pedra
    if jogador == 0:
        print('Você e o computador empataram!!')
    if jogador == 1:
        print('Você venceu o computador!!')
    if jogador == 2:
        print('O computador te venceu!!')

if computador == 1: #papel
    if jogador == 0:
        print('Você venceu o computador!!')
    if jogador == 1:
        print('Você e o computador empataram!')
    if jogador == 2:
        print('O computador te venceu!!')

if computador == 2: #tesoura
    if jogador == 0:
        print('O computador te venceu!!')
    if jogador == 1:
        print('Você venceu o computador!!')
    if jogador == 2:
        print('Você e o computador empataram!')