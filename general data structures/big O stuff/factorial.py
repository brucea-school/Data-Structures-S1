

def factorial(n: int) -> int:
    total = 1
    for i in range(0, (n-1)):
        total *= (n-i)
    return total


print(factorial(5))
