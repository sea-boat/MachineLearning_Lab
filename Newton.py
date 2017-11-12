def h(x):
    return x * x * x + 2 * x * x + 3 * x + 4


def h1(x):
    return 3 * x * x + 4 * x + 3


def h2(x):
    return 6 * x + 4


xk = 0
k = 1
y = 0
e = 0.0001
times = 10000

while k < times:
    y = h(xk)
    a = h1(xk)
    if abs(a) <= e:
        break
    b = h2(xk)
    xk -= a / b
    k += +1
print("k = ", k)
print("x = ", xk)
print("y = ", y)
