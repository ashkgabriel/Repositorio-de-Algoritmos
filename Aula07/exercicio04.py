contador = 0
i = int(input("Deseja iniciar? (Sim = 1 / Não = 0)"))
soma_i = 0

while i != 0:
    i = int(input("Digite números inteiros para que se calcule a média dos números pares. "))    

    if i % 2 == 0 and i != 0:
        soma_i = soma_i + i
        contador += 1
    elif i == 0:
        break
    else:
        continue

print(f"A média aritmética dos números pares digitados é de: {soma_i/contador}.")

