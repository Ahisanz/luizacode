import random

rgb = ['R', 'G', 'B']
letras = [ random.choice(rgb) for letra in range(0,15)]
print(letras)

letras_r = [letra for letra in letras if letra == 'R']
letras_b = [letra for letra in letras if letra == 'B']
letras_g = [letra for letra in letras if letra == 'G']

new_letras = letras_r + letras_b + letras_g
str_letras = ' - '.join(new_letras)

print(new_letras)
print(str_letras)