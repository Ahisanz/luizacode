'''
Crie um programa que peça o nome do usuário, diga que é um prazer conhecê-lo e pergunte a idade dele.
O programa se apresentará como um robô - pode inventar o nome - e dirá quantos anos mais velhos que o usuário ele é.

O robô tem 107 anos
Não se preocupar se o usuário já fez aniversário ou não
'''


print("Olá, qual o seu nome?")
user_name = input()
print(f"Prazer te conhecer, {user_name}. Qual é a sua idade?")
user_years = input()
years_difference = 107 - int(user_years)
print(f"Eu sou a MaluRobo, e eu sou {years_difference} mais velha que você!")