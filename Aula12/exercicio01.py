'''
Faça uma função que retorne o valor lógico V 
(verdadeiro) se o número inteiro passado por 
parâmetro for par, e F (falso) se não.
Implemente sua função em um programa 
completo.
'''

def epar(n):
    return (n % 2 == 0)

n = int(input("Digite o valor a ser analisado: "))

if epar(n):
    print("O número é par.")
else:
    print("O número é impar")