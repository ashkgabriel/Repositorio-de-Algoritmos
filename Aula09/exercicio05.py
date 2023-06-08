'''
Faça um Algoritmo que simule 6000 jogadas de um dado de 6 faces. Para simular o 
resultado utilize a função randintAo final, mostre a frequência de sorteio de 
cada uma das faces.
'''

from random import randint

dado = [0] * 7
estatistica = [0] * 7

# Importante destacar que é necessário 7 elementos para não precisar inserir mais um cálculo para o elemento de index = 0 

for i in range (6000):
    x = randint(1, 6)
    dado[x] += 1

for i in range(1, 7): # Range inicia em 1 para descartar a contagem do elemento de índice = 0
    estatistica[i] = dado[i]/6000

for i in range(1, 7):
    print(f"O lado {i} foi sorteado {dado[i]} = {estatistica[i]:.2%}")