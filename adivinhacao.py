print('********************************')
print('Bem Vindo ao jogo de advinhação!')
print('********************************')

numero_secreto = 52
total_de_tentativas = 3
rodada = 1

for rodada in range(total_de_tentativas+1):

    print(f'Rodada {rodada} de {total_de_tentativas}')

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
