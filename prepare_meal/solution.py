def prepare_meal(number):
    count = 0
    spams = []
    for i in range(1, number):
        if number % 3 ** i == 0:
            count = i
    if count == 0 and number % 5 == 0:
        return "eggs"
    elif count == 0 and number % 5 != 0:
        return ''
    elif number % 5 == 0:
        for i in range(1, count+1):
            spams.append("spam")
        return " ".join(spams) + " and eggs"
    else:
        for i in range(1, count+1):
            spams.append("spam")
        return " ".join(spams)

