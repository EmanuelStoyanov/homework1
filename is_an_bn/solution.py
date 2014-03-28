def is_an_bn(word):
    if len(word) % 2 != 0:
        return False
    else:
        half = len(word) // 2
        for i in range(0, half):
            if word[i] != 'a':
                return False
        for i in range(half, len(word)):
            if word[i] != 'b':
                return False
    return True
