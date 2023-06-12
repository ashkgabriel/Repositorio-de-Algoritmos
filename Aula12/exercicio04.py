'''
Construa uma função que retorne o MDC de dois números 
inteiros passados por parâmetro.
'''

from math import gcd

def mdc(n1, n2):
    mdc = gcd(n1, n2)
    return mdc

n1 = int(input("Digite o primeiro numero para efetuar o cálculo do máximo divisor comum: "))
n2 = int(input("Digite o segundo numero para efetuar o cálculo do máximo divisor comum: "))

print(f"O MDC dos números {n1} e {n2} é: {mdc(n1,n2)}")