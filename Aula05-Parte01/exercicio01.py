# FAZER UM ALGORITMO QUE LEIA DOIS NÚMEROS E ESCREVA (DEVOLVA COMO RESULTADO) O MENOR DELES.

primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))

if primeiro_numero < segundo_numero:
    print(f"{primeiro_numero} é menor.")
elif segundo_numero < primeiro_numero:
    print(f"{segundo_numero} é menor.")
else:
    print("Os 2 números são iguais.")