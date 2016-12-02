def binarySearch(alist, lower,upper):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
    print(alist[midpoint])
    if alist[midpoint]>lower and alist[midpoint]< upper:
        return True
    elif alist[midpoint] > upper:
            return binarySearch(alist[:midpoint],lower,upper)
    elif alist[midpoint] < lower:
            return binarySearch(alist[midpoint+1:],lower,upper)

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]

print(binarySearch(testlist, 3,12))
#print(binarySearch(testlist, 13))

