class AritmeticaDue:
    def __init__(self, op1=0, op2=0):
        self.operando1 = op1
        self.operando2 = op2
    def __str__(self):
        return f"Arithmetic Two: {self.operando1} and {self.operando2}"
    def differenza(self):
        return abs(self.operando1 - self.operando2)
    def prodotto(self):
        return self.operando1 * self.operando2
    def confronto(self, other):
        prodotto_other = other.prodotto()
        prodotto_self = self.prodotto()
        if prodotto_self > prodotto_other:
            return f"{prodotto_self} > {prodotto_other}"
        elif prodotto_self == prodotto_other:
            return f"{prodotto_self} = {prodotto_other}"
        else:
            return f"{prodotto_self} < {prodotto_other}"

class AritmeticaTre(AritmeticaDue):
        def __init__(self, op1=0, op2=0, op3=0):
            super().__init__(op1, op2)
            self.operando3 = op3
        def __str__(self):
            return f"Arithmetic Three: {self.operando1}, {self.operando2} and {self.operando3}"    
        def somma(self):
            return self.operando1 + self.operando2 + self.operando3

ar2 = AritmeticaDue(2, 5)
print(ar2.differenza())
print(ar2.prodotto())
ar2_2 = AritmeticaDue(3, 4)
print(ar2.confronto(ar2_2))
ar3 = AritmeticaTre(2, 5, 8)
print(ar3.somma())