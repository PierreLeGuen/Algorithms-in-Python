class Maillon():
    def __init__(self, val):
        self.val=val
        self.suiv=None

class ListeCh_Simple():
    def __init__(self, tete=None):
        self.tete=tete
    def affListeCh(self):
        courant = self.tete
        while courant != None:
            print(courant.val, end = " -- > ")
            courant = courant.suiv
    def ajoutTete(self, valeurTete):
        mx = Maillon(valeurTete)
        mx.suiv=self.tete
        self.tete = mx
    def ajoutFin(self, valeurFin):
        courant = self.tete
        mf = Maillon(valeurFin)
        if courant == None:
            self.tete=mf
        else:
            while courant.suiv != None:
                courant = courant.suiv


m = Maillon("5")

l = ListeCh_Simple(m)
l.ajoutTete("1")
#l.ajoutTete("2")
l.ajoutFin("10")
l.affListeCh()
