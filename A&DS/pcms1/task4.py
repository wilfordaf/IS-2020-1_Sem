fin = open('smallsort.in', 'r')
fout = open('smallsort.out', 'w')
a = int(fin.readline())
mass = [int(x) for x in fin.readline().split()]
for i in range(a):
    for j in range(a-1-i):
        if int(mass[j]) > int(mass[j+1]):
            mass[j], mass[j+1] = mass[j+1], mass[j]
print(*mass, file = fout)
fout.close()
