def saisie_liste():
    cest_un_nombre=True
    premier_nombre = input("Entrer un nombre : ")

    somme=int(premier_nombre)
    min=int(premier_nombre)
    max=int(premier_nombre)
    nombre_int = 0
    n=0
    moyenne = 0

    while cest_un_nombre==True:
        n += 1
        nombre=input("Entrer un nombre : ")
        if nombre=="":
            print("Ce n'est pas un nombre")
            cest_un_nombre=False
        else:
            nombre_int = int(nombre)
            somme += nombre_int
            moyenne = int(somme / n)
            if(min>nombre_int): 
                min = nombre_int
            elif(max<nombre_int): 
                max = nombre_int
            else:
                pass
            print("Moyenne actuelle : "+ str(moyenne))
            print("Min : "+str(min))
            print("Max : "+str(max))
saisie_liste()
