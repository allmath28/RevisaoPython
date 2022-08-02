print('********************************')
print('Bem Vindo ao jogo de advinhação!')
print('********************************')

numero_secreto = 52

chute = int(input("Digite o seu número: "))

acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto

print(f'Você digitou {chute}')

if acertou:
    print(f'Você acertou')
else:
    if maior:
        print(f'Você errou! O seu chute foi maior que o número secreto.')
    elif menor:
        print(f'Você errou! O seu chute foi menor que o número secreto.')

print('Fim de jogo!')