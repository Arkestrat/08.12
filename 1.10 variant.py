def fx(a, b):
    c = (a+b) ** 3
    return c


m = int(input())
k = int(input())
a1 = m
b1 = 10
a2 = k + m / 5.0
b2 = k + m
f1 = fx(a1, b1)
f2 = fx(a2, b2)
f = f1 - f2
print(f)