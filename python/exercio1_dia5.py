import random

grupos = [1, 2, 3, 4, 5, 6, 7]
for sorteio in range(len(grupos) + 1):
    grupo = random.choice(grupos)
    print(grupo)
    grupos.remove(grupo)