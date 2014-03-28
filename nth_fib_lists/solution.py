def nth_fib_lists(listA, listB, n):
    fib_list = [listA, listB]
    for i in range(2, n+1):
        newfib = fib_list[i-2] + fib_list[i-1]
        fib_list.append(newfib)
    return fib_list[n-1]
