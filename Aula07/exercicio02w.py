'''
Faça um algoritmo que calcule a área de um triângulo. 
Este algoritmo não pode permitir a entrada de dados 
inválidos, ou seja, medidas menores ou iguais a zero.
'''

base = float (input ("Digite a medida da base do triângulo em cm: "))

while (base <= 0):
    base = float (input ("Digite a medida da base do triângulo em cm: "))
    
while True:
    altura = float (input ("Digite a medida da altura do triângulo em cm: "))
    if altura > 0:
        break
area = (base * altura)/2
print(f"O valor da área do triângulo é de {area:.2f} cm")