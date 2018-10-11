def tableau(n):
    tableau_return=[]
    for i in range(n):
        tableau_return.append(i)
    return tableau_return

def searchTab(tab,element):
    print(tab)
    for i in tab:
        if i==element:
            print("Index de l'élément recherché : "+str(tab[i]))
            return i
    return False

print(searchTab(tableau(9),0))

