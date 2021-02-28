class Matrix:
    def __init__(self, length, height, data):
        self.length = length
        self.height = height
        self.data = data


def print_matrix(M):
    out = ""
    i = 0
    while i < len(M.data):
        out += str(M.data[i]) + " "
        if i % M.height == 1:
            out += "\n"
        i += 1
    print(out, file=fout)


def create_matrix(x, y, array):
    matrix = Matrix(x, y, array)
    return matrix


def make_real_matrix(M):
    if M.data == [None]:
        return [None]
    matrix = []
    cnt = 0
    for i in range(M.length):
        matrix.append([])
        for j in range(M.height):
            matrix[i].append(M.data[cnt])
            cnt += 1
    return matrix


def sum_of_matrix(M1, M2):
    if M1.length != M2.length or M1.height != M2.height or M1.data == [None] or M2.data == [None]:
        M3 = create_matrix(1, 1, [None])
        return M3
    newdata = [0] * len(M1.data)
    for i in range(len(M1.data)):
        newdata[i] += M1.data[i] + M2.data[i]
    M3 = create_matrix(M1.length, M1.height, newdata)
    return M3


def multiply_by_const(M, const):
    if M.data == [None]:
        Mnew = create_matrix(1, 1, [None])
        return Mnew
    newdata = [0] * len(M.data)
    for i in range(len(M.data)):
        newdata[i] += M.data[i] * const
    Mnew = create_matrix(M.length, M.height, newdata)
    return Mnew


def multiplication_of_matrix(M1, M2):
    if M1.height != M2.length or M1.data == [None] or M2.data == [None]:
        M3 = create_matrix(1, 1, [None])
        return M3
    newdata = [0] * M1.length * M2.height
    for i in range(M1.length):
        for j in range(M2.height):
            newdata[i*M2.height+j] = 0
            for k in range(M1.height):
                newdata[i * M2.height + j] += M1.data[i*M1.height+k] * M2.data[k*M2.height+j]
    M3 = create_matrix(M1.length, M2.height, newdata)
    return M3


def transpose_matrix(M):
    if M.data == [None]:
        Mnew = create_matrix(1, 1, [None])
        return Mnew
    out = [[0]*M.length]*M.height
    matrix = (make_real_matrix(M))
    newdata = []
    for i in range(M.height):
        for j in range(M.length):

            out[i][j] = matrix[j][i]
            newdata.append(out[i][j])
    Mnew = create_matrix(M.height, M.length, newdata)
    return Mnew


fin = open("input.txt", "r")
fout = open("output.txt", "w")
alpha, beta = [float(x) for x in fin.readline().split()]
na, ma = [int(x) for x in fin.readline().split()]
arr1 = [float(x) for x in fin.readline().split()]
nb, mb = [int(x) for x in fin.readline().split()]
arr2 = [float(x) for x in fin.readline().split()]
nc, mc = [int(x) for x in fin.readline().split()]
arr3 = [float(x) for x in fin.readline().split()]
nd, md = [int(x) for x in fin.readline().split()]
arr4 = [float(x) for x in fin.readline().split()]
nf, mf = [int(x) for x in fin.readline().split()]
arr5 = [float(x) for x in fin.readline().split()]
MatA = create_matrix(na, ma, arr1)
MatB = create_matrix(nb, mb, arr2)
MatC = create_matrix(nc, mc, arr3)
MatD = create_matrix(nd, md, arr4)
MatF = create_matrix(nf, mf, arr5)
X1 = multiply_by_const(transpose_matrix(MatB), beta)
X2 = sum_of_matrix(multiply_by_const(MatA, alpha), X1)
X3 = transpose_matrix(X2)
X4 = multiplication_of_matrix(MatC, X3)
X5 = multiplication_of_matrix(X4, MatD)
X = sum_of_matrix(X5, multiply_by_const(MatF, -1))
if X.data != [None]:
    print(1, file=fout)
    print(X.length, X.height, file=fout)
    print_matrix(X)
else:
    print(0, file=fout)


