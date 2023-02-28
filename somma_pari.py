#Creare una funzione che abbia come parametri formali un numero arbitrario di valori numerici. Si vuole che restituisca la somma dei soli numeri pari e il prodotto dei soli
#numeri dispari. Successivamente creare un programma che richiami tale funzione e che stampi in output i risultati.
#spazio
def ProdottoOSommaValore(*input_numero): # Inizio definizione funzione per determinare se il valore è da sommare o fare il prodotto
    somma_valore_in_input = 0.0 # Alloca un valore alla somma in input
    prodotto_valore_in_input = 0.0 # Alloca un valore al prodotto in input
    for valore in input_numero: # Inizio ciclo per i valori presenti in input_numero
        if float(valore) % 2 == 0: # Eseguo il modulo del valore per verificare se è uguale a 0 quindi pari
            somma_valore_in_input += valore # Accumulo il valore in somma_valore_in_input
        else: # Inizio else per controlli
            if prodotto_valore_in_input == 0: # Se il valore è uguale a (0 int)
                prodotto_valore_in_input += 1 # Accumulo una somma (1 int)
                prodotto_valore_in_input *= valore #Accumulo un prodotto
            else: # Inizio else ulteriore per scrematura
                prodotto_valore_in_input *= valore # Accumulo il prodotto di valore
    return somma_valore_in_input, prodotto_valore_in_input # output della funzione Prodotto O Somma Valore
#spazio
somma_output_finale, prodotto_output_finale = ProdottoOSommaValore(1, 4, 2, 7) # Utilizzo la funzione con dei valori pre allocati
print("Ecco i risultati: ",somma_output_finale," ", prodotto_output_finale) # Output della funzione
