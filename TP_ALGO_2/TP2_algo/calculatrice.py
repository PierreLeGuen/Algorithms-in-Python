x = input("Entrez votre calcul : ")

liste = list(x)
def test1(t):
    testoperateur = False
    for i in range(len(t)-1):
        if ('0'>t[i] or t[i]>'9'):
            if (t[i]!='+' and t[i]!='-' and t[i]!='*' and t[i]!='/' and t[i]!='%'):
                return False
            
        if (t[i]=='+' or t[i]=='-' or t[i]=='*' or t[i]=='/' or t[i]=='%'):
            if testoperateur == True:
                return False
            else:
                testoperateur = True

    if (liste[len(liste)-1] != '='):
        return False
    return True

if test1(liste):
    j = 0
    a = 0
    nombre1 = 0
    nombre2 = 0
    operande = 0
    while '0'<liste[j] and liste[j]<'9':
        nombre1 = nombre1*10 + int(liste[j])
        j = j+1
    a = j
    j=j+1
    while '0'<liste[j] and liste[j]<'9':
        nombre2 = nombre2*10 + int(liste[j])
        j = j+1
    if (liste[a]=='+'):
        print(str(nombre1) + " + " + str(nombre2) + " = " + str(nombre1+nombre2))
    elif (liste[a]=='-'):
        print(str(nombre1) + " - " + str(nombre2) + " = " + str(nombre1-nombre2))
    elif (liste[a]=='*'):
        print(str(nombre1) + " * " + str(nombre2) + " = " + str(nombre1*nombre2))
    elif (liste[a]=='/'):
        print(str(nombre1) + " / " + str(nombre2) + " = " + str(nombre1/nombre2))
    else:
        print(str(nombre1) + " % " + str(nombre2) + " = " + str(nombre1%nombre2))
else:
    print("Erreur de syntaxe.")
