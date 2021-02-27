fin = open("postfix.in", "r")
fout = open("postfix.out", "w")

stack = []
cycle = 0

for i in fin.readline():
    if i != " ":
        if i == "+":
            stack[cycle - 2] = int(stack[cycle - 1]) + int(stack[cycle - 2])
            stack.pop(cycle - 1)
            cycle -= 2
        elif i == "-":
            stack[cycle - 2] = int(stack[cycle - 2]) - int(stack[cycle - 1])
            stack.pop(cycle - 1)
            cycle -= 2
        elif i == "*":
            stack[cycle - 2] = int(stack[cycle - 1]) * int(stack[cycle - 2])
            stack.pop(cycle - 1)
            cycle -= 2
        else:
            stack.append(i)
        cycle += 1
print(stack[0], file=fout)

