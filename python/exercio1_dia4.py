def soma(nota_1, nota_2, nota_3):
    user_media = (nota_1 + nota_2 + nota_3)/3
    return user_media


print('Olá qual o seu nome?')
user_name = input()
user_notas = []
for trim in range(1, 4):
    print(f'qual a nota do seu {trim} trimestre?')
    user_nota = float(input())
    user_notas.append(user_nota)

user_final = soma(user_notas[0], user_notas[1], user_notas[2])
print(f'Sua media final é {user_final:.2f}')