r, c, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(3)]
chk = 1


def calcrow():
    mat = []
    maxlen = 0
    length = len(matrix)
    for i in range(len(matrix)):
        cnt = [0] * (length + 1)
        for j in range(len(matrix[i])):
            cnt[matrix[i][j]] += 1
        tmp = []
        while len(tmp) != 200:
            for a in range(1, (length + 1)):
                for b in range(1, (length + 1)):
                    if cnt[b] == a:
                        tmp.append(b)
                        tmp.append(a)
            maxlen = max(maxlen, len(tmp))
            mat.append(tmp)

    for i in range(len(mat)):
        for _ in range(maxlen-len(mat[i])):
            mat[i].append(0)

    return mat


def calccol():
    mat = []
    maxlen = 0
    length = len(matrix[0])
    for i in range(len(matrix[0])):
        cnt = [0] * (length + 1)
        for j in range(len(matrix)):
            cnt[matrix[j][i]] += 1
        tmp = []
        while len(tmp) != 200:
            for a in range(1, (length + 1)):
                for b in range(1, (length + 1)):
                    if cnt[b] == a:
                        tmp.append(b)
                        tmp.append(a)
                        if len(tmp) == 200:
                            break
            maxlen = max(maxlen, len(tmp))
            mat.append(tmp)

    for i in range(len(mat)):
        for _ in range(maxlen-len(mat[i])):
            mat[i].append(0)

    rotmat = [[] for _ in range(len(mat[0]))]
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            rotmat[j].append(mat[i][j])

    return rotmat


for i in range(101):
    for mat in matrix:
        print(*mat)
    print('-----')
    if r-1 < len(matrix) and c-1 < len(matrix[0]):
        if matrix[r-1][c-1] == k:
            print(i)
            chk = 0
            break

    if len(matrix[0]) <= len(matrix):
        matrix = calcrow()

    else:
        matrix = calccol()

if chk:
    print(-1)
