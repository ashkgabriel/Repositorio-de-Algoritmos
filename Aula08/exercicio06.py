'''
Faça um algoritmo para determinar se um determinado vetor, digitado pelo usuário,
é um palíndromo.

Palíndromo: lido da direita para a esquerda, ou vice e versa, representm a mesma coisa.
Exemplo: "AMA"
'''

palavra = input("Digite a palavra a ser analisada: ")

palindromo = palavra.lower()[::-1]

if palavra == palindromo:
    print(f"A palavra {palavra} é um palíndromo.")

else:
    print(f"A palavra {palavra} não é um palíndromo.")