from random import randint, random

#função1 cria um gene aleatório de 8 cromossomos
def criaGeneAleatorio():
    return f'{randint(0,127):08b}'

#função2 cria lista de genes aleatorios
def criaListaDeGenes():
    listaItens = [criaGeneAleatorio() for x in range(100)]
    return listaItens

#função3 cria de fato uma cromossomo com um campo fitness aleatorio
def criaGeneComFitnessAleatorio(string):
    return [string, (randint(0,9)+round(random(), 2))]

#função4 cria uma popuçção de cromossomos
def criaListaDeListas(lista):
    listaItens = [criaGeneComFitnessAleatorio(x) for x in lista]
    return listaItens

#função7 o quão perto aquele gene chegou do peso maximo
def calculaPeso(numero):
    return numero > 25 and numero-25 or 25-numero
# função8 formula um fitness bidimensional, 
# onde os dois critérios serão usados para definir a eficacia de cada solução
def pesoBeneficoGene(numero):
    peso = 0
    ben = 0
    if numero[0] == '1':
        peso += 4
        ben  += 3
    if numero[1] == '1':
        peso += 5
        ben  += 8
    if numero[2] == '1':
        peso += 4
        ben  += 7
    if numero[3] == '1':
        peso += 7
        ben  += 3
    if numero[4] == '1':
        peso += 6
        ben  += 6
    if numero[5] == '1':
        peso += 5 
        ben  += 6
    if numero[6] == '1':
        peso += 3
        ben  += 5
    if numero[7] == '1':
        peso += 4
        ben  += 5
    return [calculaPeso(peso), ben]

#função8 é o conceito de seleção, dentre os que tiveram menor peso na caixa
# e maior beneficio
def dezMaisAptos(lista):
    return sorted(lista, key=lambda x : (x[1][0], -x[1][1]))[0:10]

#função9 conceito de mutação, aplicado na fração de 1/10
def mutacao(string):
    i = randint(0,7)
    newString = ''
    for x in range(len(string)):
        if i==x:
            if string[i] == '0':
                newString = newString +'1'
            else:
                newString = newString +'0'
        else:
            newString = newString+string[x]
    return newString

#função10 efetua a criação de um lista de genes que serão expostos ao processo 
# de cruzamento
def combina(lista):
    superLista = []
    for i in range(10):
        for j in range(10):
            if i!=j:
                superLista.append([lista[i][0], lista[j][0]])
    return superLista

#função11 efetua o cruzamento pelo conceito de ponto unico
def cruzamentoPontoUnico(stringA,stringB):
    return [stringA[0:4]+''+stringB[4:8], stringB[0:4]+''+stringA[4:8]]

#função12 efetua o cruzamento pelo conceito de ponto duplo
def cruzamentoPontoDuplo(stringA,stringB):
    return [stringA[0:2]+''+stringB[2:6]+''+stringA[6:8], stringB[0:2]+''+stringA[2:6]+''+stringB[6:8]]
############################################################################################################

#expõe um cromossomo a avaliação do seu fitness em todos os quesitos necessários
def calculaAptidaoCaixa(individuoN):
      individuoN[1] = pesoBeneficoGene(individuoN[0])
      return individuoN

#retorna se a taxa de variação do beneficio esta menor do que 1, para poder se aplicar mutação
def verificaTaxaVariabilidade(lista):
    return (lista[-1][1][1]-lista[0][1][1]) < 1

#recebe os genes que serão cruzados e qual tipo de cruzamento será efetuado
def efetuaCruzamento(lista, tipo):
      algumacoisa = []
      for combinacaoN in lista:
            if tipo ==1:
                algumacoisa.append(cruzamentoPontoUnico(combinacaoN[0], combinacaoN[1]))
            elif tipo==2:
                algumacoisa.append(cruzamentoPontoDuplo(combinacaoN[0], combinacaoN[1]))

      return algumacoisa

#apresenta uma lista de forma um tanto mais legivel, utilizada para testes e vizualização de saidas
def show(lista):#string.zfill(3)
    i=1
    for x in lista:
        print(f'{i:3d}', " - ", x)
        i+=1

#apresenta uma lista de forma a apresentar os itens contidos na caixa
def showEspecial(lista):#string.zfill(3)
    i=1
    for x in lista:
        print(f'{i:3d}', "-[",end='') 
        if(x[0][0]=='1'): print( x[0][0],"-P=4 HotDog|",end='') 
        if(x[0][1]=='1'): print(x[0][1], "-P=5 Chambari|",end='') 
        if(x[0][2]=='1'): print(x[0][2], "-P=4 Cuscuz|",end='') 
        if(x[0][3]=='1'): print(x[0][3], "-P=7 Guaraná|",end='')  
        if(x[0][4]=='1'): print(x[0][4], "-P=6 Hamburguer|",end='')  
        if(x[0][5]=='1'): print(x[0][5], "-P=5 Pizza|",end='') 
        if(x[0][6]=='1'): print(x[0][6], "-P=3 Sarapatel|",end='')  
        if(x[0][7]=='1'): print(x[0][7], "-P=4 Tapioca|",end='') 
        print(" => ",x[0]," FITNeSS = ", x[1])
        i+=1
