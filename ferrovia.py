# 6. Su una linea ferroviaria, rispetto alla tariffa piena, gli utenti pensionati usufruiscono di uno sconto del 10%, gli studenti del 15% e i disoccupati del 25%. 
# Codificando i pensionati con un 1, gli studenti con un 2 e i disoccupati con un 3, scrivere un programma che, richiesto il costo di un biglietto e l'eventuale 
# condizione particolare dell'utente, visualizzi l'importo da pagare.

print("Inserire codice interessato: ");
print("(1) Pensionato");
print("(2) Studenti ");
print("(3) disoccupati ");
code = input("Selezionare (1/2/3): ");
spesa = float(input("Inserire costo biglietto (euro): "));
if code == "1":
    spesa = spesa - ((spesa * 10)/100);
    print("Importo da pagare: ", spesa, "euro");
elif code == "2":
    spesa = spesa - ((spesa * 15)/100);
    print("Importo da pagare: ", spesa, "euro");
elif code == "3":
    spesa = spesa - ((spesa * 25)/100);
    print("Importo da pagare: ", spesa, "euro");
else:
    print("Codice selezionato errato, errore!");
