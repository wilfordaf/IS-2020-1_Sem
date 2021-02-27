global queue, labels, inputs, registers, ind
queue = []
labels = []
inputs = []
registers = [0]*26
ind = 0


def get():
    number = queue[0]
    queue.pop(0)
    return number


def put(number):
    queue.append(number)


def plus():
    x = get()
    y = get()
    result = (x + y) % 65536
    put(result)


def minus():
    x = get()
    y = get()
    result = (x - y) % 65536
    put(result)


def multiply():
    x = get()
    y = get()
    result = (x * y) % 65536
    put(result)


def division():
    x = get()
    y = get()
    if y == 0:
        result = 0
    else:
        result = x // y
    put(result)


def mod():
    x = get()
    y = get()
    if y == 0:
        result = 0
    else:
        result = x % y
    put(result)


def inregister(register):
    x = get()
    registers[register-97] = x


def fromregister(register):
    x = registers[register-97]
    put(x)


def printnumber():
    number = get()
    print(number, file=fout)


def printregister(register):
    r = registers[register-97]
    print(r, file=fout)


def printaschar():
    c = get() % 256
    print(chr(c), end="", file=fout)


def printregisteraschar(register):
    c = registers[register-97] % 256
    print(chr(c), end="", file=fout)


def labelcheck(label, ind):
    check = True
    for i in range(len(labels)):
        if labels[i] == label:
            check = False
    if check:
        labels.append([label, ind])


def jump(label):
    for i in range(len(labels)):
        if label == labels[i][0]:
            return labels[i][1]


def zero(register, label, ind):
    if registers[register-97] == 0:
        return jump(label)
    else:
        return ind + 1


def equal(register1, register2, label, ind):
    if registers[register1-97] == registers[register2-97]:
        return jump(label)
    else:
        return ind + 1


def greater(register1, register2, label, ind):
    if registers[register1-97] > registers[register2-97]:
        return jump(label)
    else:
        return ind + 1


fin = open("quack.in", "r")
fout = open("quack.out", "w")
i = 0
for line in fin:
    if line[0] == ":":
        labelcheck(line[1:-1], i)
    inputs.append(line)
    i += 1

while ind <= len(inputs) - 1:
    Input = inputs[ind]
    if (ord(Input[0]) < 58) and (ord(Input[0]) > 47):
        put(int(Input) % 65536)
        ind += 1
    elif Input[0] == "+":
        plus()
        ind += 1
    elif Input[0] == "-":
        minus()
        ind += 1
    elif Input[0] == "*":
        multiply()
        ind += 1
    elif Input[0] == "/":
        division()
        ind += 1
    elif Input[0] == "%":
        mod()
        ind += 1
    elif Input[0] == ">":
        inregister(ord(Input[1]))
        ind += 1
    elif Input[0] == "<":
        fromregister(ord(Input[1]))
        ind += 1
    elif Input[0] == "P":
        if (ord(Input[1]) > 96) and (ord(Input[1]) < 123):
            printregister(ord(Input[1]))
        else:
            printnumber()
        ind += 1
    elif Input[0] == "C":
        if (ord(Input[1]) > 96) and (ord(Input[1]) < 123):
            printregisteraschar(ord(Input[1]))
        else:
            printaschar()
        ind += 1
    elif Input[0] == ":":
        ind += 1
    elif Input[0] == "J":
        ind = jump(Input[1:-1])
    elif Input[0] == "Z":
        ind = zero(ord(Input[1]), Input[2:-1], ind)
    elif Input[0] == "E":
        ind = equal(ord(Input[1]), ord(Input[2]), Input[3:-1], ind)
    elif Input[0] == "G":
        ind = greater(ord(Input[1]), ord(Input[2]), Input[3:-1], ind)
    elif Input[0] == "Q":
        break
fout.close()

