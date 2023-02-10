# 3. Leggere una successione di numeri interi passati dall’utente, fermandosi al primo numero che rende
# la successione non crescente e restituendo quanti numeri formano la successione inserita.
import sys
from sys import maxsize

count = 0;
new_num = 0;
while True:
    num = new_num;
    new_num = float(input("Inserisci numero: "));
    count += 1;
    if num > new_num:
        count -= 1;
        print("Numero inerito minore del precedente! Sequenza da ", count, " elementi.");
        sys.exit();
    else:
        num = maxsize;
