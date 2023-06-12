'''
Faça algoritmo que carregue duas listas de dez elementos numéricos inteiros cada um. 

A partir dessas duas listas, crie um conjunto da união entre essas duas listas
'''

from random import randint

lista1 = []
lista2 = []

for i in range (10):
    x = randint(1, 100)
    y = randint(1, 100)
    lista1.append(x)
    lista2.append(y)

conjunto1 = set(lista1)
conjunto2 = set(lista2)

conjuntos = conjunto1.union(conjunto2)

print(conjuntos)