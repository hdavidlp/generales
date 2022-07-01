import collections
from math import factorial, sqrt





words = "Why sometimes I jave believed as many as six impossible things before breakfast".split()

""" 
Comprhesions Syntax
[expr(item) for item in iterable]
"""

print ([len(word) for word in words])

f = [len(str(factorial(x))) for x in range(20)]
print (f)


def is_prime(x):
    if x<2:
        return False
    for i in range(2,int(sqrt(x))+1):
        if x%i==0:
            return False
    return True

print ([x for x in range(101) if is_prime(x)])

iterable = ['Spring','Summer','Autumn','Winter']
iterator = iter(iterable)
print(next(iterator))


def gen123():
    yield 1
    yield 2
    yield 3

g = gen123()
print (next(g))
print (next(g))






