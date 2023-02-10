# 5. Un negoziante per ogni spesa di importo superiore a 100 € effettua uno sconto del 5%, se l’importo risulta superiore a 300€
# lo sconto è del 10%.Scrivere un programma che richieda all'utente l'ammontare della spesa e visualizzi quindi l'importo 
# effettivo da pagare.
spesa = float(input("Inserire spesa (euro): "))
if spesa > 100:
    spesa = spesa - ((spesa * 5)/100);
elif spesa > 300:
    spesa = spesa - ((spesa * 10)/100);
else:
    spesa = spesa;
print("Importo da pagare: ", spesa, "euro");
