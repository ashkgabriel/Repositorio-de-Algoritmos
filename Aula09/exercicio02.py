'''
Faça um algorimto que carregue um vetor de 10 elementos numéricos inteiros.
Após a finalização da entrada, o algoritmo deve escrever o maior valor e sua posição.
'''

vetor = []

for i in range (10):
    print("Digite 10 elementos numéricos e inteiros: ")
    entrada = int(input(f"Digite o {i + 1}º elemento: "))
    vetor.append(entrada)

vetor.sort()

print(vetor)