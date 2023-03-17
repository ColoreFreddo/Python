# Data una lista si vuole cercare tutte le ricorrenze di un elemento inserito in input. Tale ricerca deve essere effettuata utilizzando esclusivamente il metodo index e il metodo count della lista.
lista = [1, 3, 4, 5, 3, 3] 
elemento = 3
listaOUT=[]
for i in lista:
        listaOUT.append(lista.index(elemento))
        lista[lista.index(elemento)] = 9
print(listaOUT)
