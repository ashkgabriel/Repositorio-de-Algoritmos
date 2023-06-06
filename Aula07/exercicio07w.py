# Faça um programa que calcule os 10 primeiros números da sequencia de Fibonacci.

contador = 0
a, b = 0, 1
while contador <=10:
    print(a, end = " ")
    a, b = b, a + b
    contador += 1