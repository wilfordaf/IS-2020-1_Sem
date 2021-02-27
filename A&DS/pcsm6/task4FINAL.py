def hash_function(self, word):
    h = 293
    for char in word:
        h = h * 89 + ord(char)
    return h % self.size


class HashTable:
    def __init__(self, size=10 ** 5):
        self.size = size
        self.data = [[] for _ in range(self.size)]

    def get(self, key):
        temp = self.data[self.hashf(self, key)]
        for i in range(len(temp)):
            if temp[i]:
                if temp[i][0] == key:
                    return i
        return None

    def put(self, pair):
        tempindex = self.get(pair[0])
        temphash = self.data[self.hashf(self, pair[0])]
        if tempindex is not None:
            temphash[tempindex][1].insert(pair[1])
        else:
            newbst = Node(pair[1])
            temphash.append([pair[0], newbst])

    def deletepair(self, pair):
        tempindex = self.get(pair[0])
        temphash = self.data[self.hashf(self, pair[0])]
        if tempindex is not None:
            temphash[tempindex][1] = delete(temphash[tempindex][1], pair[1])
            if temphash[tempindex][1] is None:
                del temphash[tempindex]

    def deleteall(self, key):
        tempindex = self.get(key)
        temphash = self.data[self.hashf(self, key)]
        if tempindex is not None:
            del temphash[tempindex]


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, key):
        if self.key is not None:
            if key < self.key:
                if self.left is None:
                    self.left = Node(key)
                else:
                    self.left.insert(key)
            elif key > self.key:
                if self.right is None:
                    self.right = Node(key)
                else:
                    self.right.insert(key)
        else:
            self.key = key

    def printtree(self):
        out = self.key
        if self.left:
            out += " " + self.left.printtree()
        if self.right:
            out += " " + self.right.printtree()
        return out

    def amountofelements(self):
        cnt = 1
        if self.left and self.left.key:
            cnt += self.left.amountofelements()
        if self.right and self.right.key:
            cnt += self.right.amountofelements()
        return cnt


def minnode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current


def delete(root, key):
    if root is None:
        return root
    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        if root.right is None:
            temp = root.left
            root = None
            return temp
        temp = minnode(root.right)
        root.key = temp.key
        root.right = delete(root.right, temp.key)
    return root


def exists(node, key):
    if node is None:
        return False
    if node.key is key:
        return True
    l = exists(node.left, key)
    if l:
        return True
    r = exists(node.right, key)
    return r


fin = open("multimap.in", "r")
fout = open("multimap.out", "w")
hshtable = HashTable()
hshtable.hashf = hash_function


def work():
    for line in fin:
        cmd = line.split()
        if cmd[0] == "put":
            hshtable.put(cmd[1:])
        elif cmd[0] == "delete":
            hshtable.deletepair(cmd[1:])
        elif cmd[0] == "get":
            tmpindex = hshtable.get(cmd[1])
            tmphash = hshtable.data[hshtable.hashf(hshtable, cmd[1])]
            if tmpindex is not None:
                tree = tmphash[tmpindex][1]
                print(tree.amountofelements(), tree.printtree(), file=fout)
            else:
                print(0, file=fout)
        else:
            hshtable.deleteall(cmd[1])


work()
