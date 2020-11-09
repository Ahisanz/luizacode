print("Olá, qual seu nome?")
user_nome = input()
print(f"{user_nome}, em que ano você nasceu?")
user_ano = input()
print('Qual o mes do seu aniversário?')
user_month = input()
user_month = int(user_month)
if (user_month <= 10):
    user_idade = 2020 - int(user_ano)
else:
    user_idade = 2020 - int(user_ano) - 1
print(f"{user_nome}, você tem {user_idade} anos.")

# perguntar se já fez aniversário

'''
print("Ola, qual seu nome?")
user_nome = input()
print(f"{user_nome}, em que ano voce nasceu?")
user_ano = input()
print(f'{user_nome}, vc ja fez aniversario esse ano? (Sim/Nao)')
user_aniv = input()
if user_aniv == 'Sim' or user_aniv == 'sim' :
    user_idade = 2020 - int(user_ano)
    print(f"{user_nome},  voce ja fez aniversario, vc tem {user_idade} aninhos")
elif user_aniv == 'Nao' or user_aniv == 'nao':
    user_idade = 2020 - int(user_ano) - 1
    print(f"{user_nome}, se voce nao fez aniversario, vc tem {user_idade} aninhos")
'''