def simu_tableau(tableau,position,element):
    tableau.append(0)
    for i in range(len(tableau)-position):
        tableau[len(tableau)-(i+1)]=tableau[len(tableau)-(i+1)-1]
    tableau[position-1]=element
    return tableau


def tableau(n):
    tableau_return=[]
    for i in range(n):
        tableau_return.append(i+1)
    return tableau_return

print(simu_tableau(tableau(20),14,"x"))