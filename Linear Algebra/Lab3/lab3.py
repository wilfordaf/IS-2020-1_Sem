class Dot:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def printmyselfdot(self):
        print("(", self.x, ";", self.y, ";", self.z, ")", sep="")


class Plain:
    def __init__(self, A, B, C, D):
        self.A = A
        self.B = B
        self.C = C
        self.D = D

    def printmyselfplain(self):
        print(self.A, "*x +", self.B, "*y +", self.C, "*z +", self.D)


def innerproduct(v1, v2):
    return v1.x * v2.x + v1.y * v2.y + v1.z * v2.z


def const(v1, num):
    return Dot(v1.x * num, v1.y * num, v1.z * num)


def subtraction(v1, v2):
    return Dot(v1.x - v2.x, v1.y - v2.y, v1.z - v2.z)


def createplain(d0, d1, d2):
    p = Plain(((d1.y - d0.y) * (d2.z - d0.z) - (d2.y - d0.y) * (d1.z - d0.z)),
              ((d2.x - d0.x) * (d1.z - d0.z) - (d1.x - d0.x) * (d2.z - d0.z)),
              ((d1.x - d0.x) * (d2.y - d0.y) - (d2.x - d0.x) * (d1.y - d0.y)),
              d0.x * (-(d1.y - d0.y) * (d2.z - d0.z) + (d2.y - d0.y) * (d1.z - d0.z)) +
              d0.y * (-(d2.x - d0.x) * (d1.z - d0.z) + (d1.x - d0.x) * (d2.z - d0.z)) +
              d0.z * (-(d1.x - d0.x) * (d2.y - d0.y) + (d2.x - d0.x) * (d1.y - d0.y)))
    return p


def intersectionoflineandplain(dot, vector, plain):
    if (plain.D + plain.A * dot.x + plain.B * dot.y + plain.C * dot.z) == 0 or (
            plain.A * vector.x + plain.B * vector.y + plain.C * vector.z) == 0:
        return False
    t = -((plain.D + plain.A * dot.x + plain.B * dot.y + plain.C * dot.z) / (
            plain.A * vector.x + plain.B * vector.y + plain.C * vector.z))
    if t <= 0:
        return False
    return Dot(dot.x + t * vector.x, dot.y + t * vector.y, dot.z + t * vector.z)


def lenghtbetweendots(dot1, dot2):
    return ((dot2.x - dot1.x) ** 2 + (dot2.y - dot1.y) ** 2 + (dot2.z - dot1.z) ** 2) ** 0.5


def lenofvect(v):
    return (v.x ** 2 + v.y ** 2 + v.z ** 2) ** 0.5


def mirroredvector(vector, plain):
    normalplain = Dot(plain.A, plain.B, plain.C)
    l = lenofvect(normalplain)
    n = Dot(plain.A/l, plain.B/l, plain.C/l)
    scalarmp = innerproduct(vector, n)
    subtracted = const(n, scalarmp * 2)
    return Dot(vector.x - subtracted.x, vector.y - subtracted.y, vector.z - subtracted.z)


fin = open("input.txt", "r")
fout = open("output.txt", "w")

Ax, Ay, Az = [float(x) for x in fin.readline().split()]
Bx, By, Bz = [float(x) for x in fin.readline().split()]
Cx, Cy, Cz = [float(x) for x in fin.readline().split()]
Dx, Dy, Dz = [float(x) for x in fin.readline().split()]
vinx, viny, vinz = [float(x) for x in fin.readline().split()]
v0x, v0y, v0z = [float(x) for x in fin.readline().split()]
energy = int(fin.readline())
n = int(fin.readline())

A = Dot(Ax, Ay, Az)
B = Dot(Bx, By, Bz)
C = Dot(Cx, Cy, Cz)
D = Dot(Dx, Dy, Dz)
E = Dot(C.x+subtraction(A, B).x, C.y+subtraction(A, B).y, C.z+subtraction(A, B).z)
F = Dot(E.x, E.y, Dz)
G = Dot(Ax, Ay, Dz)
H = Dot(Bx, By, Dz)
vect = Dot(vinx, viny, vinz)
vin = Dot(v0x, v0y, v0z)
# vin.printmyselfdot()
# vect.printmyselfdot()

arrayofdots = []
arrayofmirrors = []
arrayofedges = [createplain(A, B, C), createplain(B, C, D), createplain(D, C, E), createplain(A, B, H),
                createplain(A, E, F), createplain(H, D, F)]

# A.printmyselfdot()
# B.printmyselfdot()
# C.printmyselfdot()
# D.printmyselfdot()
# E.printmyselfdot()
# F.printmyselfdot()
# G.printmyselfdot()
# H.printmyselfdot()


for i in range(n):
    for j in range(3):
        dx, dy, dz = [float(x) for x in fin.readline().split()]
        arrayofdots.append(Dot(dx, dy, dz))
for i in range(n):
    p = createplain(arrayofdots[i * 3], arrayofdots[i * 3 + 1], arrayofdots[i * 3 + 2])
    arrayofmirrors.append(p)

infoaboutmirror1 = [0] * n  # 1 - точка пересеч, 2 - длина до точки пересеч, 3 - отраж вектор
infoaboutmirror2 = [0] * n
infoaboutmirror3 = [0] * n
infoaboutedges1 = [0] * 6  # 1 - точка пересечения, 2 - длина до точки пересечения
infoaboutedges2 = [0] * 6
oldvect = vect
olddot = vin
bool = True
while energy > 0:
    # olddot.printmyselfdot()
    # oldvect.printmyselfdot()
    for i in range(len(arrayofmirrors)):
        same = intersectionoflineandplain(olddot, oldvect, arrayofmirrors[i])
        infoaboutmirror1[i] = same
        if same is not False:
            infoaboutmirror2[i] = lenghtbetweendots(olddot, same)
            infoaboutmirror3[i] = mirroredvector(oldvect, arrayofmirrors[i])
        else:
            infoaboutmirror2[i] = 10 ** 9
            infoaboutmirror3[i] = False
    minlenght = min(infoaboutmirror2)
    number = infoaboutmirror2.index(minlenght)
    # print(infoaboutmirror1)
    # print(infoaboutmirror2)
    # print(infoaboutmirror3)
    for i in range(6):
        intersection = intersectionoflineandplain(olddot, oldvect, arrayofedges[i])
        infoaboutedges1[i] = intersection
        if intersection is not False:
            infoaboutedges2[i] = lenghtbetweendots(olddot, intersection)
            # print(infoaboutedges1)
            # print(infoaboutedges2)
            if lenghtbetweendots(olddot, intersection) < minlenght:
                print("1", file=fout)
                print(energy, file=fout)
                print(round(intersection.x, 2), round(intersection.y, 2), round(intersection.z, 2), file=fout)
                print(round(oldvect.x, 2), round(oldvect.y, 2), round(oldvect.z, 2), file=fout)
                bool = False
                break
        else:
            infoaboutedges2[i] = 10 ** 9
    if not bool:
        break
    olddot = infoaboutmirror1[number]
    oldvect = infoaboutmirror3[number]
    energy -= 1
if bool:
    print("0", file=fout)
    print(round(olddot.x, 2), round(olddot.y, 2), round(olddot.z, 2), file=fout)
