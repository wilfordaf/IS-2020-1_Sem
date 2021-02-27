fin = open('isheap.in', 'r')
fout = open('isheap.out', 'w')
n = int(fin.readline())
array = [int(x) for x in fin.readline().split()]
a = [0]*(n+1)
for i in range(n):
    a[i+1] = array[i]
ind = True
for i in range(1, n+1):
    if 2 * i <= n and a[i] > a[2 * i]:
        ind = False
        break
    if 2 * i + 1 <= n and a[i] > a[2 * i + 1]:
        ind = False
        break
print("YES" if ind else "NO", file=fout)
fout.close()
