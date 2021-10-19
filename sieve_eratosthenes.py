def sieve(n):
    prime_list = []
    # Creates a boolean array for all integers up to n
    prime = [True for i in range(n + 1)]
    x = 2
    while x * x <= n:
        if prime[x]:
            # Turns all multiples of x to False(not prime)
            for i in range(x * x, n + 1, x):
                prime[i] = False
        x += 1

    # Adds all instances of values with True to prime_list
    for y in range(2, n + 1):
        if prime[y]:
            prime_list.append(y)
    print(prime_list)


sieve(10000)
