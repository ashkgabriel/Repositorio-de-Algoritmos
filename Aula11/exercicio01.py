'''
Faça um algoritmo que carregue uma tupla de 10 elementos numéricos inteiros.
Após a finalização da entrada, o algoritmo deve escrever a mesma tupla, na ordem 
inversa de entrada.
'''

tupla = ()

for i in range (10):
    numero = int(input(f"Digite o {i + 1}º número: "))
    tupla += (numero, )

print(tupla[::-1])