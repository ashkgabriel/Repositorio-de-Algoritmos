'''
Importe o pacote “Random” e prepare uma função função que irá retornar 
aleatoriamente um valor de um dos lados de um dado (valores variando de 1 a 6)
'''

import random

def dado():
    computador = random.randint(1,6)
    eu = random.randint(1,6)

    if computador > eu: return print(f"Você perdeu...\nComputador: {computador}\nVocê: {eu}")
    elif computador < eu: return print(f"Você ganhou!\nComputador: {computador}\nVocê: {eu}")
    else: return print("Empate")