def factorielle(n):
    if (n >= 3):
        return n * factorielle(n-1)
    return n

print(factorielle(input("Enter a number : ")))