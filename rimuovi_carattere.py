# Scrivere un programma per rimuovere l'n- esimo carattere da una stringa non vuota. Progettare una funzione che accetti la stringa, 
# la posizione del carattere e restituisca la stringa modificata.
stringa = "prova"

def String(stringa,numero):
    risultato = stringa[0:numero-1]
    risultato += stringa[numero:len(stringa)]
    return risultato

numero = int(input("inserisci quale carattere vuoi rimuovere! : "))
print(String(stringa,numero))
