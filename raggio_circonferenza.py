#Scrivere un programma che legga il raggio r di una circonferenza e ne calcoli l'area e la lunghezza.

print("Inserire raggio: ");
r = float(input("Inserire raggio: "));
a = (r**2) * 3.14;
p = (2*3.14)*r;
print("Area = " , a);
print("Circonferenza = " , p);
