'''
Faça um algoritmo que leia os dados de uma matriz de 4 linhas e 4 colunas, composta de 
elementos reais, e calcule a soma dos elementos da diagonal principal da matriz.
'''

matriz = [
    [0, 0, 0, 0], 
    [0, 0, 0, 0], 
    [0, 0, 0, 0], 
    [0, 0, 0, 0]
    ] 

for i in range (4):
    for j in range (4):
        matriz[i][j] = float(input(f"Digite os valores da matrix 4x4: ({i + 1}, {j + 1}): "))

soma = []

for i in range (4):
    for j in range (4):
        if i == j:
            soma.append(matriz[i][j])

print(f"A soma dos elementos da diagonal principal da matriz 4x4 informada é: {sum(soma)}")