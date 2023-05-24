'''
Faça um programa que receba o preço líquido de um produto e o seu código de origem e mostre a sua 
procedência e o preço final, calculado pelo imposto relativo a sua procedência. A procedência 
obedece a tabela a seguir:

Código Origem   |    Procedência    |  % Imposto
    1           |    Sul            |     11%
    2           |    Norte          |     13%
    3           |    Nordeste       |     9%
    4           |    Centro-Oeste   |     12%
    5           |    Sudeste        |     18%
'''

preco = float(input("Digite o preço líquido do produto: "))
codOrigem = int(input("Digite o código de origem: "))

if codOrigem == 1:
    print(f"O produto procede da região Sul e o valor final é de: R${preco * 1.11:.2f}")
elif codOrigem == 2:
    print(f"O produto procede da região Norte e o valor final é de: R${preco * 1.13:.2f}")
elif codOrigem == 3:
    print(f"O produto procede da região Nordeste e o valor final é de: R${preco * 1.09:.2f}")
elif codOrigem == 4:
    print(f"O produto procede da região Centro-Oeste e o valor final é de: R${preco * 1.12:.2f}")
elif codOrigem == 5:
    print(f"O produto procede da região Sudeste e o valor final é de: R${preco * 1.18:.2f}")