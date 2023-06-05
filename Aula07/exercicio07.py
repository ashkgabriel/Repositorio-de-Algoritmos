# Faça um programa que calcule os 10 primeiros números da sequencia de Fibonacci:

a = 0
b = 1

print(a, end = " ")

for i in range(1, 10):
    print(b, end = " ")
    a, b = b, a + b