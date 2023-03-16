# Scrivere un programma per rimuovere l'n- esimo carattere da una tupla non vuota. 
tupla = (1,2,3,4)

index = int(input("Inserire che posizione rimuovere: "))
l1=list(tupla)
l1.pop(index)
tupla=tuple(l1)
print(tupla)
