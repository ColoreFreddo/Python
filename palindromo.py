# Scrivere un programma che dica se una stringa è palindroma.
# str="ABBA" PALINDROMA
# str="PIPPO" NON PALINDROMA

stringa_1 = "ABBA"
stringa_2 = "PIPPO"

if stringa_1 == stringa_1[::-1]:
    print("PALINDROMA!")
else:
    print("NON PALINDROMA")
