from random import *
fout = open("input.txt", "w")
for i in range(4):
    print(randint(-100, 100), randint(-100, 100), file=fout)