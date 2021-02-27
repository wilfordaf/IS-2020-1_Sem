def cell_hash_function(value, sizeofhash):
    return value % sizeofhash


def hash_function(word, sizeofhash):
    h = 2
    for char in word:
        h = h * 89 + ord(char)
    return h % sizeofhash


class Cell:
    def __init__(self, size=2):
        self.size = size
        self.data = [[] for i in range(self.size)]
        self.amountofdata = 0

    def exists(self, key):
        return key in self.data[hash_function(key, self.size)]

    def insert(self, key):
        if not self.exists(key):
            self.data[hash_function(key, self.size)].append(key)
            self.amountofdata += 1

    def delete(self, key):
        if self.exists(key):
            self.data[hash_function(key, self.size)].remove(key)
            self.amountofdata -= 1


class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.data = [[] for i in range(self.size)]

    def get(self, key):
        temp = self.data[hash_function(key, self.size)]
        for i in range(len(temp)):
            if temp[i]:
                if temp[i][0] == key:
                    return i
        return None

    def put(self, pair):
        tempindex = self.get(pair[0])
        temphash = hash_function(pair[0], self.size)
        if tempindex is not None:
            self.data[temphash][tempindex][1].insert(pair[1])
        else:
            self.data[temphash].append([pair[0], Cell()])
            self.data[temphash][-1][1].insert(pair[1])

    def deletepair(self, pair):
        tempindex = self.get(pair[0])
        temphash = hash_function(pair[0], self.size)
        if tempindex is not None:
            self.data[temphash][tempindex][1].delete(pair[1])

    def deleteall(self, key):
        tempindex = self.get(key)
        temphash = hash_function(key, self.size)
        if tempindex is not None:
            self.data[temphash][tempindex] = []


fin = open("multimap.in", "r")
fout = open("multimap.txt", "w")
hshtable = HashTable()


def work():
    for line in fin:
        cmd = line.split()
        if cmd[0] == "put":
            hshtable.put(cmd[1:])
        elif cmd[0] == "delete":
            hshtable.deletepair(cmd[1:])
        elif cmd[0] == "get":
            tmpindex = hshtable.get(cmd[1])
            tmphash = hash_function(cmd[1], hshtable.size)
            if tmpindex is not None and hshtable.data[tmphash][tmpindex][1].amountofdata > 0:
                deadinside = hshtable.data[tmphash][tmpindex][1]
                print(deadinside.amountofdata, end=" ", file=fout)
                for i in range(deadinside.size):
                    for h in deadinside.data[i]:
                        print(h, end=" ", file=fout)
                print(file=fout)
            else:
                print(0, file=fout)
        else:
            hshtable.deleteall(cmd[1])


work()
