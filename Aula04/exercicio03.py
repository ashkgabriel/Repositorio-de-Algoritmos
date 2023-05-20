'''
Faça um algoritmo que receba o ano de
nascimento de uma pessoa e o ano atual
e mostre:
a) A idade dessa pessoa em anos;
b) A idade dessa pessoa em meses;
c) A idade dessa pessoa em dias;
d) A idade dessa pessoa em semanas.
'''

ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))

idade_anos = ano_atual - ano_nascimento
idade_meses = idade_anos * 12
idade_dias = idade_anos * 365
idade_semanas = idade_dias / 7

# a) Idade em anos.
print(f"Idade em anos: {idade_anos}")

# b) Idade em meses.

print(f"Idade em meses: {idade_meses}")

# c) Idade em dias.

print(f"Idade em dias: {idade_dias}")

# d) Idade em semanas.

print(f"Idade em semanas: {idade_semanas}")