#Creare una funzione che riceva una quantità di tempo in formato ore, minuti e secondi e la restituisca espressa solamente in secondi. Successivamente creare un programma
#principale che chieda in input due quantità di tempo e stampi in output quale quantità di tempo è maggiore. La funzione deve avere i parametri formali con valoripredefiniti.

def tempo (ore = 0, minuti = 0, secondi = 0):
        return (ore * 3600) + (minuti * 60) + (secondi)

ore, minuti, secondi = map(int, input("Inserire ore minuti e secondi separato da uno spazio: ").split())
ore1, minuti1, secondi1 = map(int, input("Inserire ore minuti e secondi separato da uno spazio: ").split())

if tempo(ore, minuti, secondi) > tempo(ore1, minuti1, secondi1):
    print("il primo formato è più grande!")
else:
    print("il secondo formato è più grande!")

