# Conversione temperatura: implementare una funzione convertiCF che effettuti la conversione in gradi Fahrenheit di una temperatura in gradi Celsius. 
# Usare la seguente formula:
# Spazio
# F = ( 9 / 5 ) * C + 32
# Spazio
# Creare un programma principale che richiami la funzione e ne stampi il risultato visualizzando solo 3 cifre decimali.
# Spazio
def ConvertiCelsiusInFarenheit(celsius_input = 0.000): # Inizio definizione della funzione per la conversione da celsius in Fahrenheit
    return (9/5) * (celsius_input + 32) # funzione che ritorna il valore convertito in Fahrenheit
# Spazio
celsius_input = float(input("Inserire gradi celsius da convertire: ")) # Richiedo all'utente l'input dei celsius da allocare che viene convertito in float
print("I gradi in Fahrenheit sono: ", float(round(ConvertiCelsiusInFarenheit(celsius_input), 3))) # Output del valore Fahrenheit con al massimo 3 valori dopo la virgola
