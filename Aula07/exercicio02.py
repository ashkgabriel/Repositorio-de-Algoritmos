'''
Faça um algoritmo que calcule a soma dos primeiros 50 números pares. 
Este algoritmo não recebe valores do teclado. 

Os primeiros números pares são 2, 4, 6...
'''
soma = 0
for i in range (1,101):
    if (i%2 == 0):
        soma += i
    else:
        continue
print(soma)