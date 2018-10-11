def est_paire(n):
    if n%2 == 0:
        print(str(n)+" est pair")
    else:
        print(str(n)+" n'est pas pair")

a=[2,4,3,7]

for i in range(4):
    est_paire(a[i])