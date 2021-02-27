global queue, lenqueue
queue = []
lenqueue = 0

fin = open("queue.in")
fout = open("queue.out", "w")


def plus(x):
    global queue, lenqueue
    queue.insert(0, x)
    lenqueue += 1


def minus():
    global queue, lenqueue
    print(queue[lenqueue - 1], file=fout)
    queue.pop(lenqueue - 1)
    lenqueue -= 1


n = int(fin.readline())
for line in fin:
    inp = line.split()
    if inp[0] == '+':
        plus(int(inp[1]))
    else:
        minus()
