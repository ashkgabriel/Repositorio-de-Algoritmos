'''
FAZER UM PROGRAMA QUE RECEBA DOIS NÚMEROS E EXECUTE AS OPERAÇÕES 
LISTADAS A SEGUIR DE ACORDO COM A ESCOLHA DO USUÁRIO:
1. Média entre os números digitados
2. Diferença do maior pelo menor
3. Produto entre os números digitados
4. Divisão do primeiro pelo segundo
'''

num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))

media = (num1 + num2) / 2
print(f"A média entre os números é de: {media}")

if num1 > num2:
    print(f"A diferença entre os números é de: {num1 - num2}")
else:
    if num2 > num1:
        print(f"A diferença entre os números é de: {num2 - num1}")
    else:
        print("Os números são iguais.")

produto = num1 * num2
print(f"O produto dos números é igual a: {produto}")

divisao = num1 / num2
print(f"A divisão do primeiro número pelo segundo resulta em: {divisao}")