#Creare una funzione che abbia come parametri formali un numero arbitrario di valori numerici. Si vuole che restituisca la somma dei soli numeri pari e il prodotto dei soli
#numeri dispari. Successivamente creare un programma che richiami tale funzione e che stampi in output i risultati.

def PoD(*numero):
    somma = 0.0
    prodotto = 0.0
    for x in numero:
        if float(x) % 2 == 0:
            somma += x
        else:
            if prodotto == 0:
                prodotto += 1
                prodotto *= x
            else:
                prodotto *= x
    return somma, prodotto
somma, prodotto = PoD(1, 4, 2, 7)
print("Ecco i risultati: ",somma," ", prodotto)
