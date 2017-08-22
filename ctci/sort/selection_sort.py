li = [113 , 117 , 97 , 100 , 114 , 108 , 116 , 105 , 99]


def selection(li):
    for j in range( len(li) - 1, 0, -1):
        max = -1
        for i in range(0, j):
            if (li[i] > max):
                max = li[i]
        li[j], li[li.index(max)] = max, li[j]


selection(li)

#(with max at the end )
