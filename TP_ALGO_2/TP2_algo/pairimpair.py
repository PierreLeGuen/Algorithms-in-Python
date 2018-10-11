import random

liste = []
for i in range(0,random.randint(1,100)):
    liste.append(random.randint(1,100))
print (liste)

for i in range(len(liste)):
    if liste[i]%2 == 0:
        for j in range(i - 1, -1, -1):
            liste[j],liste[j+1] = liste[j+1],liste[j]

print(liste)
