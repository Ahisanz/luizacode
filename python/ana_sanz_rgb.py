# letras = ['R', 'B', 'R', 'R','B','G','G','B','G','R']
# new_letras = []
# letras_r = letras.count('R')
# letras_b = letras.count('B')
# letras_g = letras.count('G')

# for r in range(letras_r):
#     new_letras.append('R')
# for b in range(letras_b):
#     new_letras.append('B')
# for g in range(letras_g):
#     new_letras.append('G')

# str_letras = ' - '.join(new_letras)

# print(new_letras)
# print(str_letras)

# letras = ['R', 'B', 'R', 'R','B','G','G','B','G','R']
# letras_r = []
# letras_b = []
# letras_g = []

# for letra in letras:
#     if letra == 'R':
#         letras_r.append(letra)
#     elif letra == 'B':
#         letras_b.append(letra)
#     else:
#         letras_g.append(letra)

# new_letras = letras_r + letras_b + letras_g
# str_letras = ' - '.join(new_letras)

# print(new_letras)
# print(str_letras)

# modolu random choice
'''
criar a lista em random
range de 15
'''

import random

rgb = ['R', 'G', 'B']
letras = [ random.choice(rgb) for letra in range(0,16)]
print(letras)

letras_r = [letra for letra in letras if letra == 'R']
letras_b = [letra for letra in letras if letra == 'B']
letras_g = [letra for letra in letras if letra == 'G']

new_letras = letras_r + letras_b + letras_g
str_letras = ' - '.join(new_letras)

print(new_letras)
print(str_letras)
