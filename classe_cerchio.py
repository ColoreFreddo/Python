import math

class Cerchio(object):
    def __init__(self,centro,raggio):
        self.centro = centro
        self.raggio = raggio
    def getCentro(self):
        return self.centro
    def setCentro(self,punto):
        self.centro = punto
    def getRaggio(self):
        return self.raggio
    def setRaggio(self,val):
        self.raggio = val
    def __str__(self):
        return "C= "+str(self.centro)+" r= "+str(self.raggio)
    def getSuperficie(self):
        pigreco=3.1415
        return pigreco*self.raggio**2
    def distanza(self, altro_cerchio):
        x1, y1 = self.centro
        x2, y2 = altro_cerchio.centro
        return ((x2-x1)**2 + (y2-y1)**2)**0.5
    def relazione(self, altro_cerchio):
        d = self.distanza(altro_cerchio)
        r1, r2 = self.raggio, altro_cerchio.raggio
        if d == r1 + r2:
            return "esterna"
        elif d > r1 + r2:
            return "disgiunti"
        elif d == abs(r1 - r2):
            return "tangenti esternamente"
        elif d < abs(r1 - r2):
            return "uno interno all'altro"
        elif d == 0:
            return "uguali"
        elif d < r1 + r2:
            return "secanti o tangenti internamente"

c1 = Cerchio((0, 0), 4)
c2 = Cerchio((-3, 0), 2)
c3 = Cerchio((0, 0), 3)

print("Cerchio 1: ", c1)
print("Cerchio 2: ", c2)
print("Cerchio 3: ", c3)
print("Superficie cerchio 1:", c1.getSuperficie())
print("Distanza tra cerchi 1 e 2:", c1.distanza(c2))
print("Relazione tra cerchio 1 e 2:", c1.relazione(c2))
print("Distanza tra cerchi 1 e 3:", c1.distanza(c3))
print("Relazione tra cerchio 1 e 3:", c1.relazione(c3))
    
