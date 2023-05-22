'''
(FORBELLONE; EBERSPÄCHER, 2000 - pág. 46) 
Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo 
que calcule seu peso ideal, utilizando as seguintes fórmulas:

- para homens: (72.7 * h) – 58;
- para mulheres: (62.1 * h) – 44.7.
'''

sexo = input ("Informe seu sexo biológico: ")
altura = float (input ("Informe sua altura em metros: "))

if sexo.upper() == "HOMEM" or sexo.upper() == "H" or sexo.upper() == "MASCULINO":
    pesoideal = float (72.7 * altura) - 58
    print (f"Seu peso ideal é: {pesoideal:.2f}")
    
elif sexo.upper() == "MULHER" or sexo.upper() == "M" or sexo.upper() == "FEMININO":
    pesoideal = (62.1 * altura) - 44.7
    print (f"Seu peso ideal é: {pesoideal:.2f}")