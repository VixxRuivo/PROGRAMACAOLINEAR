import random


matriz = [[1, 2, 3], [4, 5, 6],[7, 8, 9]]
resp = False

def magic():
    global resp
    if matriz[0][0] + matriz[1][0] + matriz[2][0] == matriz[0][1] + matriz[1][1] + matriz[2][1] == matriz[0][2] + \
            matriz[1][2] + matriz[2][2] == matriz[0][0] + matriz[0][1] + matriz[0][2] == matriz[1][0] + matriz[1][1] + \
            matriz[1][2] == matriz[2][0] + matriz[2][1] + matriz[2][2] == matriz[0][0] + matriz[1][1] + matriz[2][2] == \
            matriz[0][2] + matriz[1][1] + matriz[2][0]:
        resp = True
    else:
        res = False
    return resp

while resp == False:
    seq = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(3):
        for j in range(3):
            z = random.choice(seq)
            matriz[i][j] = z
            x = seq.index(z)
            seq = seq[:x] + seq[x + 1:]
    magic()
print(matriz)