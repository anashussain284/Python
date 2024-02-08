"""
Recursion

import sys

sys.setrecursionlimit(1000)
print(sys.getrecursionlimit())

i = 0
def greet():
    global i
    i += 1
    print("Hello", i)
    greet()

greet()

def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)
print(fact(5))

def walk(n):
    for i in range(n):
        print(i)
walk(5)

print("**********")

def walk(n):
    if n == 0:
        return
    print(n)
    walk(n - 1)    
    # print(n)
walk(5)

def sum_of_n_nos(n):
    sum = 0  
    for i in range(n + 1):
        sum += i
    print("a4", sum)

sum_of_n_nos(4) 

def sum_of_n_nos(n):
    if n == 1:
        return 1
    return n + sum_of_n_nos(n - 1)

print(sum_of_n_nos(3))    

0, 1, 1, 2, 3, 5, 8
-------------------
0, 1, 2, 3, 4, 5, 6

def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(4))

Write a Python program to calculate the sum of a list of numbers using recursion

def sum_of_list(x):
    sum = 0
    for i in range(len(x)):
        sum += x[i]
    print(sum)

def sum_of_list(x):
    if len(x) == 1:
        return x[0]
    else:
        return x[0] + sum_of_list(x[1:])

x = [1, 2, 3, 4]
print(sum_of_list(x))

Write a Python program to convert an integer to a string in any base using recursion.
"""