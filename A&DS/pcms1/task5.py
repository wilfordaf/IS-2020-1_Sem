fin = open('sortland.in', 'r')
fout = open('sortland.out', 'w')
a = int(fin.readline())
mass = [float(x) for x in fin.readline().split()]
num = []
for i in range(1,a+1):
    num.append(i)
for i in range(a):
    for j in range(a-1-i):
        if int(mass[j]) > int(mass[j+1]):
            mass[j], mass[j+1] = mass[j+1], mass[j]
            num[j], num[j+1] = num[j+1], num[j]
print(num[0], num[(a-1)//2], num[a-1], file = fout)
fout.close()
