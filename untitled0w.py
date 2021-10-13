# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 15:57:05 2021

@author: a3546
"""
import random
def jogofosforos ():
    n=21
    x=input("Quem quer jogar primeiro? Computador(c) ou o Jogador(j)?")
    if (x=="j"):
        while (n>1):
            jogada=int(input("Quantos fósforos pretende retirar de 1 a 4 inclusive? "))
            if (jogada>=1 and jogada<=4):
                n=n-jogada
                if jogada==1:
                    n=n-4
                    print("Restam",n, "fósforos!")
                if jogada==2:
                   n=n-3
                   print("Restam",n, "fósforos!")
                if jogada==3:
                    n=n-2
                    print("Restam",n, "fósforos!")
                if jogada==4:
                    n=n-1
                    print("Restam",n, "fósforos!")
            else:
                    print("Erro!!")
            if n==1:
                print ("O computador ganhou!")
    if x=="c":
        jogadacomputador=random.randint(1,4)
        print("O computador retirou", jogadacomputador,"fósforos")
        n=n-jogadacomputador
        print ("Restam",n,"fósforos após a jogada do computador")
        while n>1:
            x=int(input("Quantos fósforos pretende retirar de 1 a 4 inclusive? "))
            if x<=4 and x>=1:
                n=n-x
                print ("restam",n,"fósforos")
                if n==1:
                    print("o jogador ganhou!Parabéns!")
                if n==2:
                    jogadacomputador=1
                    n=n-1
                    print("A jogada do computador é retirar", jogadacomputador,"fósforos")
                    print("restam",n,"fósforos, o computador ganhou!")
                if n==3:
                    jogadacomputador=2
                    n=n-2
                    print("A jogada do computador é retirar", jogadacomputador,"fósforos")
                    print("restam",n,"fósforos, o computador ganhou!")
                if n==4:
                    jogadacomputador=3
                    n=n-3
                    print("A jogada do computador é retirar", jogadacomputador,"fósforos")
                    print("restam",n,"fósforos, o computador ganhou!")
                if n==5:
                    jogadacomputador=4
                    n=n-4
                    print("A jogada do computador é retirar", jogadacomputador,"fósforos")
                    print("restam",n,"fósforos, o computador ganhou!")
                if n==6:
                    jogadacomputador=random.randint(1,4)
                    n=n-jogadacomputador
                    print("A jogada do computador é retirar", jogadacomputador,"fósforos")
                    print("restam",n,"fósforos")
                if n==7:  
                     jogadacomputador=1
                     n=n-jogadacomputador
                     print("A jogada do computador é retirar", jogadacomputador,"fósforos")
                     print("restam",n,"fósforos")
                if n==8 :
                    jogadacomputador=2
                    n=n-jogadacomputador
                    print("A jogada do computador é retirar", jogadacomputador,"fósforos")
                    print("restam",n,"fósforos")
                if n==9 :
                    jogadacomputador=3
                    n=n-jogadacomputador
                    print("A jogada do computador é retirar", jogadacomputador,"fósforos")
                    print("restam",n,"fósforos")
                if n==10 :
                    jogadacomputador=4
                    n=n-jogadacomputador
                    print("A jogada do computador é retirar", jogadacomputador,"fósforos")
                    print("restam",n,"fósforos")
                if n==11 :
                    jogadacomputador=random.randint(1,4)
                    n=n-jogadacomputador
                    print("A jogada do computador é retirar", jogadacomputador,"fósforos")
                    print("restam",n,"fósforos")
                if n==12 :  
                    jogadacomputador=1
                    n=n-jogadacomputador
                    print("A jogada do computador é retirar", jogadacomputador,"fósforos")
                    print("restam",n,"fósforos")
                if n==13:
                   jogadacomputador=2
                   n=n-jogadacomputador
                   print("A jogada do computador é retirar", jogadacomputador,"fósforos")
                   print("restam",n,"fósforos")
                if n==14:
                   jogadacomputador=3
                   n=n-jogadacomputador
                   print("A jogada do computador é retirar", jogadacomputador,"fósforos")
                   print("restam",n,"fósforos")
                if n==15 :
                   jogadacomputador=4
                   n=n-jogadacomputador
                   print("A jogada do computador é retirar", jogadacomputador,"fósforos")
                   print("restam",n,"fósforos")
                if n==16 :
                   jogadacomputador=random.randint(1,4)
                   n=n-jogadacomputador
                   print("A jogada do computador é retirar", jogadacomputador,"fósforos")
                   print("restam",n,"fósforos")
                if n==17 :  
                    jogadacomputador=1
                    n=n-jogadacomputador
                    print("A jogada do computador é retirar", jogadacomputador,"fósforos")
                    print("restam",n,"fósforos")
                if n==18 :
                   jogadacomputador=2
                   n=n-jogadacomputador
                   print("A jogada do computador é retirar", jogadacomputador,"fósforos")
                   print("restam",n,"fósforos")
                if n==19 :
                   jogadacomputador=3
                   n=n-jogadacomputador
                   print("A jogada do computador é retirar", jogadacomputador,"fósforos")
                   print("restam",n,"fósforos")
                if n==20 :
                   jogadacomputador=4
                   n=n-jogadacomputador
                   print("A jogada do computador é retirar", jogadacomputador,"fósforos")
                   print("restam",n,"fósforos")
                
            else:
              print("Erro!")
                    
                    
                    
                    
                    
                
                
jogofosforos ()

                