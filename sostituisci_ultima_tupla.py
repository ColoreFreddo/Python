# Scrivere un programma per sostituire l'ultimo valore delle tuple in una lista con un valore richiesto in input.
TuplaIN = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
input = int(input("Inserire valore da sostituire: "))
TuplaOUT = []

for indice in TuplaIN:
    temp = indice[:-1] + (input,)
    TuplaOUT.append(temp)
print(TuplaOUT)
