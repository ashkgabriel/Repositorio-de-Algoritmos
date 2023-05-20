'''
Faça um algoritmo que receba o valor de
um depósito e o valor da taxa de juros,
calcule e mostre o valor do rendimento e
o valor total depois do rendimento.
'''

deposito = float(input("Digite o valor do depósito: "))
taxa_de_juros = float(input("Digite o valor do taxa de juros anual: "))

rendimento = deposito * taxa_de_juros/100

print(f"O investimento teve um rendimento anual de R${rendimento}, resultando num montante total de R${rendimento+deposito}")