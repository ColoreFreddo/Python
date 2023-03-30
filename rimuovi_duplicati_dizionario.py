#Scrivete un programma Python per rimuovere i duplicati dal dizionario. 
Dizionario =  {1: 1,1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
out = {}
for key,value in Dizionario.items():
    if value not in out.values():
        out[key] = value
print(out)