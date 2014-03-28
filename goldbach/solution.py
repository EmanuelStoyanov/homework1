def goldbach(n):
    array = []
    for i in range(2, n//2+1):
        if is_prime(i) and is_prime(n-i):
            array.append((i, n-i))
    return array


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
