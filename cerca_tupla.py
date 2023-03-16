# Scrivere un programma per contare gli elementi in una lista finché non si incontra un elemento di tipo tupla. Suggerimento: si usi la funzione isinstance

lista = 'prova', 2, 3, (9,7), 'ciao'
conta = 0
for indice in lista:
    if isinstance(indice, tuple):
        break
    conta+= 1
print(conta)
