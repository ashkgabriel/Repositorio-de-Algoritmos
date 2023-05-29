'''
Faça um algoritmo que leia um valor N inteiro e positivo, 
calcule e mostre o valor E, conforme a fórmula a seguir.

E = (2 ** 1) + (2 ** 2) + (2 ** 3) + ... + (2 ** N)
'''

N = int(input("Digite um valor inteiro e positivo: "))
E = 0

for i in range (1, N + 1):
    E = E + pow(2, i)

print(f"O valor de E é: {E:.2f}")