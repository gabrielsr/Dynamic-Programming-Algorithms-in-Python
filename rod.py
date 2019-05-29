
import math


def rod_button_up(p, n):
    r = [None] * (n + 1)
    s = [None] * (n + 1)
    r[0]=0
    for j in range(1, n+1):
        q = -math.inf
        for i in range(1, j+1):
            if q < p[i] + r[j-i]:
                q = p[i] + r[j-i]
                s[j] = i
        r[j]=q
    return r, s


def main():
    print("hello")


if __name__== "__main__":
    p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    res = rod_button_up(p, 7)
    print(res)