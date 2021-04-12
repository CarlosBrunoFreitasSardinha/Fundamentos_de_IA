from random import randint, random

#função3
def criaString():
    return f'{randint(0,127):07b}'

#função4
def criaListaDeStrings():
    lista_vazia = [criaString() for x in range(100)]
    return lista_vazia

#função5
def binarioSeguidoDeReal(string):
    return [string, (randint(0,9)+round(random(), 2))]

#função6
def criaListaDeListas(lista):
    lista_vazia = [binarioSeguidoDeReal(x) for x in lista]
    return lista_vazia

#função7 FITNES
def subtrai(numero):
    return numero > 22 and numero-22 or 22-numero

def pesoCromossomo(numero):
    peso = 0
    ben = 0
    if numero[0] == '1':
        peso += 7
        ben  += 5
    if numero[1] == '1':
        peso += 8
        ben  += 8
    if numero[2] == '1':
        peso += 4
        ben  += 3
    if numero[3] == '1':
        peso += 10
        ben  += 2
    if numero[4] == '1':
        peso += 4
        ben  += 7
    if numero[5] == '1':
        peso += 6 
        ben  += 9
    if numero[6] == '1':
        peso += 4
        ben  += 4
    return [subtrai(peso), ben]

#função8
def dezMenores(lista):
    return sorted(lista, key=lambda x : (x[1][0], -x[1][1]))[0:10]

#função9
def muda(string):
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

#função10
def combina(lista):
    superLista = []
    for i in range(10):
        for j in range(10):
            if i!=j:
                superLista.append([lista[i][0], lista[j][0]])
    return superLista

#função11
def cruzaUm(stringA,stringB):
    return [stringA[0:4]+''+stringB[4:8], stringB[0:4]+''+stringA[4:8]]

#função12
def cruzaDois(stringA,stringB):
    return [stringA[0:2]+''+stringB[2:6]+''+stringA[6:8], stringB[0:2]+''+stringA[2:6]+''+stringB[6:8]]
####################################


def calculaAptidaoMochila(individuoN):
      individuoN[1] = pesoCromossomo(individuoN[0])
      return individuoN

def verificaTaxaVariabilidade(lista):
      return (lista[-1][1][0]-lista[0][1][0]) < 1

def efetuaCruzamentoUm(lista):
      algumacoisa = []
      for combinacaoN in lista:
            algumacoisa.append(cruzaUm(combinacaoN[0], combinacaoN[1]))
      return algumacoisa
def efetuaCruzamentoDois(lista):
      algumacoisa = []
      for combinacaoN in lista:
            algumacoisa.append(cruzaDois(combinacaoN[0], combinacaoN[1]))
      return algumacoisa

def show(lista):#string.zfill(3)
    i=1
    for x in lista:
        print(f'{i:3d}', " - ", x)
        i+=1
def showEspecial(lista):#string.zfill(3)
    i=1
    for x in lista:
        print(f'{i:3d}', " - [", x[0][0], " - P=7   B=5 |", x[0][1], " - P=8   B=8 |", x[0][2], " - P=4   B=3 |", x[0][3], " - P=10   B=2 |", x[0][4], " - P=4   B=7 |", x[0][5], " - P=6   B=9 |", x[0][6], " - P=4   B=4 | Cromo: ",x[0]," FITNSS = ", x[1])
        i+=1
