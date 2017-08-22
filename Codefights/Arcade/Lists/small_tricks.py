__author__ = 'asarapure'

def listBeautifier(a):
    res = a[:]
    while res and res[0] != res[-1]:
        a_,*res,a = res  #Check this way of assignment for lists.
    return res

#Remove elements till first and last element are the same.
a = [3, 4, 2, 4, 38, 4, 5, 3, 2]
print(listBeautifier(a))  # = [4, 38, 4]


###################################################

