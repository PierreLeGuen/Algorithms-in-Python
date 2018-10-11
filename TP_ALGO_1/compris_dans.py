x=input()
y=input()
z=input()
def est_compris_dans(a,b,c):
    if a<z and a>y:
        print(str(a)+" est compris dans [ "+str(b)+","+str(c)+" ]")
    else:
        print(str(a)+" n'est pas compris dans ["+str(b)+","+str(c)+"]")
est_compris_dans(x,y,z)