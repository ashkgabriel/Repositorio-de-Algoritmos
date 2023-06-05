# Faça um programa que receba um número inteiro x. 
# Calcule e mostre o fatorial desse número (x!).

while True:
    x = int (input ("Digite um número inteiro: "))
    if x >= 0:
        break
    print("Valor inválido. Digite um número maior do que 0.")

fatorial = 1
i = 2
while i <= x:
     fatorial = fatorial * i
     i += 1

print(f"O valor de {x}! é igual a {fatorial}")