import random


print('********************************')
print('Bem Vindo ao jogo de advinhação!')
print('********************************')

numero_secreto = random.randrange(1, 101)
rodada = 1
total_de_tentativas = 0
pontos = 1000

print(f'Escolha o nível de dificuldade:')
print(f'[1] Facil  [2] Médio  [3] Difícil')
dificuldade = int(input())

if (dificuldade == 1):
    total_de_tentativas = 15

elif (dificuldade == 2):
    total_de_tentativas = 10

else:
    total_de_tentativas = 5


for rodada in range(1, total_de_tentativas+1):

    print(f'Rodada {rodada} de {total_de_tentativas}')

    chute = int(input("Digite um número de 1 a 100: "))

    if (chute < 1 or chute > 100):
        print(f'Você deve digitar um numero entre 1 e 100!')
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    print(f'Você digitou {chute}')

    if acertou:
        print(f'Você acertou e fez {pontos} pontos!')
        break
    else:
        if maior:
            print(f'Você errou! O seu chute foi maior que o número secreto.')
            if (rodada == total_de_tentativas):
                print(f'O número secreto era {numero_secreto}. Você fez {pontos} pontos.')

        elif menor:
            print(f'Você errou! O seu chute foi menor que o número secreto.')
            if (rodada == total_de_tentativas):
                print(f'O número secreto era {numero_secreto}. Você fez {pontos} pontos.')
        pontos_perdidos = abs(numero_secreto - chute)
        pontos -= pontos_perdidos

print('Fim de jogo!')
