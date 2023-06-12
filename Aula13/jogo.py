'''
Importe o arquivo funções.py

Implemente um programa de jogo de dados entre você e o computador, usando essa função
'''

import funcoes

decisao = input("Digite Y para iniciar: ").lower()

while decisao == "y":
    funcoes.dado()
    decisao = input("Digite 'Y' para continuar ou qualquer tecla para sair: ")
    
print("Até mais!")