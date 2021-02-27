def heighttree(treeleft, treeright):
    maxheight = 0
    s1 = [1]
    s2 = [0]
    while len(s1) != 0:
        i = s1.pop(len(s1) - 1)
        height = s2.pop(len(s2) - 1)
        left, right = treeleft[i], treeright[i]
        maxheight = max(maxheight, height + 1)
        if left != 0:
            s1.append(left)
            s2.append(height + 1)
        if right != 0:
            s1.append(right)
            s2.append(height + 1)
    return maxheight


fin = open("height.in", "r")
fout = open("height.out", "w")
n = int(fin.readline())
t1 = [0]*(n+1)
t2 = [0]*(n+1)
h = 0
for k in range(1, n + 1):
    tmp, t1[k], t2[k] = [int(x) for x in fin.readline().split()]
if n > 0:
    h = heighttree(t1, t2)
print(h, file=fout)
