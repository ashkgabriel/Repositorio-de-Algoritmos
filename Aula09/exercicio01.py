'''
Faça um algoritmo que carregue um vetor de 10 elementos numéricos inteiros.
Após a finalização de entrada, o algoritmo deve eescrever o mesmo vetor, na ordem
inversa de entrada.
'''

vetor = []

for i in range (10):
    print("Digite um vetor com 10 elementos numéricos inteiros: ")
    entrada = int(input(f"Digite o {i + 1}º elemento: "))
    vetor.append(entrada)

print(vetor[::-1])