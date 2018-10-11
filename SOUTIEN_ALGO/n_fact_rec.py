def fact(n):
    if n==1:
        res=1
    elif n>1:
        res=n*fact(n-1)
    return res
    
print(fact(5))