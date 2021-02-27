def hash_function(word, sizeofhash):
    hshvalue = 0
    tmp = 1
    for char in word:
        hshvalue = (hshvalue + tmp * (ord(char) - ord("a") + 1))
        tmp *= 60
    return hshvalue % sizeofhash


class HashTable:
    def __init__(self, size=10**5):
        self.size = size
        self.data = [[] for i in range(self.size)]

    def get(self, key):
        temp = self.data[hash_function(key, self.size)]
        for i in range(len(temp)):
            if temp[i][0] == key:
                return i
        return None

    def put(self, pair):
        temp = self.get(pair[0])
        if temp is not None:
            self.data[hash_function(pair[0], self.size)][temp][1] = pair[1]
        else:
            self.data[hash_function(pair[0], self.size)].append(pair)

    def delete(self, key):
        temp = self.get(key)
        if temp is not None:
            self.data[hash_function(key, self.size)].pop(temp)


fin = open("map.in", "r")
fout = open("map.out", "w")
hshtable = HashTable()

for line in fin:
    cmd = line.split()
    if cmd[0] == "put":
        hshtable.put([cmd[1], cmd[2]])
    elif cmd[0] == "delete":
        hshtable.delete(cmd[1])
    elif cmd[0] == "get":
        tmpindex = hshtable.get(cmd[1])
        tmphash = hash_function(cmd[1], hshtable.size)
        out = ""
        if tmpindex is not None:
            out += str(hshtable.data[tmphash][tmpindex][1].amountofdata) + " "
            if hshtable.data[tmphash][tmpindex][1].amountofdata != 0:
                for i in range
            print(hshtable.data[tmphash][tmpindex][1], file=fout)
        else:
            print("none", file=fout)
