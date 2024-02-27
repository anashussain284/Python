"""
Python Program to Display Fibonacci Sequence Using Recursion
@link: https://www.programiz.com/python-programming/examples/fibonacci-recursion
"""
def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)

nterms = 788

if nterms <= 0:
    print("Enter a positive number")
else:
    print("Fibonacci sequence.")
    for i in range(nterms):
        print(fibo(i))