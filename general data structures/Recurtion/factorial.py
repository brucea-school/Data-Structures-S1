
def factorial(n):
    result = 1
    for i in range(1,n+1):
            result *= i
    return result


def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)

def add_up(n):
    if n == 1:
        return 1
    else:
        return n + add_up(n-1)

def product(a,b):
    if b == 0:
        return 0
    else:
        return a + product(a,b-1)

def exp(b,e):
    if e == 0:
        return 1
    else:
        return b * exp(b,e-1)

def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

def num_vowels(word):
    if len(word) == 0:
        return 0
    elif word[0] in ['a','e','i','o','u']:
        return 1 + num_vowels(word[1:])
    else:
        return num_vowels(word[1:])

def sum_digits(n:int)->int:
    if n == 0:
        return 0
    s = str(n)
    if len(s) == 1:
        return n
    else:
        return int(s[0])+sum_digits(int(s[1:]))
def find_max(vals):

    if len(vals) == 0:
        return 0
    h = find_max(vals[1:])
    if vals[0] >= h:
        return vals[0]
    else:
        return h

print(find_max([3,8,1,67]))

print(sum_digits(5731))

print(num_vowels('Ryanaae'))

print(fib(30))

print(exp(4,4))



print(product(10,10))

print(add_up(20))

print(fact(5))

print(factorial(5))