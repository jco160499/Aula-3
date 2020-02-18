import random as rd

contador = 0
lista = []

while contador <= 20:
    lista.append(rd.randrange(1,1000))
    contador +=1

print('Essa é a lista', lista)
print(max(lista))
print(min(lista))
