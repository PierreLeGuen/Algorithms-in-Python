#coding=UTF-8
import math
#EXO 1
def res_sec_deg(a,b,c):
    delta=b**2-4*a*c
    if delta>0:
        x=(-b-math.sqrt(delta))/2*a
        y=(-b+math.sqrt(delta))/2*a
        print("Deux solutions :")
        print(x,y)
    elif delta==0:
        x=-b/(2*a)
        print("Une solution")
        print(x)
    else:
        print("Pas de solution")
#a=5
#b=-70
#c=2
#res_sec_deg(a,b,c)

#EXO 2
#Q1
def perimetre(rayon):
    p=2*math.pi*rayon
    #print("Périmètre : ")
    #print(p)
    return p
def surface(rayon):
    s=math.pi*rayon*rayon
    #print("Surface : ")
    #print(s)
    return s
#rayon=input()
#perimetre_surface(rayon)

def surface_volume(rayon,hauteur):
    print(perimetre(rayon)*hauteur)
    print(surface(rayon)*hauteur)
#surface_volume(5,10)

#EXO 3
import random
def user_nb_rand():
    chiffre_alea = random.randint(0,100)
    chiffre = 0
    boucle = True
    while boucle == True:
        print("Rentre un chiffre :")
        chiffre=input()
        if chiffre > chiffre_alea:
            print("Chiffre plus petit")
        elif chiffre < chiffre_alea:
            print("Chiffre plus grand")
        else:
            print("Bravo, chiffre trouve")
            boucle = False
#user_nb_rand()

#EXO4 
def ordi_nb_rand():
    print("Borne inf : ")
    a=input()
    print("Borne sup : ")
    b=input()
    chiffre_alea = input("Rentre un chiffre : ")
    chiffre=(a+b)/2
    print(chiffre)
    boucle = True
    while boucle == True:
        #chiffre=(a+b)/2
        print("Chiffre plus grand que "+str(chiffre)+" ? [y=1/n=0]")
        rep = input()
        if rep == 0:
            b=chiffre
            chiffre = (a+b)/2
        elif rep == 1:
            a=chiffre
            chiffre = (a+b)/2
        else:
            print("BRAVO")
ordi_nb_rand()
        