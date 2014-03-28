def sudoku_solved(sudoku):
    for row in sudoku:
        if wrong(row):
            return False
    for i in range(0, 9):
        column = []
        for j in range(0, 9):
            column.append(sudoku[i][j])
        if wrong(column):
            return False
    for k1 in range(0, 9, 3):
        for k2 in range(0, 9, 3):
            square = []
            for i in range(k1, k1+3):
                for j in range(k2, k2+3):
                    square.append(sudoku[i][j])
            if wrong(square):
                return False
    return True


def wrong(list):
    from_one_to_nine = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for number in list:
        if member(number, from_one_to_nine):
            from_one_to_nine.remove(number)
        else:
            return True
    return len(from_one_to_nine) > 0


def member(needle, list):
    for number in list:
        if needle == number:
            return True
    return False
