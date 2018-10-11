#coding: UTF-8
class Maillon():
    def __init__(self, valeur=None, addrSuiv=None, addrPrec=None):
        self.val=valeur #Int,Str,....
        self.aS=addrSuiv #Réf vers le suivant
        self.aP=addrPrec

class ListeCh():
    def __init__(self, premier=None):
        self.tete=premier #Tete de la liste chainée (réf)

    def affListCh(self):
        if self.tete!=None:
            courant = self.tete
            while courant!=None:
                print(courant.val,end=' => ')
                courant = courant.aS
        print("\n")

    def ajoutTete(self,x):
        mx= Maillon(x,self.tete)
        mx.aS.aP=mx
        self.tete = mx

    def ajoutQueue(self,x):
        if self.tete!=None:
                    courant = self.tete
                    while courant.aS!=None: # Parcours tant que pas fini
                        courant = courant.aS
                    mxq=Maillon(x,None,courant)
                    courant.aS=mxq

    def insertListeCh(self,position):
        indice=0
        element="5"
        if self.tete!=None:
            courant = self.tete
            while courant.aS!=None and indice<position: # Parcours tant que pas fini
                courant = courant.aS
                indice += 1
            mxq=Maillon(element,None,None)
            courant.aP.aS=mxq
            mxq.aP=courant.aP
            courant.aP=mxq
            mxq.aS=courant

    def searchListeCh(self, searched):
        if self.tete :
            courant = self.tete
            val = courant.val
            while courant.aS and val!=searched:
                courant = courant.aS
                val = courant.val
            print("Valeur " + str(searched) + " trouvée")

def concaListeCh(alist1,alist2):
    if alist1.tete and alist2.tete:
        courant = alist1.tete
        while courant.aS:
            courant = courant.aS
        courant.aS = alist2.tete
        alist2.tete.aP = courant
    return alist1
            
m=Maillon("10")

l=ListeCh(m)
l.ajoutTete("0")
l.ajoutQueue("20")
l.insertListeCh(1)
#l.affListCh()

a=Maillon("100")
x=ListeCh(a)
x.ajoutQueue("150")
x.ajoutQueue("200")
x.ajoutTete("50")
#x.affListCh()

concaListeCh(l,x)

l.affListCh()

l.searchListeCh("50")