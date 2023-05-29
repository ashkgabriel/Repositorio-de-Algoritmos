'''
Faça um algoritmo que leia o valor do peso e da altura de 20 pessoas. 
Ao final, o algoritmo deve mostrar:

- O peso médio
- A altura média
- O maior e o menor IMC
Obs: IMC (Índice de Massa Corporal) – calculado a partir da fórmula:
IMC = massa / (altura * altura)
'''

for i in range (1, 21):
    imc = 0
    peso = float(input(f"Digite o valor do peso da pessoa Nº{i}: "))
    altura = float(input(f"Digite o valor da altura da pessoa Nº{i}: "))

    imc = peso / altura ** 2

print(f"O menor valor de IMC calculado foi de: {min(imc)}")
print(f"O maior valor de IMC calculado foi de: {max(imc)}")