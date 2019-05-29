import numpy

def cannon(x, y,K, n):
    # z = numpy.empty((n+1, K+1))
    z = numpy.empty((n + 1, K + 1))
    #z = [[0 for x in range(n)] for y in range(K)]
    #z = {}

    for d in range(0, K+1):
        z[0, d] = 0

    for k in range(1, n+1):
        z[k, 0] = 0

    for k in range(1, n+1):
        for d in range(1, K + 1):
            z[k, d] = z[k-1, d]
            if x[k-1] <= d and y[k-1] + z[k-1, d-x[k-1]] > z[k, d]:
                z[k, d] = y[k-1] + z[k-1, d - x[k-1]]
    return z[n, K]


def main():
    print("hello")


if __name__== "__main__":
    tests = int(input())
    for t in range(0, tests):
        n = int(input())
        X = []
        Y = []
        for b in range(0, n):
            line = input()
            y, x = (int(i) for i in line.split())
            X.append(x)
            Y.append(y)
        K = int(input())
        R = int(input())
        res = cannon(X, Y, K, n)
        if res >= R:
            print("Missao completada com sucesso")
        else:
            print("Falha na missao")

    # c = [0, 10, 7, 25, 24]
    # w = [0, 2, 1, 6, 5]
    # res = knap_sack_bin(c, w, 7, 4)
    # print(res)