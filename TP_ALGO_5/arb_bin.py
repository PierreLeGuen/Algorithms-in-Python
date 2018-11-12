class ArbreBinaire():
    def __init__(self, racine):
        self.racine=racine
    def isEmpty(self):
        if self.racine==None:
            return True
    def root(self):
        return self.racine
        

class Node():
    def __init__(self, valeur, f_droit=None, f_gauche=None):
        self.valeur=valeur
        self.f_droit=f_droit
        self.f_gauche=f_gauche

def term():
    return None

def tree(noeud):
    return(ArbreBinaire(noeud))

def depth(arb):
    d=1
    n=ArbreBinaire.root(arb)
    if n==None:
        return -1
    else:
        prof_a = depth(tree(n.f_droit))
        prof_b = depth(tree(n.f_gauche))

    if prof_a>prof_b:
        d += prof_a
    else:
        d += prof_b
    return d

g = ArbreBinaire(Node(1 ,Node(0 ,term(), term()) ,term()))

print(depth(g))