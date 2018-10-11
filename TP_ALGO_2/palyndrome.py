def pal():
    palain = True
    user_entry=input("Phrase : ")
    split_entry=user_entry.split(" ")
    print(split_entry) #Debug purpose
    for i in range(len(split_entry)):
        for n in range(len(split_entry[i])):
            lettre=split_entry[i][n]
            lettre_fin=split_entry[i][len(split_entry[i])-(n+1)]
            if split_entry[i][n]!=split_entry[i][len(split_entry[i])-(n+1)]:
                return False
                
            else:
                palain = True
    return palain

    
print(pal())