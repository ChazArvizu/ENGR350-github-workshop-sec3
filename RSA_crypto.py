import random


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def rsa():
    p = random.randint(100, 1000)
    while not isPrime(p):
        p = random.randint(100, 1000)
    q = random.randint(100, 1000)
    while not isPrime(q):
        q = random.randint(100, 1000)
    n = p * q
    # print("p:", p)
    # print("q:", q)
    e = random.randint(100, 1000)
    while gcd(e, (p - 1) * (q - 1)) != 1:
        e = random.randint(100, 1000)
    print("n:", n)
    print("e:", e)
    print(f"gcd({e}, ({p} - 1) * ({q} - 1)) = {gcd(e, (p - 1) * (q - 1))}")
    print(f"key({n}, {e})")

print("Hello There")
rsa()
