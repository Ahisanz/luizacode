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
