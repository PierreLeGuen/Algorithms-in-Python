import saisieListe

liste = saisieListe.saisieListe()
print(liste)

for i in range(len(liste)//2) :
    liste[i], liste[len(liste) - i - 1] = liste[len(liste) - i - 1], liste[i]

print(liste)
