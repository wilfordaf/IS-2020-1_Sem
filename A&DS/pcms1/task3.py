fin = open('turtlein.txt', 'r')
fout = open('turtleout.txt', 'w')
spec = [int(x) for x in fin.readline().split()]
n = spec[0]*spec[1]
num = [0] * spec[0]
for i in range(spec[0]):
    num[i] = [0] * spec[1]
for i in range(spec[0]):
    string = [int(x) for x in fin.readline().split()]
    num[i] = string



for i in range(1,spec[0]):
    num[i][0] += num[i][0]
for i in range(1, spec[1]):
    num[spec[0]-1][i] += num[spec[0]-1][i-1]

for i in range(0, spec[0]-1):
    for j in range(1, spec[1]):
        if num[i+1][j] > num[i][j-1]:
            num[i][j] += num[i+1][j]
        else:
            num[i][j] += num[i][j-1]
print(num[0][spec[1]-1], file = fout)
fout.close()
