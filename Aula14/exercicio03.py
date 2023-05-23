numero = input("Digite o número do RA: ")

soma = 0
multiplicacao = 1

for i in numero:
    soma += int(i)
    multiplicacao *= int(i)

print(f"Multiplicação dos elementos: {multiplicacao}\nSoma dos elementos: {soma}")