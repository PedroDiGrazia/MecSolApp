print()
QtdApoios = int(input("Quantos apoios serão utilizados: "))
print()
print("!!!Considere os Apoios como:!!!")
print("-> Fixo = 1")
print("-> Movel = 2")
print("-> Engaste = 3")
print()
input("Aperte <Enter> para continuar!")

i = 0
n = 0
m = 0
Fixo = 'Fixo'
Movel = 'Movel'
Engaste = 'Engaste'

vetor = list(range(QtdApoios))
for i in range(QtdApoios):
    vetor[m]=10
    m=m+1
Apoio = list(range(QtdApoios))
print()
j=0
p=100
m=0
i=0
for i in range(0, QtdApoios):
    n = n + 1
    print(vetor)
    vetor[m] = int(input(f"Digite o numero do Apoio no ponto {n} (1,2,3): "))
    print(QtdApoios)
    print(vetor)
    if vetor[m] <1 or vetor[m] >3: 
        p=p+1
        for j in range(0,p):
            print()
            print("NUMERO INVALIDO! DIGITE NOVAMENTE")
            print(vetor)
            vetor[m] = int(input(f"Digite o numero do Apoio no ponto {n} (1,2,3): "))
            if vetor[m] >=1 and vetor[m]<=3:
                print(f"p:{p}")
                m=m+1
                break
            else:
                print(f"p2:{p}")
                print()
    else:
        m=m+1
print(vetor)
print()
n = 0
o = 0
m = 0
i = 0
for i in range(0, QtdApoios):
    if vetor[m] == 1:
        Apoio[o]=Fixo 
    elif vetor[m] == 2:
        Apoio[o] = Movel
    else:
        Apoio[o]=Engaste
    o = o+1
    m = m+1

print(Apoio)
o=0
m=0
for i in range(0, QtdApoios):
    n = n + 1
    print(f"O tipo do apoio no ponto {n} é: {Apoio[o]}")
    o = o + 1
print()
n = 0
m = 0
i = 0
j = 0
vetor2 = list(range(QtdApoios))
print("Origem = 0m")
for i in range(0, QtdApoios):
    n = n+1
    vetor2[j] = float(input(f"Qual é a distância em relação à origem do apoio {n}: "))
    j = j+1
print()

TamanhoBarra =  vetor2[-1] - vetor2[0]

print(f"O tamanho da barra é de: {TamanhoBarra}m")

QtdForcas= int(input("Quantas forças serão aplicadas: "))

print()
print("!!!Considere as Forças como:!!!")
print("-> Distribuida = 1")
print("-> Concentrada = 2")
print()
input("Aperte <Enter> para continuar!")

Forca = list(range(QtdForcas))
c=0
i=0
for i in range(0,QtdForcas): 
    TipoForca = int(input("Qual tipo de força sera aplicada: "))
    if TipoForca == 1:
        print("Força distribuida!")
        Forca[c]= 'Distribuida' 
    else:
        print("Força concentrada")
        Forca[c]= 'Concentrada' 
    c=c+1
print(Forca)
i=0
c=0
for i in range(0,QtdForcas):
    if Forca[c] == 'Concentrada':
        print()
        PosForcaC = float(input(f"Onde deseja aplicar a força {TamanhoBarra}: ")) 
        if PosForcaC >TamanhoBarra or PosForcaC <TamanhoBarra
        print()
        print("NUMERO INVALIDO, DIGITE NOVAMENTE!")
        PosForcaC = float(input(f"Onde deseja aplicar a força {TamanhoBarra}: ")) 
        
    else:
        print()
        print("Utilize um dos apoios como origem!")
        PosForcaD = float(input(f"Digite o intervalo da força em relação a origem até {TamanhoBarra}m: "))
        if PosForcaD > TamanhoBarra:
           PosForcaD = float(input("Digite Novamente: "))
    c=c+1
