'''
Booleans

Booleans são um tipo de dado que possui dois valores que podem ser considerados 0 ou 1, Falso ou Verdadeiro.

O que são Operadores de Comparação?

Igual que: ==
Diferente que: !=
Maior que: >
Maior ou igual a: >=
Menor que: <
Menor ou igual a: <=


'''
var1 = True

print(type(var1)) #<class 'bool'>

'''
O que são Operadores Booleans?

Com esses tipos de dados é possivel fazer operações Booleanas que são: And, Or & Not.
AND :  Contem todos os termos da pesquisa
OR: Contem pelo menos um
NOT: Não contem os termos especificados. Contrario do resultado dentro da operação

'''


#                 and             or
#             True    False   True    False   

# True        True    False   True    True
# False       False   False   True    False

# not True = False
# not False = True

#AND

var2 = 5
var3 = 8
var4 = 15 
var5 = 0

print( var2 == 4  and var3 == 8 ) #False
print( var2 == 5  and var3 == 8 ) #True

# OR
print( var2 == 4  or var3 == 8 ) #True
print( var2 == 5  or var3 == 8 ) #True
print( var2 == 4  and var3 == 7 ) #False

# NOT
print( not var2 == 5 ) #False

# Aplicações: conditions if/else, for loops, while loops

# Exemplo 1 -  and & or

if (var3 > var2) and (var4 < var5) :
    print('Com o and é False')

elif (var3 > var2) or (var4 < var5) :
    print('Com o or é True')

# Exemplo 2 - or & not
if (var3 < var2) or (not var3 == 7):
    print('var3 < var2 = False, var3 não é igual a 7 = False, mas not de False = True')

# Exemplo 3 - Checar se lista está vazia
lista = []
if lista: # A lista está vazia? Sim = False
    print(f"Lista vazia: {lista}.")
if not lista: # A lista está vazia? Sim = False
    print(f"Lista vazia: {lista}.")
lista = [1,4]
if lista: # A lista está vazia? Não = True
    print(f"Lista não está vazia: {lista}.")
