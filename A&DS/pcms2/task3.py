def merge_sort(array,inv):
    if len(array) == 1:
        return 0
    if len(array)>1:
        mid = len(array)//2
        lefthalf = array[:mid]
        righthalf = array[mid:]
        cntl = merge_sort(lefthalf,inv)
        cntr = merge_sort(righthalf,inv)
        cnt = 0
        i = 0
        j = 0
        k = 0
        t = 0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<=righthalf[j]:
                array[k]=lefthalf[i]
                t += 1
                i += 1
            else:
                array[k]=righthalf[j]
                inv += len(lefthalf)-t
                j += 1
            k += 1
        while i<len(lefthalf):
            array[k]=lefthalf[i]
            i += 1
            k += 1
        

        while j<len(righthalf):
            array[k]=righthalf[j]
            j += 1
            k += 1
        cnt = inv + cntl + cntr
        return cnt

fin = open('inversions.in', 'r')
fout = open('inversions.out', 'w')
num = int(fin.readline())
array = [int(x) for x in fin.readline().split()]
inv = 0
print(merge_sort(array,inv), file = fout)
fout.close()
