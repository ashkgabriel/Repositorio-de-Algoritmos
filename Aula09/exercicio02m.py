'''
Faça um algoritmo que leia uma matriz 2x2, calcule e mostre uma matriz resultante que 
será a matriz digitada, multiplicada pelo maior elemento da matriz
'''

matriz = [[0, 0], [0, 0]] 

for i in range (2):
    for j in range (2):
        matriz[i][j] = int(input(f"Digite os valores da matrix 2x2: ({i + 1}, {j + 1}): "))

multiplicador = max(max(matriz))

print(f"A matriz digitada é: {matriz}")
print("O elemento da matriz de maior valor é: {multiplicador}")

produto = []

for i in range (2):
    linha = []
    for j in range (2):
        linha.append(matriz[i][j] * multiplicador)
    produto.append(linha)

print(f"O resultado da multiplicação de {multiplicador}, pela matriz {matriz} é: {produto}")