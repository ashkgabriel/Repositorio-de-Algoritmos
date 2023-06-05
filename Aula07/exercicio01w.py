'''
Faça um algoritmo que leia dois valores b e N inteiros e positivos, 
calcule e mostre o valor E, conforme a fórmula a seguir.

E = (b ** 1) + (b ** 2) + (b ** 3) + ... + (b ** N)
'''

e = 0
b = int (input ("Digite o valor da base: "))
n = int (input ("Digite um número inteiro: "))
i = 1

while (i <= n):
    e = e + b ** i
    i += 1

print(f"E = {e:.2f}")