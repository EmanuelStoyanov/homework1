def simplify_fraction(fraction):
    gcd = nod(fraction[0], fraction[1])
    return (fraction[0]//gcd, fraction[1]//gcd)


def nod(a, b):
    if a > b:
        return nod(a-b, b)
    elif a < b:
        return nod(a, b-a)
    else:
        return a
