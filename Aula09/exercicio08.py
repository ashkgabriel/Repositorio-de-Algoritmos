'''
Faça um algoritmo que lê 10 números inteiros e os armazena em um vetor A.
Depois de armazenado, o algoritmo fará a ordenação desses números (em ordem crescente de valores) 
e os colocará no vetor B. Ao final o algoritmo deve mostrar os dois vetores: A e B.
'''

va = []
vb = []
contador = 0

while contador < 10:
    numeros = int(input(f"Digite o {contador + 1}º elemento: "))
    contador += 1
    va.append(numeros)
    vb.append(numeros)

vb.sort()

print(f"Vetor A: {va}\nVetor B: {vb}")