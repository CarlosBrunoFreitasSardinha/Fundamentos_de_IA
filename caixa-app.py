# listaqq = [[4, 2], [5, 2], [7, 3], [9, 4], [9, 3], [9, 5], [6, 4]]
# print(sorted(listaqq, key=lambda c: (c[0],-c[1],)))

from CEF import *

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
            t = verificaTaxaVariabilidade(listaTop10)
            if t == 0:
                  for m in range(3):
                        i=randint(0,9)
                        listaTop10[i][0] = muda(listaTop10[i][0])
                  #CrossOver Ponto Unico
            elif t==1:
                  i=randint(0,9)
                  listaTop10[i][0] = muda(listaTop10[i][0])
            
            listaDeGenes = combina(listaTop10)#saida: [['10101010','11111111'],['10101010','00110011'],... ['11111111','10101010'],...]
            listaPopulacao = efetuaCruzamentoDois(listaDeGenes)#saida: [['10101111','10101111'],['10100011','00111010'],... ['11111010','11111010'],...]
      for individuo in listaPopulacao:
            individuo = calculaAptidaoMochila(individuo)#Calcula Aptidão de cada Cromossomo

      print("Geração {}".format(geracao))#Seleção
      listaTop10 = dezMenores(listaPopulacao)#saida na tela: [[['10001000',[0, 28]],['01000100',[0, 27]],...,['11001100',[1, 13]]]
      showEspecial(listaTop10)
      continuar = input("Deseja Continuar: ")