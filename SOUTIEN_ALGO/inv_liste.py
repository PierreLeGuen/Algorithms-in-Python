def inv_liste(liste):
    len_liste = len(liste)
    m_liste = len_liste//2
    for i in range(m_liste):
        j=liste[len_liste-i-1]
        x=liste[i]
        liste[i]=j
        liste[len_liste-i-1]=x
    print(liste)
inv_liste([1,2,3,4,5])