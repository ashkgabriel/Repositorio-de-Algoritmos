'''
Faça um algorimto que carregue um dicionário de 10 elementos 
onde a chave é o sobrenome da pessoa e o valor a sua idade.

Após a finalização da entrada, o algoritmo deve escrever o 
sobrenome da pessoa com maior idade.
'''

dicionario = {}

for i in range (3):
    sobrenome = input(f"Digite o sobrenome do {i + 1}º indivíduo: ")
    idade = int(input(f"Digite a idade do {i + 1}º indivíduo: "))
    dicionario[sobrenome] = idade

maior_idade = max(dicionario, key=dicionario.get)

# Código alternativo

# maior_idade = max(dicionario.values())
# sobrenome_maior_idade = ""
# for sobrenome, idade in dicionario.items():
#     if idade == maior_idade:
#         sobrenome_maior_idade = sobrenome
#         break

# print(f"O sobrenome do indivíduo com maior idade é: {sobrenome+maior_idade}")

print(f"O sobrenome do indivíduo com maior idade é: {maior_idade}")