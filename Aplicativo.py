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
Apoio = list(range(QtdApoios))
print()
j=0
for i in range(0, QtdApoios):
    n = n + 1
    vetor[m] = int(input(f"Digite o numero do Apoio no ponto {n} (1,2,3): "))
    print(QtdApoios)
    for j in range(0, QtdApoios):
        if vetor[m] <1 and vetor[m] >3: 
            print()
            print("NUMERO INVALIDO! DIGITE NOVAMENTE")
            print()
            vetor[m] = int(input(f"Digite o numero do Apoio no ponto {n} (1,2,3): "))
            m = m + 1
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
    vetor2[j] = int(input(f"Qual é a distância em relação à origem do apoio {n}: "))
    j = j+1
print()

TamanhoBarra =  vetor2[-1] - vetor2[0]

print(f"O tamanho da barra é de: {TamanhoBarra}m")

QtdForcas= int(input("Quantas forças serão aplicadas: "))

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
