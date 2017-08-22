def binarySearch(alist, num) :
    mid = len(alist)//2
    low = 0
    high = len(alist) - 1
    # print(mid)
    while low <= high :
        if num == alist[mid]:
            return mid
        elif num < alist[mid]:
            high = mid - 1
            mid = (low + high)//2
        elif num > alist[mid]:
            low = mid + 1
            mid = (low + high)//2
    return False


print(binarySearch([2,4,6,34,65,78,99], 100))