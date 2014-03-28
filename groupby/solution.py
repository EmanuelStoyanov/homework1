def groupby(func, seq):
    dict = {}
    for number in seq:
        dict[func(number)] = []
    for number in seq:
        dict[func(number)].append(number)
    return dict

