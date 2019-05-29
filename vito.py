
import math

import numpy

def vito(S, E, I):

    tend = E[-1]
    n = len(E)

    z = numpy.empty((n, tend+1))
    z.fill(-math.inf)

    for j in range(0, tend+1):
        z[0, j] = 0

    for i in range(0, n):
        z[i, 0] = 0

    # linha a linha (cada programa)
    for i in range(1, n):
        # olha a tabela até aqui
        q = -math.inf
        for j in range(1, tend+1):
            if j == E[i]:
                q = z[i, S[i]] + I[i]
            z[i,j] = max(z[i-1, j], q)
    return z[n-1, tend], z


def main():
    print("hello")


if __name__== "__main__":
    res = vito([0, 0, 1, 1, 2, 3, 4], [0, 1, 3, 4, 5, 6, 7], [0, 1, 7, 9, 12, 6, 5])
    print(res)