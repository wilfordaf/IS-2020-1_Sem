def buildheap(arr, n, i):
    greater = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        greater = l
    if r < n and arr[greater] < arr[r]:
        greater = r
    if greater != i:
        arr[i], arr[greater] = arr[greater], arr[i]
        buildheap(arr, n, greater)


def heap_sort(arr):
    n = len(arr)
    for i in range(n, -1, -1):
        buildheap(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        buildheap(arr, i, 0)


fin = open('sort.in', 'r')
fout = open('sort.out', 'w')
n = int(fin.readline())
array = [int(x) for x in fin.readline().split()]
heap_sort(array)
print(*array, file=fout)
fout.close()