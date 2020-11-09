'''Desafio Jogo
Regras: Crie um programa pegue nome do usuário e que explique as regras do jogo para o usuário.
Pensei em um numero de 1 a 20
Consegue adivinhar?
Espaço para usuário digitar a opção
Espaço para usuário digitar a opção
6 tentaivas
cada palpite - usar palpite ecomparar se igual ou diferente
igual ESCREVE PARABÉNS
SE O NUMERO FOR MENOR >>ESCREVE O NUMERO QUE PENSEI É MENOR
SE O NUMERO FOR MAIOR ESCREVER O NUMERO QUE PENSEI É MAIOR


Homework Aula 1 - Um jogo

- Criar um programa que pegue nome do usuário e explique as regras do jogo para o usuário.
- Pense em um numero de 1 a 20
- Sortear um numero aleatório
- Usuário tente adivinha numero sorteado
- Usuário só pode ter 6 chances
- Pegar cada palpite e verificar se é: maior, igual ou menor que o número sorteado
- Falar mensagem que o número que o usuário deu palpite é maior, igual ou menor que o número sorteado.
- Colocar condição de parada "break" nas condições de verificação'''

# import random


# print("Seja bem vindo! Qual é o seu nome?")
# user_name = input()
# print(f"Prazer, {user_name}, vou te explicar as regras do jogo, primeiro eu vou pensar em um número de 1 a 20.")
# random_number = random.randint(1, 21)
# print("Pronto, pensei! Agora eu vou te dar 6 chances para acertar qual é o número que eu pensei. Valendo!")
# user_try = 1
# for chances in range(0,6):
#     user_guess = input()
#     user_guess = int(user_guess)
#     if(random_number == user_guess):
#         print("GANHOOUUU!!!!")
#         print(f"{user_name} você acertou!")
#         if(user_try == 1):
#             print(f"Sim, o numero é {random_number} você acertou de primera!")
#         else:
#             print(f"Sim, o numero é {random_number} e você acertou na {user_try}ª vez")
#         break
#     elif(random_number != user_guess and user_try <= 5 ):
#         try_left = 6 - user_try
#         if(user_guess > 20):
#             print(f"ôôôôÔôôÔÔ {user_name}!! O número tem que ser menor ou igual a 20. Tente outra vez!")
#         if(user_guess < random_number):
#             print("O numero que eu pensei é maior que esse!")
#         else:
#             print("O numero que eu pensei é menor que esse!")  
#         print(f"Tente outra vez, te faltam {try_left} chances!")
#         user_try += 1
#     else: 
#         print(f"Ah, que pena... O número era {random_number}. Jogue outra vez.")
#         break

import random


print("Seja bem vindo! Qual é o seu nome?")
user_name = input()
print(f"Prazer, {user_name}, vou te explicar as regras do jogo, primeiro eu vou pensar em um número de 1 a 20.")
random_number = random.randint(1, 21)
print()
print("Pronto, pensei! Agora eu vou te dar 6 chances para acertar qual é o número que eu pensei. Valendo!")
for chances in range(1,7):
    user_guess = int(input())
    if random_number == user_guess:
        print("GANHOOUUU!!!!")
        print(f"{user_name} você acertou!")
        if chances == 1:
            print(f"Sim, o numero é {random_number} você acertou de primera!")
        else:
            print(f"Sim, o numero é {random_number} e você acertou na {chances}ª vez")
        break
    elif random_number != user_guess and chances <= 5:
        try_left = 6 - chances
        if user_guess > 20:
            print(f"ôôôôÔôôÔÔ {user_name}!! O número tem que ser menor ou igual a 20. Tente outra vez!")
        elif user_guess < random_number:
            print("O numero que eu pensei é maior que esse!")
        else:
            print("O numero que eu pensei é menor que esse!")  
        print(f"Tente outra vez, te faltam {try_left} chances!")
if user_guess != random_number:
    print(f"Ah, que pena... O número era {random_number}. Jogue outra vez.")
