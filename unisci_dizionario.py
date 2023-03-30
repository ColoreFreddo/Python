#Progettare una funzione che accetti un numero indefinito di dizionari e restituisca un dizionario che è 
#la concatenazione di tutti i dizionari indicati come parametro formale alla funzione. Scrivete uno script che utilizzi tale funzione.
diz1 = {'v1':1,'v2':2,'v3':3}
diz2 = {'v4':4,'v5':5,'v6':6}
diz3 = {'v7':7,'v8':8}
dizout = {}
#inizio definizione funzione per unire dizionari
def unisci_dizionari(diz1,diz2,diz3):
        tmp = diz1 | diz2 | diz3
        return tmp

dizout = unisci_dizionari(diz1,diz2,diz3)
print(dizout)