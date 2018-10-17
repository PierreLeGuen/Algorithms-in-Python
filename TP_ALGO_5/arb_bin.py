class ArbreBinaire():
    def __init__(self, racine):
        self.racine=racine
    def isEmpty(self):
        if self.racine==None:
            return True
    def root(self):
        return self.racine
    def affArbre(self):
        pass
        

class Node():
    def __init__(self, valeur, ref_ss_droit=None, ref_ss_gauche=None):
        self.valeur=valeur
        self.ref_ss_droit=ref_ss_droit
        self.ref_ss_gauche=ref_ss_gauche

def term():
    return None

g = ArbreBinaire(Node(1 ,Node(0 ,term(), term()) ,term()))