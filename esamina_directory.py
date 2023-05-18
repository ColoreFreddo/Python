# Scrivere un programma che esamini tutte le directories sotto un dato percorso e conti tutti i files con una determinata estensione data in input.
# [In prima battuta fermatevi al primo livello di profondità delle directories]
import os

def conta_files_con_estensione(path, estensione):
    totale = 0
    for nome in os.listdir(path):
        if os.path.isfile(os.path.join(path, nome)):
            if nome.endswith(estensione):
                totale += 1
        elif os.path.isdir(os.path.join(path, nome)):
            totale += conta_files_con_estensione(os.path.join(path, nome), estensione)
    return totale

percorso = input("Inserisci il percorso da esaminare: ")
estensione = input("Inserisci l'estensione dei file da contare (es. .txt): ")

totale = conta_files_con_estensione(percorso, estensione)

print("Il totale dei file con estensione", estensione, "è", totale)