def garland(left, right):
    while right - left > 10 ** (-6):
        h[1] = (left + right) / 2
        ind = True
        for i in range(2, int(n)):
            h[i] = 2 * h[i - 1] - h[i - 2] + 2
            if h[i] < 0:
                ind = False
                break
        if ind:
            right = h[1]
        else:
            left = h[1]
    print(left, right)
    print(h)
    return h[int(n)-1]


fin = open("garland.in", "r")
fout = open("garland.out", "w")
n, A = [float(x) for x in fin.readline().split()]
h = [0]*int(n)
h[0] = A
out = garland(0, h[0])
print(float('{:.3f}'.format(out)), file=fout)