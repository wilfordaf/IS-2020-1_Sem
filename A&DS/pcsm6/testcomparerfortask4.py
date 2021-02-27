import os
fin1 = open("multimap.txt", "r")
fin2 = open("multimapwrong.txt", "r")
for i in range(10):
    os.system('tester.py')
    os.system('task4bst.py')
    os.system('task4.py')
    numofstr = 1
    ind = True
    for line in fin1:
        linecorrect = line.split()
        linewrong = fin2.readline().split()
        if sorted(linecorrect) != sorted(linewrong):
            ind = False
            print(linecorrect, "OK")
            print(linewrong)
            print(numofstr)
        numofstr += 1
    if not ind:
        break

