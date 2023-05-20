'''
Faça um algoritmo que receba o salário de
um funcionário e o percentual de aumento,
calcule e mostre o valor do aumento e o
novo salário.
'''

salario = float ( input ("Salário atual: "))
p_aumento = float ( input ("Digite o valor percentual de aumento: "))
novoSalario = salario * (p_aumento/100 + 1)
print ("Novo salário: ", novoSalario)