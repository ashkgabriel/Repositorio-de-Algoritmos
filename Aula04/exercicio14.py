'''
Faça um algoritmo que receba uma hora formada por hora e minutos (um número 
real), calcule e mostre a hora digitada apenas em minutos. 

Lembre-se de que:
◼ Para quatro e meia deve-se digitar: 4,30
◼ Os minutos vão de 0 a 60!
'''

horario = float(input("Digite o horário separando as horas dos minutos com um ponto '.' (Exemplo: 12.59): "))

horas = int(horario)
minutos = 100 * (horario - horas)

horario_minutos = horas * 60 + minutos

print(f"O horário digitado convertido em minutos pode ser representado por: {horario_minutos} minutos.")