'''
Faça um algoritmo que leia um número não determinado de pares de valores [m,n], todos 
inteiros e positivos, um par de cada vez e que calcule e mostre a soma de todos os 
números inteiros entre m e n (inclusive). 

Na digitação dos pares m,n deve-se validar que m é maior que n.
'''
soma_hist = 0

while True:
    soma = 0
    m = int(input('Digite um número para ser atribuído a M: '))
    n = int(input('Digite outro número para ser atribuído a N: '))
    
    if m > n:
        for i in range (n, m + 1):
            soma = soma + i
            soma_hist = soma_hist + i
        print(f"A soma dos inteiros entre {m} e {n} é de: {soma}\n A mesma operação para todos os pares de M e N digitados anteriormente é de: {soma_hist} ")
    else:
        sair = input("O valor de M é menor que de N. Digite Y para continuar ou qualquer tecla para sair da aplicação.")
        if sair.upper() == "Y":
            continue
        else:
            break
