'''
Faça uma função que determine se um ano 
qualquer, no formato AAAA, é bissexto.
A função retorna 1 se o ano é bissexto e 
0(zero) se não.
'''

def eh_bissexto(ano):
    if (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False

ano = int(input("Digite um ano no formato AAAA: "))

eh_bissexto(ano)

if eh_bissexto(ano):
    print(f"O ano {ano} é Bissexto")
else:
    print(f"O ano {ano} não é bissexto")