# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 16:31:11 2021

@author: bruna
"""

import os
print(os.getcwd())
#BDAlunos=[Alunos]
#Aluno={id:"...", nome:"...", curso:"...", tpc:[int]}

#1exercicio
# Leitura/carregamento da informação do ficheiro#
def lerDataset(fnome):
    bd=[]
    f=open(fnome,encoding="utf-8")
    f.readline()#Vai ler já a primeira linha de forma a que quando entrar no ciclo de for já esteje a ler a partir da mesma
    for linha in f: #Já vai iterar na segunda linha
        novaLinha= linha.replace("\n","") #Tirar o "\n" de maneira universal
        campos=novaLinha.split(",")
        aluno={}
        aluno["id"]=campos[0]
        aluno["nome"]=campos[1]
        aluno["curso"]=campos[2]
        listaTPC=[]
        for tpc in campos[3:]: #Lista de inteiros
            listaTPC.append(int(tpc))
        aluno["tpc"]=listaTPC #do 3º índice até ao fim
        bd.append(aluno)
    return bd
BDalunos= lerDataset("alunos.csv")
print(BDalunos)

#Listagem (exercício 2)
#Especifica uma função que faça a listagem no monitor dos vários registos de informação. Tenta dar a forma duma tabela em que as colunas têm todas a mesma dimensão.

# Listagem da informação
def listarDataset(bd):
    print("  id   |    nome    |    curso    |     tpcs")
    print("---------------------------------------------")
    for a in bd:
        print(a["id"] + "|" + a["nome"] + "|" + a["curso"] + "|" + str(a["tpc"]))


#listarDataset(BDalunos)
#Consulta de um registo (exercício 3)
#Especifica uma função que, dado o id de um aluno, coloca a sua informação no monitor. Para além disso, indica também a média dos TPC realizados.

def consultarDataset(bd, id):
    for a in bd:
        if (str(id)==a["id"].replace('"','')):
            return(a["id"]+"|"+a["nome"]+"|"+a["curso"]
                 +"|"+str(sum(a["tpc"])/len(a["tpc"])))
idaluno=str(input("Introduza o Id do aluno:"))
print(consultarDataset(BDalunos,idaluno))

#Top 10 (exercício 4)
#Especifica um função que dá como resultado uma lista com os alunos com as 10 médias mais altas: id, nome, curso, média.

def top10(bd):
    listaMedia=[]
    for a in bd:
        a["tpc"]= sum(a["tpc"])/len(a["tpc"])
        listaMedia.append(a["tpc"])
        listaMedia.sort()
        listaMedia.reverse()
    n=0
    while(n<10):
        for a in bd:
            if listaMedia[n]==a["tpc"] and n<10:
                n=n+1
                print(a["id"] + "|" + a["nome"] + "|" + a["curso"] + "|" + str(a["tpc"]))              
top10(lerDataset("alunos.csv"))

#Distribuição por curso (exercício 5)
#Especifica uma função que dá como resultado uma lista de pares indicando quantos alunos há em cada curso.

def distribPorCurso(bd): #Os dicionários premitem tratar os dados em várias situações
    distribuicao={}
    for a in bd:
        if(a['curso'] in distribuicao.keys()):
            distribuicao[a['curso']]+=1
        else:
            distribuicao[a['curso']]=1
    return distribuicao
mydistrib = distribPorCurso(BDalunos)
print(mydistrib)

#Distribuição por médias (exercício 6)
#Especifica uma função que dá como resultado uma lista de pares, média e número de alunos com essa média (considera o valor inteiro da média).

import collections
def distribPorMedia(bd):
    media={}
    for a in bd:
        medias=int(sum(a["tpc"])/len(a["tpc"]))
        if(medias in media.keys()):
            media[medias]+=1
        else:
            media[medias]=1
    result = collections.OrderedDict(sorted(media.items()))
    media=dict(result)
    return media
mydistribmed=distribPorMedia(BDalunos)
print(mydistribmed)


#Gráficos
#Gráfico da distribuição por curso (exercício 7)
#Especifica uma função que faz o plot dum gráfico com a distribuição de alunos por curso.

import matplotlib.pyplot as plt
def plotDistribPorCurso(distrib):
    cursos = distrib.keys()
    nAlunos = distrib.values()
    plt.xlabel("Cursos")
    plt.ylabel("Nº de alunos")
    plt.title("Distribuição por curso:")
    plt.bar(cursos,nAlunos, color=["pink", "red"])
plotDistribPorCurso(distribPorCurso(lerDataset("alunos.csv")))

#Gráfico da distribuição por média (exercício 8)
#Especifica uma função que faz o plot dum gráfico com a distribuição de alunos por média.

def plotDistribPorMedia(medias):
    import matplotlib.pyplot as plt
 

    left = [1, 2, 3, 4,5,6,7,8,9,10]
 
    height = [mydistribmed[9],mydistribmed[10] ,mydistribmed[11],mydistribmed[12],
              mydistribmed[13],mydistribmed[14],mydistribmed[15],mydistribmed[16],mydistribmed[17],mydistribmed[18]]
 
    tick_label = [9,10,11,12,13,14,15,16,17,18]

    plt.bar(left, height, tick_label = tick_label, #Tá a dar o nome as barras
            width = 0.8, color = ['orange', 'gold']) #largura da barra e cor delas
 
   
    plt.xlabel('Média')

    plt.ylabel('Nº de alunos')
 
    plt.title('Distribuição de alunos por Média')
 
    plt.show()
plotDistribPorMedia(mydistribmed)
