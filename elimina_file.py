# Scrivere un programma che elimini tutti i files che contengono nel nome una sequenza di caratteri dati in input.
import os

# richiesta dell'input all'utente
caratteri = input("Inserisci la sequenza di caratteri da cercare nel nome dei file: ")

# ottenere la directory corrente
directory_corrente = os.getcwd()

# ottenere la lista di tutti i file nella directory corrente
elenco_files = os.listdir(directory_corrente)

for file in elenco_files:
    # controllare se il file contiene la sequenza di caratteri dati in input
    if caratteri in file:
        # eliminare il file se contiene la sequenza di caratteri
        os.remove(file)
        print(f"{file} eliminato con successo!")