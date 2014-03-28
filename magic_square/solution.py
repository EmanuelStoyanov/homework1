def magic_square(matrix):
    k = sum(matrix[0])
    for row in matrix:
        if k != sum(row):
            return False
    for index_column in range(0, len(matrix)):
        sum_column = 0
        for row in matrix:
            sum_column += row[index_column]
        if k != sum_column:
            return False
    sum_main_diagonal = 0
    sum_second_diagonal = 0
    for i in range(0, len(matrix)):
        sum_main_diagonal += matrix[i][i]
        sum_second_diagonal += matrix[i][len(matrix)-i-1]
    if k != sum_main_diagonal or k != sum_second_diagonal:
        return False
    return True

