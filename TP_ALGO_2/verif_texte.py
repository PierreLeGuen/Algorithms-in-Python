def verif_saisie(texte_util):
    nombre = True
    i=0
    while i<len(texte_util) and nombre == True:
        if texte_util[i] < "0" or  texte_util[i] > "9":
            nombre = False
        i += 1

    return nombre

print(verif_saisie("5aze1"))
print(verif_saisie("1235465"))