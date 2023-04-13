class calcolatore:
    def Factorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self.Factorial(n-1)
        
    def Sum(self, n):
        return sum(range(1,n+1))
    
    def tableMult(self, n):
        for i in range(1, 11):
            print(n, "x", i, "=", n*i)
        
    def allTablesMult(self):
        for i in range(1, 10):
            self.tableMult(i)
            print()
calcolatore = calcolatore()
print(calcolatore.Factorial(10)) 
print(calcolatore.Sum(70)) 
calcolatore.tableMult(9)