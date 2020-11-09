'''
# Crie uma versão da Bola 8 Mágica
# Ela te da respostas a perguntas diretas. Use a criatividade
# Quando você fizer uma pergunta o programa tem que buscar 
# uma resposta aleatória para responder o usuário
'''
import random

answers = ['Sim', 'Não', 'Talvez', 'Fora de Serviço', 'Tente novamente mais tarde', 'Não tenho muita certeza', 'Talvez, sim, não', 'Ooops acho melhor você não saber']
user_want = True
print('Olá, eu sou a bola 8 mágica, eu sei a resposta para tudo no mundo')

while user_want == True:
    print('Qual a sua pergunta?')
    user_question = input()
    random_position = random.randint(0, len(answers) - 1)
    print(f'A resposta é: {answers[random_position]}')
    print()
    print('Você gostaria de fazer alguma pergunta? (Sim/Nao)')
    user_play = input()
    if user_play == 'nao' or user_play == 'Nao':
        print('Obrigada, volte sempre que quiser!')
        user_want = False
    else:
        user_want = True