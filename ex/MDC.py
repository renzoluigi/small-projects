def mdc(a,b):
    if b == 0:
        return a
    else:
        return b,a % b
print(mdc(9,6))