class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, key):
        if self.key != 0:
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


def next(root, key):
    minim = 10 ** 9
    if root is None:
        return "none"
    tmp = root
    while True:
        if tmp.key <= key:
            if tmp.right is not None:
                tmp = tmp.right
            else:
                break
        else:
            if tmp.key < minim:
                minim = tmp.key
            if tmp.left is not None:
                tmp = tmp.left
            else:
                break
    if minim == 10 ** 9:
        return "none"
    return minim


def prev(root, key):
    maxim = -10 ** 9
    if root is None:
        return "none"
    tmp = root
    while True:
        if tmp.key >= key:
            if tmp.left is not None:
                tmp = tmp.left
            else:
                break
        else:
            if tmp.key > maxim:
                maxim = tmp.key
            if tmp.right is not None:
                tmp = tmp.right
            else:
                break
    if maxim == -10 ** 9:
        return "none"
    return maxim


def exists(node, key):
    if node is None:
        return "false"
    if node.key is key:
        return "true"
    l = exists(node.left, key)
    if l == "true":
        return "true"
    r = exists(node.right, key)
    return r


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


fin = open("bstsimple.in", "r")
fout = open("bstsimple.out", "w")
tree = None
for line in fin:
    task, x = line.split()
    if task == "insert":
        if tree is None:
            tree = Node(int(x))
        else:
            tree.insert(int(x))
    if task == "delete":
        tree = delete(tree, int(x))
    elif task == "exists":
        print(exists(tree, int(x)), file=fout)
    elif task == "next":
        print(next(tree, int(x)), file=fout)
    elif task == "prev":
        print(prev(tree, int(x)), file=fout)