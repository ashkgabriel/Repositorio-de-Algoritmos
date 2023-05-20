''' 
Faça um algoritmo que receba a data de
nascimento de uma pessoa e a data atual
e mostre sua idade em anos, meses,
semanas e dias
'''

ano_nascimento = int(input("Digite seu ano de nascimento: "))
mes_nascimento = int(input("Digite seu mes de nascimento: "))
dia_nascimento = int(input("Digite seu dia de nascimento: "))

ano_atual = int(input("Digite o ano atual: "))
mes_atual = int(input("Digite o mes atual: "))
dia_atual = int(input("Digite o dia atual: "))

idade_anos = ano_atual - ano_nascimento
idade_meses = idade_anos * 12 + mes_atual
idade_dias = idade_anos * 365 + mes_atual * 30 + dia_atual
idade_semanas = int(idade_dias / 7)

print(f"Idade em anos: {idade_anos}\nIdade em meses: {idade_meses}\nIdade em semanas: {idade_semanas}\nIdade em dias: {idade_dias}")