quant = int(input("Informe a idade de pessoas para o experimento "))
X,Y,Z,M,F,P,NP,XS,YS,ZS,MS,FS,PS,NPS,i = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
def calculo(x,y):
    if x > 0:
        x = (y/x) * 100
        print(f"{x:.2f}% Ganhar {100 - x:.2f}% Perder ")
    else:
        print("Não teve ")
def calcular(input,x,quant):
    if input == x :
        return quant + 1 
    return quant
def calc_ganhar(input,x,ganha,quantS):
    if input == x  and ganha == "S":
        return quantS + 1
    return quantS 
while i < quant: 
    geracao = str(input("Informe sua geracao. (X, Y, Z) ")).upper()
    sexo = str(input("Informe seu sexo. (M, F) ")).upper()
    pratica = str(input("Pratica ou Praticou futebol? (S, N) ")).upper()
    ganhar = str(input("O Brasil vai ganhar em 2026? (S, N) ")).upper()
    X = calcular(geracao,"X",X)
    Y = calcular(geracao,"Y",Y)
    Z = calcular(geracao,"Z",Z)
    M = calcular(sexo,"M",M)
    F = calcular(sexo,"F",F)
    P = calcular(pratica,"S",P)
    NP = calcular(pratica,"N",NP)
    XS = calc_ganhar(geracao,"X",ganhar,XS)
    YS = calc_ganhar(geracao,"Y",ganhar,YS)
    ZS = calc_ganhar(geracao,"Z",ganhar,ZS)
    MS = calc_ganhar(sexo,"M",ganhar,MS)
    FS = calc_ganhar(sexo,"F",ganhar,FS)
    PS = calc_ganhar(pratica,"S",ganhar,PS)
    NPS = calc_ganhar(pratica,"N",ganhar,NPS)
    i += 1 
print("Geração X :")
calculo(X,XS)
print("Geração Y :")
calculo(Y,YS)
print("Geração Z :")
calculo(Z,ZS)
print("Sexo masculino :")
calculo(M,MS)
print("Sexo feminino :")
calculo(F,FS)
print("Pratica futebol :")
calculo(P,PS)
print("Não Pratica futebol :")
calculo(NP,NPS)
