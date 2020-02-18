import random as rd
qtd_num = int(input('Digite quantidade de números'))
contador = 0
lista = []

while contador <= qtd_num:
    lista.append(rd.randrange(1,100))
    contador +=1

print('Essa é a lista', lista)
print(max(lista))
print(min(lista))