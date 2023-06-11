'''
Faça um algoritmo que leia uma matriz 10x20 com números inteiros e some cada uma das 
linhas, armazenando o resultado das somas em um vetor. A seguir, multiplique cada elemento 
da matriz pela soma da linha e mostre a matriz resultante.
'''

# Criação automatizada da matriz 10x20

from random import randint

matriz = []

for i in range (10):
    linha = []
    for j in range (20):
        numero = randint(1, 100)
        linha.append(numero)
    matriz.append(linha)

print(f"A matriz antes de realizar a operação é:\n{matriz}")

soma = []

for linha in matriz:
    soma.append(sum(linha))

for i in range (len(matriz)):
        for j in range (len(matriz[i])):
            matriz[i][j] *= soma[i]

print(f"O vetor das somas das linhas é:\n{soma}")
print()
print(f"A matriz resultante é:\n{matriz}")