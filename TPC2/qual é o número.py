# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 19:07:09 2021

@author: Brunamatos
"""
def qualéonúmero ():
    print ("Pense num número entre 1 e 100")
    min=0
    max=100
    b=1 #este b vai servir para pausar a função quando imprimir-mos que achamos o valor 
    c= min+ ((max-min)//2) #vai nos dar o novo valor, que serve para questionar o utilizador do programa
    f=0
    while b==1: # o ciclo while vai fazer com que volte a fazer a pergunta
        print("Esse número é igual,inferior ou superior a",c,"?") #coloco aqui porque nao posso chamar variaveis em input
        a=input(" ") #como nao podemos usar uma variavel dentro do input colocamos de fora
        if a=="igual":
            print ("O seu número é:",c)
            b=13 # quando escrevemso b=13 ele vai acabar com o ciclo
        else:
            if a=="superior":
                    min=c
                    c=min+int((1/2)*(max-min))
                    f=f+1
            elif a=="inferior":
                    max=c
                    c=max-int((1/2)*(max-min))
                    f=f+1
    print ("conseguiu resolver o códio em",f, "tentativas")
            
        
        

        
        
        
        
qualéonúmero()
    
        
            

  
        
    
