# Scrivere un programma che date due liste stampi "OK"  se hanno almeno un membro comune altrimenti stampa "KO".

lista1=[1,5,8] 
lista2=[3,1,10]
stampa = "KO"

for i in lista1:
    if i in lista2:
        stampa = "OK"
print(stampa)
