cadastro = []
info_individuo = []

def recebe_peso():
    while True:
        try:
            peso = float(input("Digite o seu peso: "))
            return peso
        except:
            print("Digite um peso válido.")
        else:
            if peso:
                return peso
            else:
                print("Digite um peso válido.")

def recebe_altura():
    while True:
        try:
            altura = int(input("Digite a sua altura: "))
        except:
            print(f"Altura inválida.")
        else:
            if altura:
                return altura
            else:
                print("Digite uma altura válida.")

def recebe_idade():
    while True:
        try:
            idade = int(input("Digite a sua idade: "))
        except:
            print(f"Idade inválida.")
        else:
            if idade:
                return idade
            else:
                print("Digite uma idade válida.")

def recebe_sobrenome():
    while True:
        try:
            sobrenome = input("Digite o sobrenome: ")
        except:
            print(f"Sobrenome inválido.")
        else:
            if sobrenome:
                if sobrenome.isalpha():
                    return sobrenome
                else:
                    print("Digite um sobrenome válido.")
            else:
                return sobrenome

continua = True
while continua == True:
    sobrenome = recebe_sobrenome()
    if sobrenome == "":
        break
    info_individuo.append(sobrenome)
    info_individuo.append(recebe_idade())
    info_individuo.append(recebe_altura())
    info_individuo.append(recebe_peso())
    cadastro.append(info_individuo)
    info_individuo = []

print(f"\nInformações do cadastro: \n{cadastro}")