'''
Faça um algoritmo que receba três notas de um aluno, calcule e mostre a média aritmética e a mensagem que 
segue a tabela abaixo. Para alunos de exame, calcule e mostre a nota que deverá ser tirada no exame para 
aprovação, considerando que a média do exame é 6,0 (e que a média após o exame é resultado da média 
aritmética entre a nota do exame e a média antes do exame).

0,0         e   <3,0    Reprovado
>= 3,0      e   < 7,0   Exame
>=7,0       e   <=10,0  Aprovado
'''

primeira_nota = float(input("Digite o valor da primeira nota: "))
segunda_nota = float(input("Digite o valor da segunda nota: "))
terceira_nota = float(input("Digite o valor da terceira nota: "))

media = (primeira_nota + segunda_nota + terceira_nota) / 3

if (media) >= 7:
    print ("Aprovado")

elif (media >=3):
        print (f"Sua média é {media:.1f}. Necessário exame")
        nota =  12 - media
        print (f"Você precisa tirar no mínimo nota {nota:.1f}")

else:
    print("Você foi reprovado")