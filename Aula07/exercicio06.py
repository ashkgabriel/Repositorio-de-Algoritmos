'''
Faça um programa que receba um número inteiro x. 
Calcule e mostre o fatorial desse número (x!).
'''

numero = int(input("Digite um número inteiro e positivo: "))
fatorial = 1

for i in range (numero, 0, -1):
    fatorial *= i

print(f"O valor do fatorial deste número é de {fatorial}")