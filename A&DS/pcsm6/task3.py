def hash_function(word, sizeofhash):
    hshvalue = 0
    tmp = 1
    for char in word:
        hshvalue = (hshvalue + tmp * (ord(char) - ord("a") + 1))
        tmp *= 2
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

    def put(self, arr):
        tempindex = self.get(arr[0])
        temphash = hash_function(arr[0], self.size)
        if tempindex is not None:
            self.data[temphash][tempindex][1] = arr[1]
            return self.data[temphash][tempindex], False  # isn`t a new elem, no need to change previous
        else:
            self.data[temphash].append(arr)
            return self.data[temphash][-1], True

    def delete(self, arr):
        tempindex = self.get(arr[0])
        temphash = hash_function(arr[0], self.size)
        if arr[3] is not None:
            arr[3][2] = arr[2]  # if next exists, prev for this elem becomes prev for next
        if arr[2] is not None:
            arr[2][3] = arr[3]  # if prev exists, next for this elem becomes next for prev
        self.data[temphash].pop(tempindex)


fin = open("linkedmap.in", "r")
fout = open("linkedmap.out", "w")
hshtable = HashTable()
previous = None
for line in fin:
    cmd = line.split()
    if cmd[0] == "put":
        arrayofinput = [cmd[1], cmd[2], None, None]  # key, value, next, previous
        if previous is not None:
            arrayofinput[2] = previous
        current, bool = hshtable.put(arrayofinput)
        if bool:
            if previous is not None:
                previous[3] = current
            previous = current

    elif cmd[0] == "delete":
        tmpindex = hshtable.get(cmd[1])
        tmphash = hash_function(cmd[1], hshtable.size)
        if tmpindex is not None:
            if previous == hshtable.data[tmphash][tmpindex]:
                previous = hshtable.data[tmphash][tmpindex][2]
            hshtable.delete(hshtable.data[tmphash][tmpindex])

    elif cmd[0] == "get":
        tmpindex = hshtable.get(cmd[1])
        tmphash = hash_function(cmd[1], hshtable.size)
        if tmpindex is not None:
            print(hshtable.data[tmphash][tmpindex][1], file=fout)
        else:
            print("none", file=fout)

    elif cmd[0] == "prev":
        tmpindex = hshtable.get(cmd[1])
        tmphash = hash_function(cmd[1], hshtable.size)
        if tmpindex is not None:
            prev = hshtable.data[tmphash][tmpindex][2]
            if prev is not None:
                print(prev[1], file=fout)
            else:
                print("none", file=fout)
        else:
            print("none", file=fout)

    elif cmd[0] == "next":
        tmpindex = hshtable.get(cmd[1])
        tmphash = hash_function(cmd[1], hshtable.size)
        if tmpindex is not None:
            next = hshtable.data[tmphash][tmpindex][3]
            if next is not None:
                print(next[1], file=fout)
            else:
                print("none", file=fout)
        else:
            print("none", file=fout)

