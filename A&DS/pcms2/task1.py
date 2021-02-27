def merge_sort(array):
    if len(array)>1:
        mid = len(array)//2
        lefthalf = array[:mid]
        righthalf = array[mid:]
        merge_sort(lefthalf)
        merge_sort(righthalf)
        i=0
        j=0
        k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                array[k]=lefthalf[i]
                i=i+1
            else:
                array[k]=righthalf[j]
                j=j+1
            k=k+1
        while i<len(lefthalf):
            array[k]=lefthalf[i]
            i=i+1
            k=k+1
        

        while j<len(righthalf):
            array[k]=righthalf[j]
            j=j+1
            k=k+1

fin = open('sort.in', 'r')
fout = open('sort.out', 'w')
num = int(fin.readline())
array = [int(x) for x in fin.readline().split()]
merge_sort(array)
print(*array, file = fout)
fout.close()
