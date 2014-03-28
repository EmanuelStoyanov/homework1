def member_of_nth_fib_lists(listA, listB, needle):
    fib_list = make_fib_lists(listA, listB, 10)
    for member in fib_list:
        if needle == member:
            return True
    return False


def make_fib_lists(listA, listB, n):
    fib_list = [listA, listB]
    for i in range(2, n+1):
        newfib = fib_list[i-2] + fib_list[i-1]
        fib_list.append(newfib)
    return fib_list
