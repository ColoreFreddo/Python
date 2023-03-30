#Scrivete uno script Python per generare e stampare un dizionario che contenga un numero (compreso tra 1 e n) nella forma (x, x*x).
n = 5
#Dizionario = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
dizout = {}
diztmp=[]
for indice in range(n):
    dizout.update({indice:indice*indice})
print(dizout)