print('Olá, qual é o seu nome?')
user_name = input()
print()
print(f'{user_name} qual ano você está na escola?')
user_year = input()
print()
user_notas = []
for trimes in range(1, 4):
    print(f'Qual foi a nota do seu {trimes}o trimestre?')
    user_nota = float(input())
    user_notas.append(user_nota)
    print()
user_media = (user_notas[0] + user_notas[1] + user_notas[2]) / 3
print()
if user_media >= 7:
    print(f'Parabens, {user_name} você foi aprovadx no {user_year}º ano!! \nE sua media final foi {user_media:.2f}')
else:
    print(f'Ah que pena {user_name}, sua media final é: {user_media:.2f}. \nVocê ainda não conseguiu passar o {user_year}º ano, continue se esforçando!')