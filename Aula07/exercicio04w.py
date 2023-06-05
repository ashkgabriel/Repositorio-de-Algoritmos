'''
Faça um algoritmo que:

- Leia um número indeterminado de números que representam, cada um, a idade de um indivíduo. 
- Para finalizar, o usuário deverá digitar 0, que não entrará nos cálculos.
- Calcule e mostre a idade média e o número total de pessoas deste grupo de indivíduos.
'''
qtd = 1
soma_idade = 0

while True:
    
    idade = int(input(f"Digite a idade do {qtd}º indivíduo: "))
    
    if idade > 0:
        soma_idade = soma_idade + idade
        media = soma_idade / qtd
        
        print(f"A idade média de todos os {qtd} indivíduos é de: {media}")
        
        qtd += 1
    else:
        break