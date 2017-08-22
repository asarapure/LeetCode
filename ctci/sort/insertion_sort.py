def insertionSort(alist):
    for i in range(1, len(alist)):
        element = alist[i]
        pos = i

        while alist[pos - 1] > element and pos > 0:
            alist[pos] = alist[pos - 1]

            pos = pos - 1
        alist[pos] = element



alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print(alist)


#(for and while loops are very powerful)
