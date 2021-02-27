fin = open('antiqs.in', 'r')
fout = open('antiqs.out', 'w')
num = int(fin.readline())
array = [0]*num
for i in range(num):
    array[i] = i+1
for i in range(2,num):
    tmp = array[i//2]
    array[i//2] = array[i]
    array[i] = tmp
print(*array, file = fout)
fout.close()
