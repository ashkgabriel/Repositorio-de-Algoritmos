# Faça um programa que receba um número inteiro e verifique se esse número é par ou ímpar.

numero = int(input("Digite um número inteiro: "))

if numero % 2 != 0:
    print(f"O número {numero} é ímpar.")
else:
    print(f"O número {numero} é par.")