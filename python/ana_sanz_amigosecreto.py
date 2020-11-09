'''
Escolher um para cada, resposta tem que ser Rachel => Phoebe, e Phoebe => Monica e tals.

'''
import random


friends = ['Phoebe', 'Rachel', 'Monica', 'Joe', 'Chandler', 'Ross', 'Gunther']
friends_random = friends[:]
couples = []
tries = 0

for couple in range(0, len(friends)):
    friend_1 = random.choice(friends)
    friend_2 = random.choice(friends_random)

    while friend_1 == friend_2:
        friend_1 = random.choice(friends)
        tries += 1
        if tries > 5:
            break

    tries = 0
    couples.append([friend_1, friend_2])
    print(f'{friend_1} tirou {friend_2}')
    friends.remove(friend_1)
    friends_random.remove(friend_2)
# print(couples)