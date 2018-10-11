###  QUICKSORT
A=[44,5,22,0,323,995,94,4,7,15]
def main():
    r=len(A)-1
    p=0
    Result=QuickSort(A,p,r)
    print(Result)
    
def QuickSort(A,p,r):
    if p<r:
        q=partition(A, p, r)
        QuickSort(A, p, q-1)
        QuickSort(A, q+1, r)
    return A

def partition(A,p,r):
    x=A[r]
    i=p-1
    for j in range(p,r):
        if A[j]<=x:
            i=i+1
            a,b=A.index(A[i]), A.index(A[j])
            A[a],A[b]=A[b],A[a]
    d,c=A.index(A[i+1]),A.index(A[r])
    A[c],A[d]=A[d],A[c]
    return i+1
main()