#Creare una funzione che riceva una quantità di tempo in formato ore, minuti e secondi e la restituisca espressa solamente in secondi. Successivamente creare un programma
#principale che chieda in input due quantità di tempo e stampi in output quale quantità di tempo è maggiore. La funzione deve avere i parametri formali con valoripredefiniti.
#spazio
def calcola_tempo (ore_input = 0, minuti_input = 0, secondi_input = 0): # inizio dichiarazione funzione per la conversione in seconfi
        return (ore_input * 3600) + (minuti_input * 60) + (secondi_input) # funzione che converte in seconfi moltiplicando e sommando i valori in input
#spazio
ore_primo_valore, minuti_primo_valore, secondi_primo_valore = map(int, input("Inserire ore minuti e secondi separato da uno spazio: ").split()) # input dei primi dati separato da uno spazio
ore_secondo_valore, minuti_secondo_valore, secondi_secondo_valore = map(int, input("Inserire ore minuti e secondi separato da uno spazio: ").split()) # input dei secondi dati separati da uno spazio
# spazio
if calcola_tempo(ore_primo_valore, minuti_primo_valore, secondi_primo_valore) > calcola_tempo(ore_secondo_valore, minuti_secondo_valore, secondi_secondo_valore): # comparazione tra il primo e il secondo orario
    print("il primo formato è più grande!") # output in caso di primo valore più grande
elif (calcola_tempo(ore_primo_valore, minuti_secondo_valore, secondi_primo_valore) == calcola_tempo(ore_secondo_valore, minuti_secondo_valore, secondi_secondo_valore)): # se i valori sono uguali
    print("i formati sono uguali!") # output in caso i valori siano uguali
else: # ogni altro caso se è piu grade il secondo valore
    print("il secondo formato è più grande!") # output in caso di secondo valore più grade
