'''
Faça uma função que retorne o valor lógico V 
(verdadeiro) se o número inteiro passado por 
parâmetro for primo, e F (falso) se não.
Implemente sua função em um programa 
completo.
'''

def eh_primo(n):
    i = 1
    contador = 0
    while i <= n:
        if (n % i) == 0:
            contador += 1
        i += 1
    
    if contador == 2:
        return True
    else:
        return False

print("Os primeiros 50 números são os seguintes: ")

i, x = 2, 0

while x <= 50:
    if eh_primo(i):
        print(x, i)
        x += 1
    i += 1