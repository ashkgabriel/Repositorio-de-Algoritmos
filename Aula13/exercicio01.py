'''
Faça a implementação de uma função 
recursiva que calcule a sequência de 
Fibonacci, recebendo como parâmetro o 
número de elementos da sequência.
'''

def fib(i):
    if i == 0 or i == 1: return i
    else: return fib(i-1) + fib(i-2)

for i in range(0, 11):
    print(fib(i), end = " ")