from math import *


def multiply(v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1] + v2[2] * v1[2]


def lenofvect(v):
    return sqrt(v[0] ** 2 + v[1] ** 2 + v[2] ** 2)


def sinbetweenvect(v1, v2):
    return lenofvect(vectormultiply(v1, v2)) / (lenofvect(v1) * lenofvect(v2))


def cosbetweenvect(v1, v2):
    return multiply(v1, v2) / (lenofvect(v1) * lenofvect(v2))


def anglebetweenvectcos(v1, v2):
    return degrees(acos(cosbetweenvect(v1, v2)))


def anglebetweenvectsin(v1, v2):
    return degrees(asin(sinbetweenvect(v1, v2)))*copysign(1, v1[0] * v2[1] - v1[1] * v2[0])


def vectormultiply(v1, v2):
    return [v1[1] * v2[2] - v1[2] * v2[1], v1[2] * v2[0] - v1[0] * v2[2], v1[0] * v2[1] - v1[1] * v2[0]]


def sign(v1, v2):
    if v1[1] * v2[0] > 0 or v1[0] * v2[1] < 0:
        return -1
    elif v1[1] * v2[0] < 0 or v1[0] * v2[1] > 0:
        return 1
    return 0


fin = open("input.txt", "r")
fout = open("output1.txt", "w")

myshipx, myshipy = [float(x) for x in fin.readline().split()]
vectorx, vectory = [float(x) for x in fin.readline().split()]
mastx, masty = [float(x) for x in fin.readline().split()]
enemyx, enemyy = [float(x) for x in fin.readline().split()]

normalvector = [0, 0, 1]
orientationvector = [vectorx, vectory, 0]
mastvector = [mastx, masty, 1]
enemyvector = [myshipx - enemyx, myshipy - enemyy, 0]

normalship = vectormultiply(normalvector, orientationvector)
gunrotation = anglebetweenvectsin(normalship, enemyvector)
if anglebetweenvectsin(enemyvector, orientationvector) > 0:
    if abs(gunrotation) <= 60:
        print(1, file=fout)
    else:
        print(0, file=fout)
        print("penis")
else:
    if abs(gunrotation) <= 60:
        print(-1, file=fout)
    else:
        print(0, file=fout)
        print("doublepenis")
print(round(gunrotation, 2), file=fout)

mastrotation = anglebetweenvectcos(normalvector, mastvector)
print(round(mastrotation, 2) * sign(orientationvector, mastvector), file=fout)
print("yareyaredaze", file=fout)
