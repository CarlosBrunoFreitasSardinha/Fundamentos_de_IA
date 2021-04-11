'''
Faça um programa que 

1.	Gere 100 strings compostas por oito valores zeros ou uns e coloque em uma lista
2.	Crie uma lista com cada string sendo colocada junto com sua avaliação, em um formato [string, avaliação]
3.	Para a string ser avaliada, deve converter cada uma destas strings em um valor decimal fracionário: os dois primeiros equivalem à parte inteira e os demais equivalem a parte fracionária. Após, avalia cada um destes valores em relação ao número 2: cada um deles deve ser elevado ao quadrado e subtraído do número 2. Esta diferença, em módulo, é a avaliação.
4.	Imprima cada string, seu valor em número real e sua avaliação
5.	Verifique qual string tem menor avaliação, imprima-a seguido de seu valor em real
a.	Se esse valor (avaliação) for muito próximo de zero, para a execução
6.	As 10 strings com menor valor de avaliação devem ser separadas e, duas a duas, devem gerar duas novas strings (as duas novas devem ser compostas pela metade inicial de uma com a metade final da outra e vice-versa). Ou seja, vc está fazendo um arranjo simples que gerará 90 novas strings que devem ser colocadas em uma lista. Escolha dez strings aleatórias, modifique-as alterando um de seus valores, e acrescente-as na lista, totalizando 100 strings na nova lista.
7.	Refaça a partir do passo 2 com a nova lista até chegar a uma string com avaliação muito próxima de zero.
Apresente o valor desta string em binário e em decimal fracionário.
'''
from random import randint, random

#função1
def converteBinarioReal(valor):
    return int(valor[0:2], 2)+(int(valor[2:], 2)/100)

#função2
def converteRealBinario(numero):
    aux = int(round(numero, 0))
    numero= int(round((numero-aux)*100, 0 ))
    return f'{aux:2b}'+ f'{numero:06b}'

#função3
def criaString():
    return f'{randint(0,255):08b}'

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

#função7
def subtrai(numero):
    quad = numero*numero
    return quad > 2 and round(quad-2,2) or round(2 - quad, 2)

#função8
def dezMenores(lista):
    return sorted(lista, key=lambda x : x[1])[0:10]

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

def show(lista):#string.zfill(3)
    i=1
    for x in lista:
        print(f'{i:3d}', " - ", x)
        i+=1
def showEspecial(lista):#string.zfill(3)
    i=1
    for x in lista:
        print(f'{i:3d}', " - [", converteBinarioReal(x[0]), " - ", x[1])
        i+=1
'''
ListaTeste_1= []
ListaTeste_2= []
ListaTop10 = []
ListaCombinacao = []

print("Função 1")
print("O valor Real é ", converteBinarioReal('11001100'))
# saida na tela: 3.12
print("Função 2")
print (converteRealBinario(3.12))
#saida na tela: 11001100
print("Função 3")
print(criaString())
#saida na tela: 11001100
ListaTeste_1 = criaListaDeStrings()
print("Função 4")
show(ListaTeste_1)
#saida na tela: ['10101101','10110101','01101010',...,'10101010']
print("Função 5")
print(binarioSeguidoDeReal('11001100'))
#saida na tela: ['11001100',2.02]
print("Função 6")
ListaTeste_2 = criaListaDeListas(ListaTeste_1)
show(ListaTeste_2)
#saida na tela: [['11001100',4.43],['10001000',0.54],...,['01000100',2.12]]
print("Função 7")
print(subtrai(1.2))#saida na tela: 0.56
print(subtrai(2.2))#saida na tela: 2.84
print("Função 8")
ListaTop10 = dezMenores(ListaTeste_2)
show(ListaTop10)
#saida na tela: [[['10001000',0.54],['01000100',2.12],...,['11001100',4.43]]
print("Função 9")
print('10110110')
print(muda('10110110'))
#saida na tela: 11110110
print('10110110')
print(muda('10110110'))
#saida na tela: 00110110
print("Função 10")
ListaCombinacao = combina(ListaTop10)
show(ListaCombinacao)
#saida na tela: [['10101010','11111111'],['10101010','00110011'],... ['11111111','10101010'],...]
print("Função 11")
print(cruzaUm('10110100','11001000'))
#saida na tela: ['10111000','11000100']
print("Função 12")
print(cruzaDois('10110100','11001000'))
#saida na tela: ['10001000','11110100']
'''