# Manifesto: Trabalho prático 4

### Autor:  Bruna Matos
### Identificador: TP4
### Título: Calculadora funções 
### Data de início: 2021-11-04
### Data do fim: 2021-11-10
### Supervisor:José Carlos Ramalho, https://www.di.uminho.pt/~jcr/thesup-v2.php

## _Resumo_

Neste trabalho foi realizada uma calculadora de fracões que nos permite calcular somas,diferenças, produtos e razões. Além disso também foi incorporada a função de criar uma lista aleatória e calcular a soma de tidos os seus elementos, usando o import random. Para que a calculadora funcione de forma adequada foram usadas algumas formas matemáticas de forma a facilitar também os cálculos. A função valor0 vai tornar a função de encontrar o máximo e o mínimo de cada lista mais simples uma vez que fração anteriormente representada num tuplo, é redusida a um número real.


## Função Calculadora Frações



```python

def menu():
    print("""
    Gestão de Frações e Listas de Frações: 
(1) Criar uma fração;
(2) Simplificar uma fração;
(3) Somar duas frações;
(4) Subtrair duas frações;
(5) Multiplicar duas frações;
(6) Dividir duas frações;
(7) Gerar lista de n frações;
(8) Somar as frações de uma lista;
(9) Qual a maior fração da lista;
(10) Qual a menor fração da lista;
(0) Sair""")

def criarFracao():
    numerador = int(input(("Insira o numerador da fração: ")))
    denominador = int(input(("Insira o denominador da fração: ")))
    return (numerador, denominador)


def VerFracao (f):
    num, denom=f
    return (str(num)+"/"+str(denom))

    
def mdc(a, b):
    if a < b:
        return mdc(b, a%b)
    elif a % b == 0:
        return b
    else:
        return mdc(a, a%b)

    
def simplificarFracao(f):
    num, denom = f
    a = mdc(num,denom)
    return(int(num/a),int(denom/a))


def somarFracao(f1, f2):
    denom = f1[1] * f2[1]
    a = f1[0] * f2[1]
    b = f2[0] * f1[1]
    num = a + b
    return (VerFracao(simplificarFracao((num, denom))))


def subtraiFracao(f1, f2):
    denom = f1[1] * f2[1]
    a = f1[0] * f2[1]
    b = f2[0] * f1[1]
    num = a-b
    return (VerFracao(simplificarFracao((num, denom))))


def multiplicaFracao(f1, f2):
    num = f1[0] * f2[0]
    denom = f1[1] * f2[1]
    return (VerFracao(simplificarFracao((num, denom))))


def divideFracao(f1, f2):
    num = f1[0] * f2[1]
    denom = f1[1] * f2[0]
    return (VerFracao(simplificarFracao((num, denom))))


def listaAleaFracao():
    L = []
    from random import randint 
    n = int(input("Introduza o número de elementos da lista:"))
    for i in range(n):
        elem = (randint(1, 100), randint(1, 100))
        L.append(elem)
    return L


def somarLista(L):    
    ac = (0,1)  
    for elem in L:
         ac = somarFracao(ac, elem)
    return(ac)

    
def valorFrac(L):
    valor = []
    for i in range(len(L)):
        res = L[i][0]/L[i][1]
        valor.append(res)
    return valor
    
    
def maiorLista(valor):
    i = 0
    maxi = valor[0]
    for i in range (len(valor)-1):
        if valor[i+1] > maxi:
            maxi = valor[i+1]
            i = i+1
        elif maxi > valor[i+1]:
             i = i+1
    return maxi


def menorLista(valor):
    i = 0
    mini = valor[0]
    for i in range(len(valor)-1):
        if mini > valor[i+1]:
            mini = valor[i+1]
            i = i+1
        elif mini < valor[i+1]:
            i = i+1
    return mini

def operacoes():
    op = "1"
    menu ()
    print ("Seja Bem-vindo à operadora de frações!")
    while (op != "0"):
        op = input("Qual é a sua opção?")
        if op == "1":
            frac = criarFracao()
            print (frac)
            print ("            ")
        elif op == "2":
            try:
                frac = simplificarFracao(frac)
                print(frac)
                print("      ")
            except:
                print ("Ainda não há frações criadas.")
                print ("                  ")
        elif op =="3":
            try:
                f1 = criarFracao()
                f2 = criarFracao()
                frac = somarFracao(f1, f2) 
                print(frac)
                print("      ")
            except:
                print ("Ainda não há frações criadas.")
                print ("                  ")
        elif op =="4":
            try:
                f1 = criarFracao()
                f2 = criarFracao()
                frac = subtraiFracao(f1, f2)
                print(frac)
            except:
                print ("Ainda não há frações criadas.")
                print ("                  ")
        elif op =="5":
            try:
                f1 = criarFracao()
                f2 = criarFracao()
                frac = multiplicaFracao(f1, f2)
                print (frac)
                print("      ")
            except:
                print ("Ainda não há frações criadas.")
                print("            ")
            
        elif op =="6":
            try:
                f1 = criarFracao()
                f2 = criarFracao()
                frac = divideFracao(f1, f2)
                print (frac)
            except:
                print ("Ainda não há frações criadas.")
                print("            ")
        elif op =="7":
                lis = listaAleaFracao()
                print (lis)
                print("      ")
        elif op =="8":
            try:
                lis = somarLista(lis)
                print (lis)
                print("      ")
            except:
                print ("Ainda não há nenhuma lista criada.")
                print("            ")
        elif op =="9":
            try:
                valor1 = valorFrac(lis)
                lis1 = maiorLista(valor1)
                print (lis1)
                print("      ")
            except:
                print ("Ainda não há nenhuma lista criada.")
                print("            ")
        elif op =="10":
            try:
                valor1 = valorFrac(lis)
                lis2 = menorLista(valor1)
                print (lis2)
                print("      ")
            except:
                print ("Ainda não há nenhuma lista criada.")
                print("  ")   
        elif op == "0":
            print("Até à próxima!")
            print ("            ")
        else:
            print("Opção inválida!")
            print ("             ")
print(operacoes ())
```
