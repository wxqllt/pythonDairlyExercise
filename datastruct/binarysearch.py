def binarysearch(l,key):
    start = 0
    end = len(l)-1
    i = 0
    while(start<= end):
        i = i + 1
        mid = start + ((end - start)//2)
        if(l[mid]<key):
            start = mid + 1
        elif(l[mid]>key):
            end = mid - 1
        else:
            return mid
    return -1

if ( __name__ == '__main__'):
    # l = [1, 2, 3, 4, 5]
    l = range(0,20,2)
    m = list(l)
    # print(range(0,10,2))
    print(m)
    print(binarysearch(m,8))

