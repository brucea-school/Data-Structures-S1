import math


def prime_number_lister(n: int):
    b = list(range(2, n))
    while len(b) > 0:
        print(b[0])
        a = 1
        while a < len(b):
            if b[a] % b[0] == 0:
                b.remove(b[a])
            else:
                a += 1
        b.remove(b[0])


prime_number_lister(10000)

