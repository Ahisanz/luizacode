import random


print("Seja bem vindo! Qual é o seu nome?")
user_name = input()
print(f"Prazer, {user_name}, vou te explicar as regras do jogo, primeiro eu vou pensar em um número de 1 a 20.")
random_number = random.randint(1, 21)
print("Pronto, pensei! Agora eu vou te dar 6 chances para acertar qual é o número que eu pensei. Valendo!")
user_try = 1
for chances in range(0,6):
    user_guess = input()
    user_guess = int(user_guess)
    if(random_number == user_guess):
        print("GANHOOUUU!!!!")
        print(f"{user_name} você acertou!")
        if(user_try == 1):
            print(f"Sim, o numero é {random_number} você acertou de primera!")
        else:
            print(f"Sim, o numero é {random_number} e você acertou na {user_try}ª vez")
        break
    elif(random_number != user_guess and user_try <= 5 ):
        try_left = 6 - user_try
        if(user_guess > 20):
            print(f"ôôôôÔôôÔÔ {user_name}!! O número tem que ser menor ou igual a 20. Tente outra vez!")
        if(user_guess < random_number):
            print("O numero que eu pensei é maior que esse!")
        else:
            print("O numero que eu pensei é menor que esse!")  
        print(f"Tente outra vez, te faltam {try_left} chances!")
        user_try += 1
    else: 
        print(f"Ah, que pena... O número era {random_number}. Jogue outra vez.")
        break