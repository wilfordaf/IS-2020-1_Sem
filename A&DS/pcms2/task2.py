def merge_sort(array1,array2):
    if len(array1)>1:
        mid = len(array1)//2
        lefthalf1 = array1[:mid]
        righthalf1 = array1[mid:]
        lefthalf2 = array2[:mid]
        righthalf2 = array2[mid:]
        merge_sort(lefthalf1, lefthalf2)
        merge_sort(righthalf1, righthalf2)
        i=0
        j=0
        k=0
        while i<len(lefthalf1) and j<len(righthalf1):
            if lefthalf1[i]<=righthalf1[j]:
                array1[k]=lefthalf1[i]
                array2[k]=lefthalf2[i]
                i=i+1
            else:
                array1[k]=righthalf1[j]
                array2[k]=righthalf2[j]
                j=j+1
            k=k+1
        while i<len(lefthalf1):
            array1[k]=lefthalf1[i]
            array2[k]=lefthalf2[i]
            i=i+1
            k=k+1
        

        while j<len(righthalf1):
            array1[k]=righthalf1[j]
            array2[k]=righthalf2[j]
            j=j+1
            k=k+1


fin = open('race.in', 'r')
fout = open('race.out', 'w')
num = int(fin.readline())
cntr = [""]*num
sports = [""]*num
for i in range(num):
    country, surname = [str(x) for x in fin.readline().split()]
    cntr[i] = country
    sports[i] = surname
merge_sort(cntr, sports)

print("=== " +cntr[0]+ " ===", file=fout)
print(sports[0], file=fout)
for i in range(1, num):
    if cntr[i] != cntr[i-1]:
        print("=== " +cntr[i]+ " ===", file=fout)
    print(sports[i], file=fout)
fout.close()    
    

