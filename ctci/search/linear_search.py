def linSearch(alist, num) :
    for each in alist :
        if each == num :
            return True
    return False

print(linSearch([3,6,3,5,21,32], 5))


def linearSearch(alist, num):
    for i in range(len(alist)):
        if alist[i] == num :
            return i
    return False

print(linearSearch([4,56,34,76,23], 34))