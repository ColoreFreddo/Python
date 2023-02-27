# Conversione temperatura: implementare una funzione convertiCF che effettuti la conversione in gradi Fahrenheit di una temperatura in gradi Celsius. 
# Usare la seguente formula:

# F = ( 9 / 5 ) * C + 32

# Creare un programma principale che richiami la funzione e ne stampi il risultato visualizzando solo 3 cifre decimali.

def ConvertiCF(celsius = 0.000):
    return (9/5) * (celsius + 32)

celsius = float(input("Inserire gradi celsius da convertire: "))
print("I gradi in Fahrenheit sono: ", float(round(ConvertiCF(celsius), 3)))
