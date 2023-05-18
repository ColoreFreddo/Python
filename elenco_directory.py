# Scrivere una procedura che dato un percorso elenchi tutte le directories presenti.
import os

def list_directories(path):
    """
    Questa funzione accetta un percorso e stampa tutte le directory presenti.
    """
    for name in os.listdir(path):
        if os.path.isdir(os.path.join(path, name)):
            print(os.path.join(path, name))

dir = input("Inerire indirizzo: ")
print(list_directories(dir))