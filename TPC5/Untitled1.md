# Manifesto Trabalho Prático 5

 __Autor__ : Bruna Matos, A95827
 
 __Identificador__ : TP5
 
 __Título__ : Função de polinómios
 
 __Data início__: 13/11/2021
 
 __Data de fim__: 17/11/2021
 
 __Supervisor__:José Carlos Ramalho, https://www.di.uminho.pt/~jcr/thesup-v2.php
 
 Este programa tem como objetivo realizar as mai difersas funções relacionadas com polinómios. Calcula o valor de polnómios, determina  seu grau, simplifica-os e até nos apresenta uma espéci de tabea com os resultados do polinómo escolhido dede x=0 ate ao x establicido pelo utilizador.
 O utilizador pode submeter o seu polinómio de forma total mas a qualquer momento pode inserir novos termos e assim formar um novo polinómio.

  ### Código tp5


```python

def criarTermo(coef,exp):
    return (coef,exp)

def criarPolinomio():
    return[]

def criarpoltotal():
    ntermos=int(input("Insira quantos termos deseja introduzir:"))
    p=criarPolinomio()
    for i in range (ntermos):
        coef=int(input("Introduza o coeficiente que pretende:"))
        exp=int(input("Introduza o expoente do coeficiente anterior:"))
        t=criarTermo(coef, exp)
        inserirTermo(p,t)
    return p

def inserirTermo(p,t):
    return p.append(t)

def verTermo(t):
    c,e=t
    if e==0:
        return (str(c))
    elif c==1:
        return (str(e))
    else:
        return (str(c)+"x"+str(e))
    
def verPolinómio(p):
    politexto=" "
    if len (p)!=0:
        politexto=verTermo(p[0])
        for i in range (1, len (p)):
            if p[i][0]>=0:
                politexto=politexto + "+" + verTermo(p[i])
            else:
                politexto=politexto + verTermo(p[i])
        return (politexto)
        
def grauPol(p):
    grau=p[0][1]
    for i in range (1,len (p)):
        if p [i][1]>grau:
            grau=p[i][1]
    return grau

def calculoPolinomio(p,x):
     valor=0
     for (c,e) in p:
         valor=valor + c*x**e
     return valor


    
def criarTabela(p):
    linhas = int(input(" Introduza o número de linhas que deseja que a tabela tenha:"))
    print("x" + "::" + verPolinómio(p))
    for i in range (0, linhas):
        print(str(i) + "->" + str(calculoPolinomio(p,i)))
  
               
def derivadaPolinomio(p):
    derivada=[]
    for (c,e) in p:
        if e!=0:
            derivada.append((c*e,e-1))
        return derivada


def ordenarExp(p):
    
    for i in range(len(p)):
        trocas=0
        i=0
        while i<(len(p)-1):
            if int(p[i][1]) > int(p[i+1][1]):
                p[i],p[i+1] = p[i+1],p[i]
                trocas=1
            i=i+1
        if trocas== 0:
            return p

def simplificar(p):
    i=0
    while i<len(p)-1:
        if p[i][1]==p[i+1][1]:
            valor=p[i][0]+p[i+1][0]
            termo=criarTermo(valor,p[i][1])
            inserirTermo(p,termo)
            p.pop(i)
            p.pop(i)
            p=ordenarExp(p)
            i=0
        else:
            i=i+1
    return p
    

def menu():
    op = input("""Qual é a sua opção? 
(1) Criar um polinómio;
(2) Criar Tabela;
(3) Descobrir grau de um polinómio
(4) Calcular polinómio num ponto; 
(5) Calcular derivada; 
(6) Simplificar polinómio;
(0) Sair """)   

      
    if op=="1":
        resultado = verPolinómio(criarpoltotal())
        print( resultado )
        menu()
    elif op=="2":
       p=criarpoltotal()
       criarTabela(p)
       menu()
    elif op=="3":
        resultado = grauPol(criarpoltotal())
        print( "O grau do polinómio que inseriu é: ", resultado )
        menu() 
    elif op=="4":
        resultado = calculoPolinomio(criarpoltotal())
        print( "O valor da ordenada correspondente à coordenada que inseriu é: ", resultado)
        menu()
    elif op =="5":
          try:
              derivada = derivadaPolinomio(p)
              ver = verPolinómio(derivada)
              print(ver)
              print("      ")
          except:
              print ("Ainda não foi criado nenhum polinómio.")
              print ("                  ")
    elif op=="6":
         resultado = verPolinómio(simplificar(ordenarExp(criarpoltotal())))
         print(resultado)
         menu()               
    elif op == "0":
         print("Até à próxima!")
         print ("            ")
    else:
         print("Opção inválida!")
         print ("             ")
              
         
            
menu()
```
