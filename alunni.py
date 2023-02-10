# 5. Scrivere un programma che chiede quanti alunni ci sono in una classe poi per ogni alunno fa inserire M voti, M dato in input, e ne scrive la media.

m = 0;
n = int(input("Quanti voti vuoi inserire?: "));
for i in range(0,n):
    v = float(input("Inserire voto: "));
    m += v;
m = m / n;
print("Media : ", m);
