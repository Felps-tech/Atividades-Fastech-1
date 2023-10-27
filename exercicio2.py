AM,BM,CM,AV,BV,CV,AN,BN,CN = 0,0,0,0,0,0,0,0,0

for i in range(3):
    elevador = input("Qual elevador você utiliza com mais frequência? (A, B, C): ").upper()
    periodo = input("Qual período você utiliza o elevador? (M=Matutino, V=Vespertino, N=Noturno): ").upper()

    if elevador == "A":
        if periodo == "M":
            AM += 1
        elif periodo == "V":
            AV += 1
        elif periodo == "N":
            AN += 1
    elif elevador == "B":
        if periodo == "M":
            BM += 1
        elif periodo == "V":
            BV += 1
        elif periodo == "N":
            BN += 1
    elif elevador == "C":
        if periodo == "M":
            CM += 1
        elif periodo == "V":
            CV += 1
        elif periodo == "N":
            CN += 1

elevador_mais_utilizado = max(
    (AM, "A", "Matutino"),
    (AV, "A", "Vespertino"),
    (AN, "A", "Noturno"),
    (BM, "B", "Matutino"),
    (BV, "B", "Vespertino"),
    (BN, "B", "Noturno"),
    (CM, "C", "Matutino"),
    (CV, "C", "Vespertino"),
    (CN, "C", "Noturno"),
    key=lambda x: x[0]
)
periodo_mais_utilizado = max(
    (AM+BM+CM,"Matutino"),
    (AV+BV+CV,"Vespertino"),
    (AN+BN+CN,"Noturno"),
    key=lambda x: x[0]
)

periodo_menos_utilizado = min(
    (AM+BM+CM,"Matutino"),
    (AV+BV+CV,"Vespertino"),
    (AN+BN+CN,"Noturno"),
    key=lambda x: x[0]
)

print(f"O elevador mais utilizado é o elevador {elevador_mais_utilizado[1]} no período {elevador_mais_utilizado[2]}.")
print(f"O periodo mais utilizado é o {periodo_mais_utilizado[1]}, o periodo menos utilizado é o {periodo_menos_utilizado[1]}.")
