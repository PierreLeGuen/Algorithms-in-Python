def saisie_liste():
    cest_un_nombre=True
    liste_nombre=[]
    while cest_un_nombre==True:
        entree_liste=input("Entrer un nombre : ")
        if entree_liste=="":
            print("Ce n'est pas un nombre")
            cest_un_nombre=False
            print(liste_nombre)
        else:
            liste_nombre.append(entree_liste)
saisie_liste()
