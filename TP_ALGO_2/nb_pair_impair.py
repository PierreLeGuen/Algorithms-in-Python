def liste_0_100():
    liste=[]
    for i in range(101):
        liste.append(i)
    return liste

def pair_impair():
    L=liste_0_100()
    pair=[]
    for i in range(len(L)):
        if L[i]%2==0:
            pair.append(L[i])
    for i in range(len(L)):
        if L[i]%2!=0:
            pair.append(L[i])
    return pair

print(pair_impair())
