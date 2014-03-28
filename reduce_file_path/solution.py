def reduce_file_path(path):
    array = path.split('/')
    badindexes = []
    for i in range(1, len(array)):
        if array[i] == '..':
            badindexes.append(i-1)
    badindexes.reverse()
    for i in badindexes:
        array.pop(i)
    for i in range(len(array)-1, -1, -1):
        if array[i] == '' or array[i] == '.' or array[i] == '..':
            array.pop(i)
    return '/' + '/'.join(array)
