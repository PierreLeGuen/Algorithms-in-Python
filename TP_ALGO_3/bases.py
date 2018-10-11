def NbChiffres(n,base):
    res=0
    if (n//base) == 0:
        res+=1
    else:
        res = 1 + NbChiffres(n//base,base)
    return res

print(NbChiffres(5102540512,10))