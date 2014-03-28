def toArr(n,arr):
    if n<=0:
        arr.reverse()
        return arr
    else:
        arr.append(n%10)
        return toArr(n//10,arr)

def member(arr,elem):
    for element in arr:
        if elem == element:
            return True
    return False

def contains_digits(number,arrdigits):
    for digit in arrdigits:
        if member(toArr(number,[]),digit) == False:
            return False
    return True
