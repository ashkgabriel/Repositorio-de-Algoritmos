'''
Faça um programa que receba a idade de um nadador e mostre a sua categoria usando as regras a seguir:
Categoria           Idade
Infantil            5 a 7
Juvenil             8 a 10
Adolescente         11 a 15
Adulto              16 a 30
Sênior              Acima de 30
'''

idade = int(input("Digite a idade do nadador :"))

if idade > 30:
    print("A categoria do nadador é SÊNIOR")
elif idade > 15:
    print("A categoria do nadador é ADULTO")
elif idade > 11:
    print("A categoria do nadador é ADOLESCENTE")
elif idade > 8:
    print("A categoria do nadador é JUVENIL")
else:
    print("A categoria do nadador é JUVENIL")