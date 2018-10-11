import verification

def saisieListe() :

    liste = []
    fin = False

    while not fin :
        a = input("entrez une valeur : ")
        if verification.verification(a) :
            liste.append(a)
        if a == "" :
            fin = True

    return liste
