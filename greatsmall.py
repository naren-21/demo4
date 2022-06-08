def great(x,y,z):
    if x>y and x>z:
        return x
    elif y>x and y>z:
        return y
    else:
        return z
print("largest among 3 no.s is",great(10,50,80))
