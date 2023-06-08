'''
Faça um algoritmo que armazenará os 10 primeiros números primos acima de 100.
Ao final, o algoritmo deve mostrar os valores desse vetor.
'''

num = 100
primos = []

while len(primos) < 10:
    e_primo = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            e_primo = False
            break
    if e_primo:
        primos.append(num)
    num += 1

print(primos)