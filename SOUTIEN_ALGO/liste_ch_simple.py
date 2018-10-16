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
            print(courant.val,end=' => ')
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
            courant.suiv=mf
    def ajoutPos(self, position, valeur):
        pos_actuel = 0
        courant = self.tete
        mp = Maillon(valeur)
        if courant == None or position == 0:
            self.tete=mp
            mp.suiv = courant
        else:
            while courant.suiv and pos_actuel < position:
                pos_actuel+=1
                courant_prec=courant
                courant = courant.suiv
            courant_prec.suiv=mp
            mp.suiv=courant
    def ajoutListeTrie(self,val):
        courant = self.tete
        ml= Maillon(val)
        if courant.suiv == None or val < courant.val:
            self.ajoutTete(val)
        else:
            while(val > courant.val) and courant.suiv:
                courant_prec=courant
                courant=courant.suiv
            if courant.suiv==None:
                courant.suiv=ml
            else:
                courant_prec.suiv=ml
                ml.suiv=courant
    def compterNbElem(self):
        nbElem=0
        i=0
        courant = self.tete
        while courant:
            nbElem+=1
            courant=courant.suiv
        return nbElem
            
        


m = Maillon(0)
l = ListeCh_Simple(m)
for i in range(0):
    l.ajoutFin(i+1)

#l.ajoutListeTrie(10)

print(l.compterNbElem())

l.affListeCh()
