def liste_0_100():
    liste=[]
    for i in range(101):
        liste.append(i)
    return liste

def dichotomie(liste,nb_cherche):
    return dichotomie_rec( liste, nb_cherche, 0, len(liste)-1)

def dichotomie_rec(liste,nb_cherche, a, b):
    if len(liste) == 1:
        return 0
    m=(a+b)//2
    if liste[m]==nb_cherche:
        return m
    elif liste[m]<nb_cherche:
        return dichotomie_rec(liste,nb_cherche,m,b)
    elif liste[m]>nb_cherche:
        return dichotomie_rec(liste,nb_cherche,a,m)


    
nb_cherche=int(input("Nombre recherche = "))
liste=liste_0_100()

print(dichotomie(liste,nb_cherche))