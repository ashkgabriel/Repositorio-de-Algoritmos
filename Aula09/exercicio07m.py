'''
Crie um algoritmo que receba uma matriz 8x8 
com números inteiros e mostre uma mensagem 
dizendo se a matriz digitada é simétrica ou não.

Uma matriz só pode ser considerada simétrica 
se A[i,j] = A[j,i]
'''

matriz = [[0] * 8 for x in range (8)]

for i in range (8):
    for j in range (8):
        matriz[i][i] = int(input(f"Digite o elemento [{i + 1}, {j + 1}]: "))

contador = 0

for i in range (len(matriz)):
    for j in range (len(matriz[0])):
        contador += 1

if contador == (len(matriz[0])) ** 2:
    print("A matriz informada é simétrica.")
else:
    print("A matriz informada é assimétrica")