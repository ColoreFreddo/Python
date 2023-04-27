# Lettura della stringa da input
stringa = input("Inserisci una stringa: ")

# Salvataggio della stringa su file
with open("stringa.txt", "w") as file:
    file.write(stringa)

# Apertura del file per verifica
with open("stringa.txt", "r") as file:
    contenuto = file.read()

# Verifica del salvataggio
if contenuto == stringa:
    print("Salvataggio avvenuto!")
else:
    print("Errore!")
