'''
Faça uma função que receba como 
parâmetro o raio de uma esfera, calcule e 
retorne o valor de seu volume.

Volume da Esfera : v = 4/3 * R^3
'''

def esfera_vol(raio):
    volume = 4/3 * pow(raio, 3)

    return volume

raio = float(input("Digite a medida do raio da esfera: "))

print(f"O volume da esfera é de: {esfera_vol(raio)} [Unidades de Volume]")