fin = open("brackets.in", "r")
fout = open("brackets.out", "w")

stack = []
ind = True

for line in fin:
    for i in range(len(line)):
        if line[i] == "(" or line[i] == "[":
            stack.append(line[i])
        if line[i] == ")":
            if len(stack) != 0:
                if stack[len(stack) - 1] == "[":
                    ind = False
                else:
                    stack.pop(len(stack) - 1)
            else:
                ind = False
        if line[i] == "]":
            if len(stack) != 0:
                if stack[len(stack) - 1] == "(":
                    ind = False
                else:
                    stack.pop(len(stack) - 1)
            else:
                ind = False
    if len(stack) != 0:
        ind = False
    if ind:
        print("YES", file=fout)
    else:
        print("NO", file=fout)
    ind = True
    stack = []
