#Scrivere un programma che legga il raggio r di una circonferenza e ne calcoli l'area e la lunghezza.

r = float(input("Inserire raggio (cm): "));
a = (r**2) * 3.14;
p = (2*3.14)*r;
print("Area = " , a, "cm");
print("Circonferenza = ", p, "cm");
