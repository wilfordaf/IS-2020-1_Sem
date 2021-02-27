def binaryfirst(arr, left, right, x):
    if right >= left:
        mid = left + (right - left) // 2
        if (mid == 0 or x > arr[mid - 1]) and arr[mid] == x:
            return mid
        elif x > arr[mid]:
            return binaryfirst(arr, (mid + 1), right, x)
        else:
            return binaryfirst(arr, left, (mid - 1), x)
    return -1


def binarylast(arr, left, right, x):
    if right >= left:
        mid = left + (right - left) // 2
        if (mid == len(arr) - 1 or x < arr[mid + 1]) and arr[mid] == x:
            return mid
        elif x < arr[mid]:
            return binarylast(arr, left, (mid - 1), x)
        else:
            return binarylast(arr, (mid + 1), right, x)
    return -1


fin = open("binsearch.in", "r")
fout = open("binsearch.out", "w")
n = int(fin.readline())
array = [int(x) for x in fin.readline().split()]
m = int(fin.readline())
request = [int(x) for x in fin.readline().split()]
for i in range(m):
    first = binaryfirst(array, 0, n-1, request[i])
    last = binarylast(array, 0, n-1, request[i])
    if first != -1:
        first += 1
    if last != -1:
        last += 1
    print(first, last, file=fout)