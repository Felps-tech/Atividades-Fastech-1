analistas = {}
quantidade_notas = {}
while True:
    idade = input("Digite a idade do analista (ou 'sair' para encerrar): ")
    if idade == "sair":
        break
    nota = input("Digite a nota do analista: (Otimo) (Bom) (Regular) (Pessimo) ").upper()
    if idade not in analistas:
        analistas[idade] = []
    analistas[idade].append(nota)

quantidade_geral = sum(len(notas) for notas in analistas.values())
for notas in analistas.values():
    for nota in notas:
        if nota not in quantidade_notas:
            quantidade_notas[nota] = 0
        quantidade_notas[nota] += 1
maior_idade = max(analistas.keys())
menor_idade = min(analistas.keys())

print(f"Total de respondentes: {quantidade_geral}")
for nota, quantidade in quantidade_notas.items():
    print(f"{nota}: {quantidade}")
print(f"O respondente mais velho possuía a idade: {maior_idade} anos e sua resposta foi: {analistas[maior_idade][0]}")
print(f"O respondente mais novo possuía a idade: {menor_idade} anos e sua resposta foi: {analistas[menor_idade][0]}")

