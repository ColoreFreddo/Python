class Persona:
    def __init__(self, nome, indirizzo, eta):
        self.__nome = nome
        self.__indirizzo = indirizzo
        self.__eta = eta

    def __str__(self):
        return f'Nome: {self.nome}\nIndirizzo: {self.indirizzo}\nEtà: {self.eta}'

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_indirizzo(self):
        return self.indirizzo

    def set_indirizzo(self, indirizzo):
        self.indirizzo = indirizzo

    def get_eta(self):
        return self.eta

    def set_eta(self, eta):
        self.eta = eta


class Studente(Persona):
    def __init__(self, nome, indirizzo, eta, scuola, media_voti):
        super().__init__(nome, indirizzo, eta)
        self.scuola = scuola
        self.media_voti = media_voti

    def __str__(self):
        return f'{super().__str__()}\nScuola: {self.scuola}\nMedia voti: {self.media_voti}'

    def get_scuola(self):
        return self.scuola

    def set_scuola(self, scuola):
        self.scuola = scuola

    def get_media_voti(self):
        return self.media_voti

    def set_media_voti(self, media_voti):
        self.media_voti = media_voti


class Lavoratore(Persona):
    def __init__(self, nome, indirizzo, eta, azienda, stipendio):
        super().__init__(nome, indirizzo, eta)
        self.azienda = azienda
        self.stipendio = stipendio

    def __str__(self):
        return f'{super().__str__()}\nAzienda: {self.azienda}\nStipendio: {self.stipendio}'

    def get_azienda(self):
        return self.azienda

    def set_azienda(self, azienda):
        self.azienda = azienda

    def get_stipendio(self):
        return self.stipendio

    def set_stipendio(self, stipendio):
        self.stipendio = stipendio


persona = Persona('Marco', 'Via Italia, 1', 35)
print(persona)
persona.set_nome('Mario')
print(persona.get_nome())

studente = Studente('Luca', 'Via Roma, 2', 18, 'Liceo Scientifico', 8.5)
print(studente)
studente.set_media_voti(9.0)
print(studente.get_media_voti())

lavoratore = Lavoratore('Giuseppe', 'Piazza del Popolo, 3', 30, 'IBM', 2000)
print(lavoratore)
lavoratore.set_stipendio(2500)
print(lavoratore.get_stipendio())