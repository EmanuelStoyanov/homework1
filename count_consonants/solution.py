def count_consonants(str):
    consonants = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"
    count = 0
    for letter in str:
        if member(consonants,letter):
            count+=1
    return count

def member(arr,elem):
    for element in arr:
        if elem == element:
            return True
    return False
