# Scrivere un programma python che rimuova gli elementi duplicati da una lista.

lista = [2, 4 ,5,6,5,5,2]
lista2 = []
for i in lista:
    if i not in lista2:
        lista2.append(i)
print(lista2)
print(lista)
