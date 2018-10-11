liste = []

a = input("écrivez une phrase : ")

iMot = 0
liste.append("")
for i in a :
    if i != ' ' :
        liste[iMot] += i
    else :
        iMot += 1
        liste.append("")


for i in liste:
    listemot = list(i)
    palindrome = True
    for j in range(len(listemot)//2):
        if listemot[j] != listemot[len(listemot) - j - 1] :
            palindrome = False
    if palindrome :
        print(i)
