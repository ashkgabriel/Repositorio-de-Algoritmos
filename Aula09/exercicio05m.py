'''
Faça um algoritmo que receba uma matriz 10x10 de elementos inteiros e localize a 
posição (linha e coluna) do maior elemento da matriz.
'''

# Forma legal de iniciar uma matriz X por X

# matriz = [[0] * 10 for x in range(10)]

# Inserindo dados manualmente

# for i in range (10):
#     for j in range (10):
        # matriz[i][j] = int(input(f"Digite o elemento [{i + 1}, {j + 1}]: "))

# Código para criar matriz 10x10 de forma automática

from random import randint

matriz = []

for i in range (10):
    linha = []
    for j in range (10):
        numero = randint(1, 1000)
        linha.append(numero)
    matriz.append(linha)

maior_elemento = matriz[0][0]
linha_maior = 0
coluna_maior = 0

for i in range (10):
    for j in range (10):
        if matriz[i][j] > maior_elemento:
            maior_elemento = matriz[i][j]
            linha_maior = i
            coluna_maior = j

print(matriz)
print(f"O maior elemento da matriz é {maior_elemento}, na posição [{linha_maior + 1}, {coluna_maior + 1}]")