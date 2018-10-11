import saisieListe

listenombres = saisieListe.saisieListe()

somme = 0
compteur = 0
nombremin = int(listenombres[0])
nombremax = int(listenombres[0])
for i in listenombres:
    somme += int(i)
    compteur += 1
    if int(i) > nombremax :
        nombremax = int(i)
    if int(i) < nombremin :
        nombremin = int(i)
    print(i + " :")
    print('minimum = ' + str(nombremin))
    print('maximum = ' + str(nombremax))
    print('moyenne = ' + str((somme/compteur)))
    
