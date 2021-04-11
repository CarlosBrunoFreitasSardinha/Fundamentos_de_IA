from todasasfuncoes import *

def calculaAptidaoRaiz(individuoN):
      decimal = converteBinarioReal(individuoN[0])
      individuoN[1] = subtrai(decimal)
      return individuoN

def verificaTaxaVariabilidade(lista):
      return (lista[-1][1]-lista[0][1]) < 1

def efetuaCruzamento(lista):
      algumacoisa = []
      for combinacaoN in lista:
            algumacoisa.append(cruzaUm(combinacaoN[0], combinacaoN[1]))
      return algumacoisa

listaDeGenes= []
listaPopulacao= []
listaTop10 = []
listaCombinacao = []
continuar = 's'
geracao=0


#CRIA POPULAÇÃO
listaDeGenes = criaListaDeStrings()
#Cria Lista de Genes com suas Aptdões Aleatórias: [['11001100',4.43],['10001000',0.54],...,['01000100',2.12]]
listaPopulacao = criaListaDeListas(listaDeGenes)
#######################################################################

while continuar == 's':
      geracao+=1
      if geracao>1:
            if verificaTaxaVariabilidade(listaTop10):
                  i=randint(0,9)
                  listaTop10[i][0] = muda(listaTop10[i][0])
                  #CrossOver Ponto Unico
            listaDeGenes = combina(listaTop10)#saida: [['10101010','11111111'],['10101010','00110011'],... ['11111111','10101010'],...]
            listaPopulacao = efetuaCruzamento(listaDeGenes)#saida: [['10101111','10101111'],['10100011','00111010'],... ['11111010','11111010'],...]
      for individuo in listaPopulacao:
            individuo = calculaAptidaoRaiz(individuo)#Calcula Aptidão de cada Cromossomo

      print("Geração {}".format(geracao))#Seleção
      listaTop10 = dezMenores(listaPopulacao)#saida na tela: [[['10001000',0.54],['01000100',2.12],...,['11001100',4.43]]
      showEspecial(listaTop10)
      continuar = input("Deseja Continuar: ")