#coding = UTF-8
def calc(calcul):
    partie_gauche = ""
    partie_droite = ""
    for i in calcul:
        while i != "x" and i != "+" and i != "%" and i != "-" and i != "/":
            partie_gauche.append(i)
            print("Partie gauche :" + partie_gauche)
    for i in range(len(calcul)):
        while calcul[len(calcul)-i] != "x" and calcul[len(calcul)-i] != "+" and calcul[len(calcul)-i] != "%" and calcul[len(calcul)-i] != "-" and calcul[len(calcul)-i] != "/":
            partie_droite.append(len(calcul)-i)
            print("partie droite : " + partie_droite)
print(calc(1+7))
