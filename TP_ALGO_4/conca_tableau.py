def conca_tableau(tab1,tab2):
    for i in tab2:
        tab1.append(i)
    return tab1

def tableau(n):
    tableau_return=[]
    for i in range(n):
        tableau_return.append(i+1)
    return tableau_return

print(conca_tableau(tableau(4),tableau(7)))