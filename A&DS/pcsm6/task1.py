def hash_function(value, sizeofhash):
    return abs(value) % sizeofhash


class HashTable:
    def __init__(self, size=400000):
        self.size = size
        self.data = [[] for i in range(self.size)]

    def exists(self, key):
        return key in self.data[hash_function(key, self.size)]

    def insert(self, key):
        if not self.exists(key):
            self.data[hash_function(key, self.size)].append(key)

    def delete(self, key):
        if self.exists(key):
            self.data[hash_function(key, self.size)].remove(key)


fin = open("set.in", "r")
fout = open("set.out", "w")
hshtable = HashTable()
for line in fin:
    task = line[0]
    x = int(line[7:-1])
    if task == "i":
        hshtable.insert(x)
    elif task == "e":
        if hshtable.exists(x):
            print("true", file=fout)
        else:
            print("false", file=fout)
    elif task == "d":
        hshtable.delete(x)