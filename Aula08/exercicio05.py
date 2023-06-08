'''
Faça um algoritmo para determinar quantas palavras existem em uma determinada frase.

Obs: Tanto a palavra, quanto a frase, devem ser informadas pelo usuário.
'''

frase = input("Digite a frase que deseja analisar sem nenhuma pontuação: ")
palavra = input("Digite a palavra que deseja contar o número de incidências: ")

contagem = 0

palavras = frase.split()


for incidencia in palavras:
    if incidencia.lower() == palavra.lower():
        contagem += 1

print(f"Há {contagem} incidências da palavra {palavra} na frase informada.")