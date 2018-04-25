import random
import math
import matplotlib.pyplot as plt


def standard_normal_rand():
    while True:
        a = random.uniform(-4.0, 4.0)
        b = random.uniform(0.0, 3.0)
        if b < normal_pdf(a):
            return a, b


def bernoulli_rand():
    while True:
        a = random.uniform(0.0, 1.0)
        if a < bernoulli_pdf():
            return 0, a
        else:
            return 1, 1 - a


def exponential_rand():
    while True:
        a = random.uniform(0.0, 100.0)
        b = random.uniform(0.0, 3.0)
        if b <= exponential_pdf(a):
            return a, b


def poisson_rand():
    while True:
        a = random.randint(0, 50)
        b = random.uniform(0.0, 1.0)
        if b <= poisson_pdf(a):
            return a, b


def normal_pdf(x, mu=0, sigma=1):
    return (1 / (math.sqrt(2 * math.pi) * sigma)) * (math.exp(-math.pow(x - mu, 2) / (2 * math.pow(sigma, 2))))


def bernoulli_pdf():
    return 0.6


def exponential_pdf(x, lam=1):
    return lam * math.exp(-lam * x)


def poisson_pdf(x, lam=1):
    return (math.pow(lam, x) / math.factorial(x)) * math.exp(-lam)


x = []
y = []
for i in range(1, 500):
    a, b = standard_normal_rand()
    x.append(a)
    y.append(b)
plt.subplot(221)
plt.scatter(x, y)

x.clear()
y.clear()
for i in range(1, 100):
    a, b = bernoulli_rand()
    x.append(a)
    y.append(b)
plt.subplot(222)
plt.scatter(x, y)

x.clear()
y.clear()
for i in range(1, 500):
    a, b = exponential_rand()
    x.append(a)
    y.append(b)
plt.subplot(223)
plt.scatter(x, y)

x.clear()
y.clear()
for i in range(1, 1000):
    a, b = poisson_rand()
    x.append(a)
    y.append(b)
plt.subplot(224)
plt.scatter(x, y)

plt.show()
