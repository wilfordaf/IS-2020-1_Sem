def merge(arr, left, mid, right, helper):
    i, j = 0, 0
    merged = []
    while (i + left <= mid) and (j + mid < right):
        if arr[i + left][helper] <= arr[j + mid + 1][helper]:
            merged.append(arr[i + left])
            i += 1
        else:
            merged.append(arr[j + mid + 1])
            j += 1
    while i + left <= mid:
        merged.append(arr[i + left])
        i += 1
    while j + mid < right:
        merged.append(arr[j + mid + 1])
        j += 1
    arr[left:right + 1] = merged


def merge_sort(arr, left, right, helper):
    if right - left < 1:
        return
    mid = (left + right) // 2

    merge_sort(arr, left, mid, helper)
    merge_sort(arr, mid + 1, right, helper)
    merge(arr, left, mid, right, helper)


fin = open('radixsort.in', 'r')
fout = open('radixsort.out', 'w')

n, m, k = [int(x) for x in fin.readline().split()]

words = []
for i in range(n):
    words.append(fin.readline().rstrip('\n'))
print(words)
for i in range(k):
    merge_sort(words, 0, n - 1, - i - 1)
for i in range(n):
    print(words[i], file=fout)

fout.close()
