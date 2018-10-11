def convert(n,base):
    if n < base:
        res = str(n)
    else:
        res = convert(n//base,base) + str(n%base)
    return res


print(convert(10,2))

def convert_inv(n,base):
    if n < base:
        res = str(n)
    else:
        res = str(n%base) + convert(n//base,base)
    return res


print(convert_inv(10,2))
