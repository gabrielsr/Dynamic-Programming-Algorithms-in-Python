
import math

import numpy

def matrix_chain_order(p):
    n = len(p)-1
    m = numpy.empty((n+1, n+1))
    m.fill(-math.inf)

    s = numpy.empty((n+1, n+1))
    s.fill(-math.inf)

    for i in range(1, n+1):
        m[i, i] = 0

    for l in range(2, n+1):
        for i in range(1, n - l + 1 + 1):
            j = i + l - 1
            m[i][j] = math.inf
            for k in range(i, j - 1 +1):
                q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    return m, s



def main():
    print("hello")


if __name__== "__main__":
    p = [30, 35, 15, 5, 10, 20, 25]
    res = matrix_chain_order(p)
    print(res)