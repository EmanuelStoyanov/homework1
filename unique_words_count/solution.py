def unique_words_count(arr):
    count = 0
    dict = count_words(arr)
    for key in dict:
        count += 1
    return count


def count_words(arr):
    dict = {}
    for word in arr:
        dict[word] = countmember(word, arr)
    return dict


def countmember(word, arr):
    count = 0
    for one in arr:
        if one == word:
            count += 1
    return count
