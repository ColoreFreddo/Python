#Costruire una funzione che abbia in input un numero intero positivo N, la funzione deve restituire  il fattoriale di N. Utilizzare la funzione almeno due volte.
# Spazio
#Fattoriale di n:  Definizione: n! = n(n-1)(n-2)...2*1 ; 0! = 1  
# Spazio
#esempio: 4! = 4*3*2= 24
# Spazio
import math # Importo la libreria che mi permette di usare funzioni matematiche
# Spazio
def Fattoriale_Valore_In_Input(input_numero): # Inizio funzione per la fattorializzazione di un numero in input
    fattoriale_output = 0 # Alloco un valore alla variabile fattoriale
    if input_numero > 0: # Verifico che il numero sia positivo
        fattoriale_output = math.factorial(input_numero) # Uso una funzione importata per calcolare il fattoriale del numero in input
    return fattoriale_output # ritorno il numero fattorializzato
# Spazio
input_numero = int(input("Inserire numero da fattorializzare: ")) # Richiedo valori in input per fattorializzarlo
output = Fattoriale_Valore_In_Input(input_numero) # Utilizzo la funzione appena creata per fattorializzare il numero intero
print("Il numero fattorializzato è ", output) # Output lato utente del numero fattorializzato
