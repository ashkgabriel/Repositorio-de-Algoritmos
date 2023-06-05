'''
Faça um programa que receba um número inteiro maior que 1. 
Ele deve verificar se o número fornecido é primo ou não, e mostrar a mensagem correspondente.

Lembre-se: um número primo só é divisível por 1 ou por ele mesmo.
'''

numero = int(input("Digite um número inteiro e positivo: "))

'''
Forma diferente de averiguar se o número é primo ou não:

Se o número não for divisível até a raiz quadrada dele será considerado um número primo.
'''

for i in range (2, int(numero ** 0.5) + 2):
    if numero == 2:
        primo = "é primo."
        break
    elif numero == 1:
        primo = "O número 1 não é considerado primo"
        break
    elif numero % i == 0:
        primo = "não é primo."
        break
    else:
        primo = "é primo."


print(f"O número {numero} {primo}")