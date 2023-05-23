y = int(input("Digite o número de cabeças: "))

pes = y * 3 + 1

def cercado(y):
    coelhos = (y + 1) / 2
    patos = y - coelhos

    return print(f"Número de patos: {patos}\nNúmero de coelhos: {coelhos}")

cercado(y)