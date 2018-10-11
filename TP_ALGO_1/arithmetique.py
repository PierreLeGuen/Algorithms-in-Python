def est_divisible_par(n,k):
    if n%k == 0:
        print(str(n)+" est divisible par "+str(k))
    else:
        print(str(n)+" n'est pas divisible par "+str(k))
a=[5,6,9]
b=[3,2,3]
for i in range(3):
    est_divisible_par(a[i],b[i])