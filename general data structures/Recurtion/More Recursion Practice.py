def sum_of_list(l:list):
    if len(l) == 0:
        return 0
    else:
        return l[0] + sum_of_list(l[1:])

def count_x(s:str):
    if len(s) == 0:
        return 0
    elif s[0] == "x":
        return 1+count_x(s[1:])
    else:
        return count_x(s[1:])



def replace_x(s:str):
    #me and the gang hate the letter x
    if len(s) == 0:
        return ""
    elif s[0] == "x":
        return "y"+replace_x(s[1:])
    else:
        return s[0]+replace_x(s[1:])

def harmonic_sum(n):
    if n == 0:
        return 0
    else:
        return (1/n) + harmonic_sum(n-1)

def recursive_search(item, my_list:list):
    if len(my_list) == 0:
        return False
    elif item == my_list[0]:
        return True
    else:
        return recursive_search(item,my_list[1:])

def better_fib(n, a=1, b=1):
    if n == 1:
        return a
    if n == 2:
        return b
    print("call x2")
    return better_fib(n - 1, b, a + b)

print("Enter an integer:")
n = int(input())
print(better_fib(n))
