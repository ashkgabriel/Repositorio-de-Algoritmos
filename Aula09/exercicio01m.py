'''
Faça um algoritmo que leia uma matriz 2x2 e imprima os seus elementos na ordem:
1,1 =
1,2 =
2,1 =
2,2 =
'''

from random import randint

matriz = []

for i in range (2):
    linha = []
    for j in range (2):
        numero = randint(1, 100)
        linha.append(numero)
    matriz.append(linha)

print(matriz)
print(matriz[0][0])
print(matriz[0][1])
print(matriz[1][0])
print(matriz[1][1])