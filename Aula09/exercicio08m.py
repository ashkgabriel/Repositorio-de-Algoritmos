'''
Faça um algoritmo que receba uma matriz de 
5x5 com números reais. Ao final o algoritmo 
deve calcular e mostrar a média dos elementos 
que estão nas linhas pares da matriz.
'''

matriz = [[0] * 5 for x in range (5)]

for i in range (5):
    for j in range (5):
        numero = float(input(f"Digite o elemento [{i + 1}, {j + 1}] da matriz 5x5: "))
        matriz[i][j] = numero

soma = 0
contador = 0

for i in range (1, 5, 2):
    soma += sum(matriz[i])
    contador += len(matriz[i])

media = soma / contador

print(f"A média dos valores dos elementos das linhas pares é: {media}")