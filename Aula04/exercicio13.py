'''
Sabe-se que o quilowatt de energia custa um oitavo do salário mínimo. Faça um 
algoritmo que receba o valor do salário mínimo e a quantidade de quilowatts 
consumida por uma residência. Calcule e mostre:
a) O valor, em reais, de cada quilowatt
b) O valor, em reais, a ser pago por essa residência
c) O valor, em reais, a ser pago com desconto de 15%
'''

salario_minimo = float(input(" Digite o valor do salário mínimo: "))
qtd_kwh = float(input(" Digite a quantidade de energia consumida em KWh: "))

custo_kwh = salario_minimo / 8
consumo_mensal = qtd_kwh * custo_kwh
consumo_desconto = consumo_mensal * 0.85

print(f"O valor em R$ por cada KWh é de: R${custo_kwh:.2f}")
print(f"O valor em R$ a ser pago neste mês é de: R${consumo_mensal:.2f}")
print(f"O valor em R$ a ser pago neste mês, com 15% de desconto é de: R${consumo_desconto:.2f}")