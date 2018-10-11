def inversion_liste(liste):
    liste_reverse=[]
    for i in range(len(liste)):
        print(len(liste))
        liste_reverse.append(liste[len(liste)-(i+1)])
    return liste_reverse
print(inversion_liste([155,484,5,7]))