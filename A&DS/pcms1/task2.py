fin = open('aplusbin.txt', 'r')
fout = open('aplusbout.txt', 'w')
a = [int(x) for x in fin.readline().split()]
print(a[0]+a[1], file=fout)
fout.close()
