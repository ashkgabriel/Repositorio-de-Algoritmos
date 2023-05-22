'''
(FORBELLONE; EBERSPÄCHER, 2000 - pág. 46) 
Faça um algoritmo que leia o ano de nascimento de uma pessoa, calcule e mostre sua idade e, 
também, verifique e mostre se ela já tem idade para votar (16 anos ou mais) e para conseguir 
a Carteira de Habilitação (18 anos ou mais).
'''

from datetime import datetime

ano_nascimento = int(input("Digite o ano de nascimento: "))

idade = datetime.now().year - ano_nascimento

if idade >= 18:
    print("Você já pode tirar a Carteira de Habilitação!")
else:
    if idade >= 16:
        print("Você já tem idade para votar!")
    else:
        print("Você é menor de idade...")