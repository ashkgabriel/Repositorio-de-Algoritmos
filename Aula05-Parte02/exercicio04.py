'''
Dados três valores X, Y e Z, verificar se eles podem ser os comprimentos dos lados de um 
triângulo e, se forem, verificar se é um triângulo eqüilátero, isósceles ou escaleno. 
Se eles não formarem um triângulo, escrever uma mensagem.

Considerar que:
•O comprimento de cada lado de um triângulo é menor que a soma dos outros dois lados;
•Chama-se eqüilátero o triângulo que tem três lados iguais;
•Chama-se isósceles o triângulo que tem o comprimento de dois lados iguais;
•Chama-se escaleno o triângulo que tem os três lados diferentes;
'''

x = float(input("Digite a medida do primeiro lado do triângulo: "))
y = float(input("Digite a medida do segundo lado do triângulo: "))
z = float(input("Digite a medida do terceiro lado do triângulo: "))

if x + y == z or x + z == y or y + z == x:
    print("As medidas informadas não formam um triângulo.")
else:
    if (x == y and x != z) or (x == z and x != y) or (y == z and y != x):
        print("As medidas informadas formam um triângulo isósceles.")
    elif x == y == z:
        print("As medidas informadas formam um triângulo equilátero.")
    else:
        print("As medidas informadas formam um triângulo escaleno.")