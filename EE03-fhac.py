import random

def aleatorio():
    
    i=0
    lista =[]
    while i<10000:
        numero = random.randint(0,100)
        lista.append(numero)
        i=i+1

    soma = 0
    j=0
    while j<len(lista):
        soma = soma + lista[j]
        j=j+1

    media = soma/10000

    return media
    

def mediana(n,x):
    i=0
    lista =[]
    while i<x:
        numero = random.randint(0,n)
        lista.append(numero)
        i=i+1

    sorted(lista)

    if (len(lista) % 2) == 1:
        return lista[len(lista)//2]
    else:
        return (lista[len(lista)//2] + lista[(len(lista)//2) + 1])/2
