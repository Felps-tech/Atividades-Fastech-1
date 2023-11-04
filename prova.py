biblioteca_idade = {}
lista_idade_S = []
lista_idade_C = []
lista_idade_D = []
quantidade_s = 0
quantidade_c = 0
quantidade_d = 0
quantidade_s_M = 0
quantidade_c_M = 0
quantidade_d_M = 0
quantidade_s_F = 0
quantidade_c_F = 0
quantidade_d_F = 0

while True:
    Estado_Civil = str(input("Digite seu estado civil [Solteiro(a) = S Casado(a) = C Divorciado(a) = D] ")).upper()
    Idade = int(input("Digite sua idade "))
    Sexo = str(input("Digite seu sexo [Masculino = M Feminino = F] ")).upper()
    sair = str(input("Deseja terminar a pesquisa? [S,N]")).upper()
    if Idade not in biblioteca_idade:
        biblioteca_idade[Idade] = []
    if Estado_Civil == "S":
        lista_idade_S.append(Idade)
    if Estado_Civil == "C":
        lista_idade_C.append(Idade)
    if Estado_Civil == "D":
        lista_idade_D.append(Idade)    
    biblioteca_idade[Idade].append([Estado_Civil, Sexo])
    if sair == "S":
        break
    # Chave {Idade} Valor {Estado Civil e Sexo}
quantidade_total = sum(len(Idades) for Idades in biblioteca_idade.values())

for valor in biblioteca_idade.values(): #{Estado Civil, Sexo}
    for ec in valor[0]: # Estado civil
        if ec == "S":
            quantidade_s += 1
        if ec == "C":
            quantidade_c += 1
        elif ec == "D":
            quantidade_d += 1 

for valor in biblioteca_idade.values():
    for ec in valor[0]: 
        if ec == "S" and Sexo == "M":
            quantidade_s_M += 1
        if ec == "S" and Sexo == "F":
            quantidade_s_F += 1
        if ec == "C" and Sexo == "M":
            quantidade_c_M += 1
        if ec == "C" and Sexo == "F":
            quantidade_c_F += 1
        if ec == "D" and Sexo == "M":
            quantidade_d_M += 1
        if ec == "D" and Sexo == "F":
            quantidade_d_F += 1
            
print("---" * 30)
print(f"Quantidade total {quantidade_total}") # Quantidade Total     
print(f'Porcentagem de solteiro {(quantidade_s/quantidade_total)*100}%')
print(f'Porcentagem de casado {(quantidade_c/quantidade_total)*100}%')
print(f'Porcentagem de divorciado {(quantidade_d/quantidade_total)*100}%')

try:
    print(f"A maior idade entre os solteiros foi {max(lista_idade_S)}")
except ValueError as error:
    print("Não teve habitantes solteiro")
try:
    print(f"A maior idade entre os casados foi {max(lista_idade_C)}")
except ValueError as error:
    print("Não teve habitantes casados")
try:
    print(f"A maior idade entre os divorciados foi {max(lista_idade_D)}")
except ValueError as error:
    print("Não teve habitantes divorciados")
try:
    print(f"A menor idade entre os solteiros foi {min(lista_idade_S)}")
except ValueError as error:
    print("Não teve habitantes solteiros")
try:
    print(f"A menor idade entre os casados foi {min(lista_idade_C)}")
except ValueError as error:
    print("Não teve habitantes casados")
try:
    print(f"A menor idade entre os divorciados foi {min(lista_idade_D)}")
except ValueError as error:
    print("Não teve habitantes divorciados")
print(f"Quantidade de solteiros do sexo masculino: {quantidade_s_M}")
print(f"Quantidade de solteiros do sexo feminino: {quantidade_s_F}")
print(f"Quantidade de casados do sexo masculino: {quantidade_c_M}")
print(f"Quantidade de casados do sexo feminino: {quantidade_c_F}")
print(f"Quantidade de divorciados do sexo masculino: {quantidade_d_M}")
print(f"Quantidade de divorciados do sexo feminino: {quantidade_d_F}")