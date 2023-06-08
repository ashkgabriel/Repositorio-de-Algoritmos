'''
Faça algoritmo que carregue dois vetores de dez elementos numéricos cada um e mostre 
um vetor resultante na intercalação desses dois vetores.
'''

from random import randint

vetor = []
vetor1 = []
vetor2 = []

contador = 0

while contador <=10:
    vetor1.append(randint(1, 100))
    vetor2.append(randint(1, 100))
    contador += 1

for i in range (10):
    vetor.append(vetor1[i])
    vetor.append(vetor2[i])

print(vetor1)
print(vetor2)
print(vetor)