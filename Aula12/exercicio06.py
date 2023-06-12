'''
Crie uma função que receba como parâmetro 
3 números interios (representando horas, 
minutos e segundos). A função deve 
converter em segundos.

Por exemplo: 2 h, 40 min e 10 segundos 
correspondem a 9.610 segundos.
'''

horario = input("Digite o horário no formato HH:MM:SS: ")

def hora_segundos(horario):
    x = []
    x = horario.split(":")

    resposta_segundos = int(x[0]) * 3600 + int(x[1]) * 60 + int(x[2])
    return resposta_segundos

print(f"O horário convertido em segundos é: {hora_segundos(horario)}")