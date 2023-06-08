'''
Elabore um algoritmo para determinar quantas vogais existem dentro de uma determinada
frase (que deve ser recebida do usuário).
'''

frase = input("Digite uma frase: ")

contagem = 0

for vogais in frase:
    if vogais.lower() in "aeiouáéíóúàâêôãõ":
        contagem += 1

print(f"Existem {contagem} vogais na frase '{frase}'.")