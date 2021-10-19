import math


def factorization(a):
    i = 1
    print(f"\nThe divisors of {a}: ")
    while i <= math.sqrt(a):
        if a % i == 0:
            if a / i == i:
                print(int(i), end=' ')
            else:
                print(int(i), int(a/i), end=' ')
        i += 1


factorization(50)
factorization(81)
factorization(25)

print("Github is cool")