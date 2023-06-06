'''
Faça um programa que receba um número inteiro maior que 1. Ele deve verificar se o número fornecido é primo 
ou não, e mostrar a mensagem correspondente.

Lembre-se: um número primo só é divisível por 1 ou por ele mesmo
'''

numero = int(input("Digite um número inteiro e maior que 1: "))

i = 2

if numero <= 1:
    primo = "não é considerado primo"
else:
    primo = "é primo."

while i <= int(numero ** 0.5):
    if numero % i == 0:
        primo = "não é primo."
        break
    i += 1

print(f"O número {numero} {primo}")