class Node:
    def __init__(self, key, left, right):
        self.left = left
        self.right = right
        self.key = key


def check(tree):
    if len(tree) == 1:
        return True
    s1 = [1]
    s2 = [-10**9]
    s3 = [10**9]
    while len(s1) != 0:
        x1 = s1.pop(len(s1)-1)
        x2 = s2.pop(len(s2)-1)
        x3 = s3.pop(len(s3)-1)
        if tree[x1].key <= x2 or tree[x1].key >= x3:
            return False
        if tree[x1].left != 0:
            s1.append(tree[x1].left)
            s2.append(x2)
            s3.append(tree[x1].key)
        if tree[x1].right != 0:
            s1.append(tree[x1].right)
            s2.append(tree[x1].key)
            s3.append(x3)
    return True


fin = open("check.in", "r")
fout = open("check.out", "w")
n = int(fin.readline())
t = [0]*(n+1)
for k in range(1, n+1):
    value, l, r = [int(x) for x in fin.readline().split()]
    t[k] = Node(value, l, r)
if check(t):
    print("YES", file=fout)
else:
    print("NO", file=fout)