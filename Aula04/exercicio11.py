'''
Sabe-se que:
◼ 1 pé = 12 polegadas
◼ 1 jarda = 3 pés
◼ 1 milha = 1760 jardas
Faça um algoritmo que receba uma medida 
em pés, faça as conversões a seguir e 
mostre os resultados:
a) Polegadas
b) Jardas
c) milhas
'''

medida = int(input("Digite o valor da medida a ser convertida: "))

medida_polegadas = medida * 12
medida_jardas = medida / 3
medida_milhas = medida_jardas / 1760

print(f"A medida convertida em polegadas é: {medida_polegadas}")
print(f"A medida convertida em jardas é: {medida_jardas}")
print(f"A medida convertida em milhas é: {medida_milhas}")