import numpy

def subset_sum(p, S):
    # z = numpy.empty((n+1, K+1))
    n = len(p)
    #z = numpy.empty((n + 1, S + 1))
    #z = [[0 for x in range(n)] for y in range(K)]
    z = {}

    for d in range(0, S+1):
        z[0, d] = False

    for k in range(1, n+1):
        z[k, 0] = False

    for k in range(1, n+1):
        for d in range(1, S + 1):
            z[k, d] = z[k-1, d] or p[k-1] == d or (p[k-1] < d and z[k-1, d-p[k-1]])
        if z[k, S] : return True;
    printx(p, S, z)
    return False


def main():
    print("hello")

def printx(p, S, z) :
    for i in range(0, len(p)+1):
        print(p[i-1])
        print(":")
        for j in range(0, S + 1):
            print(z[i, j])
        print("\n")


if __name__== "__main__":
    S = int(input())
    line = input()
    p = list(map(int,  line.split()))
    res = subset_sum(p, S)
    print(res)

    # c = [0, 10, 7, 25, 24]
    # w = [0, 2, 1, 6, 5]
    # res = knap_sack_bin(c, w, 7, 4)
    # print(res)