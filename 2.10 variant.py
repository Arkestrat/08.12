import math


def fx(a, b, c):
    c = 2 * a - b * math.sin(c)/5 + abs(c)
    return c


S = int(input())
t = int(input())
a1 = t
a2 = 2 * S
a3 = 1/17.0
b1 = 22
b2 = t
b3 = S = t
f1 = fx(a1, a2, a3)
f2 = fx(b1, b2, b3)
f = f1 + f2
print(f)    