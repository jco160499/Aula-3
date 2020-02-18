import random as rd 
import math as mt 
import statistics as sts 

contador = 0
lista = []

while contador <= 20:
    lista.append(rd.randrange(1,100))
    contador +=1

print ( 'O menor valor é:', min(lista))
print ('O maior valor é:', max (lista))
print( 'A média é:', sts.mean(lista))
print ('A mediana é:', sts.median(lista))
print ('A variância é:', sts.variance(lista))
