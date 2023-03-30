#Scrivete un programma Python per creare un dizionario da una stringa.
#Le lettere della stringa rappresentano le chiavi, i valori rappresentano le occorrenze della chiave nella stringa.
stringa = "ciao mamma"
new_diz = {}
countc = 0
counti = 0
counto = 0
countm = 0
counta = 0
for carattere in stringa:
    if carattere == 'c':
        countc+= 1
    if carattere == 'i':
        counti += 1
    if carattere == 'o':
        counto += 1
    if carattere == 'm':
        countm += 1
    if carattere == 'a':
        counta += 1
new_diz.update({'c': countc, 'i': counti, 'o': counto, 'm': countm, 'a': counta})
print(new_diz)