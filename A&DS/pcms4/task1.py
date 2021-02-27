global stack, lenstack
stack = []
lenstack = 0

fin = open("stack.in")
fout = open("stack.out", "w")


def plus(x):
    global stack, lenstack
    stack.append(x)
    lenstack += 1


def minus():
    global stack, lenstack
    print(stack[lenstack - 1], file=fout)
    stack.pop(lenstack - 1)
    lenstack -= 1


n = int(fin.readline())
for line in fin:
    inp = line.split()
    if inp[0] == '+':
        plus(int(inp[1]))
    else:
        minus()
