for numero in range(1, 101):
    if numero % 15 == 0:
        print('Dedezinha Querida')
    elif numero % 3 == 0:
        print('Dedezinha')
    elif numero % 5 == 0:
        print('Querida')
    else: 
        print(numero)