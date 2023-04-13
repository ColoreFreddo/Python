class Insegnante:

    def __init__(self, nome, eta, stipendio): 
        self.nome = nome 
        self.eta = eta 
        self.__stipendio = stipendio

    def setNome(self, nome): 
        self.nome = nome

    def setEta(self, eta): 
        self.eta = eta

    def setStipendio(self, stipendio): 
        self.__stipendio = stipendio

    def getNome(self): 
        return self.nome

    def getEta(self): 
        return self.eta

    def getStipendio(self): 
        return self.__stipendio

    def __str__(self): 
        return "Nome: " + self.nome + ", Eta: " + str(self.eta)

insegnante1 = Insegnante("Mario Rossi", 35, 2000) 
insegnante2 = Insegnante("Giuseppe Verdi", 45, 3500)

print(insegnante1) 
print(insegnante2)