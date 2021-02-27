from random import *
fout = open("multimap.in", "w")
array = ["put", "get", "delete", "deleteall"]
for i in range(1000000):
    task = array[randint(0, 3)]
    if task == "put":
        print("put", randint(0, 100), randint(0, 100), file=fout)
    elif task == "delete":
        print("delete", randint(0, 100), randint(0, 100), file=fout)
    elif task == "get":
        print("get", randint(0, 100), file=fout)
    elif task == "deleteall":
        print("deleteall", randint(0, 100), file=fout)


