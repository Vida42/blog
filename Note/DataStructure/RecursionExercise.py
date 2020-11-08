def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

def mul(a, b):
    if b == 0:
        return 0
    return a + mul(a, b-1)

def rec(x, y):
    if y == 0:
        return 1
    return x*rec(x, y-1)

def hailstone(n):
    # recursive
    print(n)
    if n == 1:
        return 1
    elif n%2 == 0:
        return 1+hailstone(n//2)
    else:
        return 1+hailstone(3*n+1)

def hailstone2(n):
    # iterative
    res = 1
    while n != 1:
        print(n)
        if n%2==0:
            n = n//2
        else:
            n = 3*n+1
        res += 1
    print(n)
    return res

def is_prime(n):
    # recursive
    def helper(index):
        if index == n:
            return True
        elif n % index == 0 or n == 1:
            return False
        else:
            return helper(index+1)
    return helper(2)


def is_prime2(n):
    # iterative
    if n == 1:
        return False
    k = 2
    while k < n:
        if n % k == 0:
            return False
        k += 1
    return True

def merge(n1, n2):
    if n1 == 0:
        return n2
    elif n2 == 0:
        return n1
    elif n1%10 < n2%10:
        return merge(n1//10, n2)*10 + n1%10
    else:
        return merge(n1, n2//10)*10 + n2%10

def make_fn_repeater(f, x):
    def repeat(i):
        if i == 0:
            return x
        else:
            return f(repeat(i-1))
    return repeat

a = 'lax'
b = 10

print("{0} has {1} rabbits.".format(a, b))

def merge(s1, s2):
    if len(s1) == 0:
        return s2
    elif len(s2) == 0:
        return s1
    elif s1[0] < s2[0]:
        return [s1[0]] + merge(s1[1:], s2)
    else:
        return [s2[0]] + merge(s1, s2[1:])

def mergesort(seq):
    if len(seq) <= 1:
        return seq
    else:
        mid len(seq) // 2
        return merge(mergesort(seq[:mid]),
            mergesort(seq[mid:]))



# def paths(x, y):
#     if x>y:
#         return []
#     elif x == y:
#         return [[x]]
#     else:
#         a = paths(x+1, y)
#         b = paths(x*2, y)
#         return [[x]+subpath for subpath in a+b]