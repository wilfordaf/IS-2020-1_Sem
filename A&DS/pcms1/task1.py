fin = open('aplusb.in', 'r')
fout = open('aplusb.out', 'w')
a = [line.split() for line in fin.readlines()]
print(int(a[0][0])+int(a[0][1]), file = fout)
fout.close()
