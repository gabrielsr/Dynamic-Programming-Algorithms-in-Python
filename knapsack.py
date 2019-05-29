
import math

import numpy

def knap_sack_bin(c, w, W, n):
    z = numpy.empty((n+1, W+1))
    z.fill(-math.inf)
    #
    # s = numpy.empty((n+1, n+1))
    # s.fill(-math.inf)

    for d in range(0, W+1):
        z[0, d] = 0

    for k in range(1, n+1):
        z[k, 0] = 0



    for k in range(1, n+1):
        for d in range(1, W + 1):
            print(z)
            z[k, d] = z[k-1, d]
            if w[k] <= d and c[k] + z[k-1, d-w[k]] > z[k, d]:
                z[k, d] = c[k] + z[k-1, d - w[k]]
    return z[n, W]


def main():
    print("hello")


if __name__== "__main__":
    c = [0, 10, 7, 25, 24]
    w = [0, 2, 1, 6, 5]
    res = knap_sack_bin(c, w, 7, 4)
    print(res)