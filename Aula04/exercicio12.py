'''
Cada degrau de uma escada tem X cm de altura. Faça um algoritmo que receba a altura 
de cada degrau em cm e a altura que o usuário deseja alcançar subindo a escada (em 
metros). Faça as conversões, calcule e mostre quantos degraus o usuário deverá subir
para atingir seu objetivo.

Obs: não se preocupe com a altura do 
usuário!
'''

altura_degrau = int(input("Digite a altura do degrau (em centímetros): "))
altura_escada = float(input("Digite a altura da escada (em metros): ")) * 100

qtd_degraus = int(altura_escada / altura_degrau)

print(f"O usuário deve subir {qtd_degraus} degraus.")