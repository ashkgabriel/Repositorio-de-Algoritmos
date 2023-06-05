'''
Elabore um algoritmo que simule uma contagem regressiva de 10 minutos, ou seja,
mostre 10:00 e então 9:59, 9:58, ..., 9:00; 8:59, 8:58, até 0:00.
'''

from time import sleep

for minutos in range (9, -1, -1):
    for segundos in range (59, -1, -1):
        print(f"{minutos:02d}:{segundos:02d}")
        sleep(1)