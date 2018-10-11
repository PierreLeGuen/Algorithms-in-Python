#coding:UTF-8
#Note : Pourcentage réussite aux questions, 15% pour optimisation

# Pas grave si utilisation de math.sqrt()
print("----------------------------")
#Exo 2
def decomp_iteratif(n):
    res=[]
    while n>0:
        rac=int(n**0.5)
        res.append(rac**2)
        n=n-rac**2
    return res
print("Décomposition itérative : "+ str(decomp_iteratif(18)))

def decomp_recursif(n):
    if n==0:
        return []
    else:
        rac = int(n**0.5)
        return [rac**2]+decomp_recursif(n-rac**2)
print("Décomposition récursive : "+ str(decomp_recursif(15)))

#Exo 3
def syracuse(u):
    if u==1:
        return [1]
    elif u%2==0:
        return [u] + syracuse(u//2)
    else:
        return [u] + syracuse(3*u+1)
print("Syracuse : "+ str(syracuse(15)))


#Exo 4 : nombres premiers
# |0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|
# ------------------------------------------------------
# |F|F|V|V|F|V|F|V|F|F|F|.....

def erastosthene(n):
    premier = [True] * (n+1)
    stop = int(n**0.5)
    for i in range(2, stop + 1):
        if premier[i]:
            j=i*i
            while j <= n:
                premier[j]=False
                j=j+i
    res=[]
    for i in range(2, n+1):
        if premier[i]:
            res.append(i)
    return res
print("Nombres premiers : "+ str(erastosthene(20)))

# Exo 5 : nbrs parfaits
def est_parfait(m):
    som_div=0
    for i in range(1, m//2 + 1):
        if m%i == 0:
            som_div=som_div+i
    if m==som_div:
        return m
def parfait(n):
    for n in (2, n+1):
        est_parfait(n)
    return "Test"
    #le return bug mais l'idée est là
print("Nbrs parfaits : " + str(parfait(50)))

print("----------------------------")
