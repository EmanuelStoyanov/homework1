def sort_fractions(fractions):
    for i in range(0, len(fractions)):
        for j in range(i+1, len(fractions)):
            if bigger(fractions[i], fractions[j]):
                temp = fractions[i]
                fractions[i] = fractions[j]
                fractions[j] = temp
    return fractions


def bigger(fraction1, fraction2):
    what_is_nok = nok(fraction1[1], fraction2[1])
    m1 = what_is_nok // fraction1[1]
    m2 = what_is_nok // fraction2[1]
    return fraction1[0]*m1 > fraction2[0]*m2


def nok(a, b):
    if a == b:
        return a
    elif a % b == 0:
        return a
    elif b % a == 0:
        return b
    elif is_prime(a) or is_prime(b):
        return a * b
    elif a > b:
        for i in range(a, a*b):
            if i % a == 0 and i % b == 0:
                return i
    else:
        for i in range(b, a*b):
            if i % a == 0 and i % b == 0:
                return i


def is_prime(n):
    return sum_of_divisors(abs(n)) == abs(n) + 1


def sum_of_divisors(n):
    return sum(divisors(n))


def divisors(n):
    if n != 1:
        arr = [1, n]
    else:
        return [1]
    for i in range(2, n):
        if n % i == 0:
            arr.append(i)
    return arr
