"""
1. ADD 2 NUMBERS (https://www.geeksforgeeks.org/python-program-to-add-two-numbers/)
n1 = input("Enter a number: ")
n2 = input("Enter a number: ")
print(float(n1) + float(n2))

def add(a, b):
    return a + b

n1 = 1
n2 = 1
s = add(n1, n2)
# print(s)
print(f"{n1} + {n2} = {s}")


x = 1
y = 1 

import operator

# s = operator.add(x, y)

s = lambda x, y : x + y
print(s(x, y))

x = 1
y = 5

def recursive_sum(x, y):
    print(f"x={x}, y={y}")
    if y == 0:
        return x
    else:
        return recursive_sum(x + 1, y - 1)
    
s = recursive_sum(x, y)
print(s)

2. MINIMUM OF 2 NUMBERS (https://www.geeksforgeeks.org/minimum-of-two-numbers-in-python/)


x = -1
y = -2

def min_no(x, y):
    if x < y:
        return x
    else:
        return y 

# z = min_no(x, y)    
# z = min(x, y)    
# z = sorted([x, y])[0]
    
from functools import reduce

z = reduce(lambda x, y : x if x < y else y, [x, y])
print(z)

3. MAXIMUM OF 2 NUMBERS (https://www.geeksforgeeks.org/maximum-of-two-numbers-in-python/)


def maximum(x, y):
    if x > y:
        return x
    else:
        return y
    
x = 21
y = 3
z = maximum(x, y)
z = max(x, y)
print(x if x > y else y)
z = lambda x, y : x if x > y else y
z = sorted([x, y])[-1]
z = [x if x > y else y]
print(z[0])

4. FIND `GCD` OF 2 NUMBERS (https://www.geeksforgeeks.org/python-program-to-find-the-gcd-of-two-numbers/)


import math

x = 10
y = 2
z = math.gcd(x, y)
print(z)

a = [1, 2, 3]
b = ["a", "b", "c"]
c = [j for i in [a, b] for j in i]
print(a)
print(b)
print(c)

"""

# def hcf(a, b):
#     if b == 0:
#         return a
#     else:
#         return hcf(b, a % b)

# a = 10
# b = 5
# c = hcf(a, b)
# print(c)

a = [1, 2, 3, 4, 5]
print(a)
print(a[13:])

