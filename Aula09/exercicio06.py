'''
Faça um algoritmo que simule a jogada de dois dados de 6 faces. O programa deve usar randint
para rolar o primeiro dado e deve usar randint novamente para rolar o segundo dado. 
A soma das duas faces deve ser calculada. Assim: a soma variará de 2 a 12.
O programa deve rolar 30.000 vezes e mostrar a frequência com que a soma (de 2 a 12) 
aparecem. Verifique se o valor 7 corresponde a 1/6 das jogadas!
'''

from random import randint

dado1 = [0] * 7
dado2 = [0] * 7
soma = [0] * 13
estatistica = [0] * 13

for i in range (30000):
    x = randint(1, 6)
    y = randint(1, 6)
    dado1[x] += 1
    dado2[y] += 1
    soma_dados = x + y
    soma[soma_dados] += 1

for i in range (2, 13):
    estatistica[i] = soma[i] / 30000
    print(f"O número {i} foi somado {estatistica[i]:.2%} das vezes.")