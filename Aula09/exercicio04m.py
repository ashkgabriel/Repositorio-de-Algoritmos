'''
Faça um algoritmo que leia os valores de uma matriz 3x3 de elementos reais e crie a matriz
transposta da matriz fornecida.

Matriz transposta: 
Igual a simétrica. 
Em matemática, é o resultado da troca de linhas por colunas em uma determinada matriz. 

A[i,j] = A[j,i]
'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range (3):
    for j in range (3):
        matriz[i][j] = float(input(f"Digite os elementos da matriz 3x3: [{i + 1}, {j + 1}] "))

transposta = []

for i in range (3):
    transposta.append([])
    for j in range (3):
        transposta[i].append(matriz[j][i])

# Comandos comentados mostram a matriz de forma visual diferente.

# for i in range (3):
#     for j in range (3):
#         print(transposta[i][j], end=" ")
#     print()

print(transposta)