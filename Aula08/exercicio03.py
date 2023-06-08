'''
Faça um algoritmo para ler nove caracteres numéricos em uma string. Mostre o conteúdo 
dessa string colando pontos e virgula, respectivamente nas posições inteiras e decimais. 

Exemplo: 
Digitado> 987654321
Mostrado> 9.876.543,21
'''

numero = input("Digite uma sequência de 9 caracteres: ")

numero_formatado = numero[0:1] + "." + numero[1:4] + "." + numero[4:7] + "," + numero[7:9]

print(numero_formatado)