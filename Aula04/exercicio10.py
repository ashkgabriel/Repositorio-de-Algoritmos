'''
Faça um algoritmo que receba um número
positivo e maior que zero, calcule e mostre:
a) O número digitado ao quadrado
b) O número digitado ao cubo
c) A raiz quadrada do número digitado
Observação:
Exp(x,y) – Calcula a potência de x elevado a y
Raizq(x) – Calcula a raiz quadrada de x
'''
import math

numero = float((input("Digite um valor positivo e maior que zero: ")))

print(f"{numero} elevado ao quadrado é: {pow(numero,2)}")
print(f"{numero} elevado ao cubo é: {pow(numero,3)}")
print(f"A raiz quadrada de {numero} é: {math.sqrt(numero)}")
