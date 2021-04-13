from CEF import *

listaDeGenes= []
listaPopulacao= []
listaTop10 = []
listaCombinacao = []
continuar = 's'
geracao=0


#CRIA POPULAÇÃO
listaDeGenes = criaListaDeGenes()
#Cria Lista de Genes com suas Aptdões Aleatórias: [['11001100',4.43],['10001000',0.54],...,['01000100',2.12]]
listaPopulacao = criaListaDeListas(listaDeGenes)
#######################################################################

while continuar == 's':
      geracao+=1
      if geracao>1:
            if verificaTaxaVariabilidade(listaTop10):
                  i=randint(0,9)
                  #seleciona os de melhores genes, com peso mais perto do limite e melhor benefício
                  listaTop10[i][0] = mutacao(listaTop10[i][0])#saida: [['11001100',[0, 28],['10001000',[1, 28]],...,['01000100',[4, 28]]]
            
            listaDeGenes = combina(listaTop10)#Efetua a combinação entre os melhores genes sem cruzar os genes com eles mesmos
            #saida: [['10101010','11111111'],['10101010','00110011'],... ['11111111','10101010'],...]
            listaPopulacao = efetuaCruzamento(listaDeGenes, 2)#Efetua o cruzamento dos genes selecionados
            #saida: [['10101111','10101111'],['10100011','00111010'],... ['11111010','11111010'],...]

      for individuo in listaPopulacao:
            individuo = calculaAptidaoCaixa(individuo)#Calcula Aptidão de cada Cromossomo

      print("Geração {}".format(geracao))#apresenta de qual geração se trata aqueles individuos
      listaTop10 = dezMaisAptos(listaPopulacao)#saida na tela: [[['10001000',[0, 28]],['01000100',[0, 27]],...,['11001100',[1, 13]]]
      showEspecial(listaTop10)
      continuar = input("Deseja Continuar: ")