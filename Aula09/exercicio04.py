'''
Faça um algoritmo que leia 20 palavras de no máximo 10 caracteres, e após a leitura, realize 
um processo qualquer que inverta os caracteres de cada uma das palavras.
'''

palavras = []

contador = 0

while contador <= 20 and True:
    palavra = input("Digite uma palavra de até 10 caracteres (ou 0 para sair): ")
    if palavra != "0" and len(palavra) < 10:
        palavras.append(palavra)
        contador += 1
    else:
        break

sarvalap = palavras[::-1]

print(f"A lista de palavras {palavras}\nExibida de forma invertida é:\n{sarvalap}")