#4. Scrivere un programma che legge N numeri da tastiera, N dato in input, e ne  restituisca il minimo.

from sys import maxsize

t = maxsize;
n = int(input("Quanti numeri vuoi inserire? "));
for i in range(0,n):
    g = float(input("Inserisci il numero: "));
    if t > g:
        t = g;
print("Il minimo è ", t);
