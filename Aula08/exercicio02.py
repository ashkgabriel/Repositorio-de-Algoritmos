'''
Faça um algoritmo que solicite uma data no formato de uma string – dd/mm/aaaa. 
Mostre essa data no formato AAAAMMDD
'''

data = input("Digite uma data no formato dd/mm/aaaa: ")

nova_data = data.split("/")

dia = nova_data[0]
mes = nova_data[1]
ano = nova_data[2]

print(ano + mes + dia)