li = [113 , 117 , 97 , 100 , 114 , 108 , 116 , 105 , 99]


def bubble(li):
    swaps = True
    j = 0
    p = len(li)
    for j in range(len(li) - 1) :
        p -=1
        for i in range(0, p):
            if (li[i] > li[i+1]):
                li[i], li[i+1] = li[i+1], li[i]

bubble(li)


def bub2(li) :
    for k in

        for i in range(len(li) - 1):
            if li[i] > li[i + 1] :
                li[i], li[i + 1] = li[i]





