'''
Elabore um algoritmo para ler/receber, separadamente, o primeiro nome, o nome do 
meio e o sobrenome de uma pessoa, e mostre o nome completo, correspondente.
'''

primeiro_nome = input("Digite o primeiro nome: ")
nome_meio = input("Digite o nome do meio: ")
sobrenome = input("Digite o sobrenome: ")

nome_completo = primeiro_nome + " " + nome_meio + " " + sobrenome

print(nome_completo)